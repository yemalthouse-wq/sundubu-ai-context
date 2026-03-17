"""
scripts/drop_candidate_generator/patterns.py
drop_candidate 生成ロジック。確定dropは出さない。候補生成のみ。
判定順序: 1.invalid_if 2.trigger_conditions 3.confidence_hint 4.candidate_output
"""

from datetime import datetime
from typing import Optional
import uuid

class DropCandidate:
    def __init__(self, pattern, staff, date, window, confidence, source_refs, note=None):
        self.candidate_id = f"dc_{date.replace('-', '')}_{uuid.uuid4().hex[:6]}"
        self.pattern = pattern
        self.staff = staff
        self.date = date
        self.window = window
        self.confidence = confidence
        self.source_refs = source_refs
        self.review_status = "pending"
        self.note = note

    def to_dict(self):
        return {
            "candidate_id": self.candidate_id,
            "pattern": self.pattern,
            "staff": self.staff,
            "date": self.date,
            "window": self.window,
            "confidence": self.confidence,
            "source_refs": self.source_refs,
            "review_status": self.review_status,
            "note": self.note,
        }

def check_guardian(staff_event, window_state):
    # invalid_if
    if window_state.get("delivery_orders", 0) < 2:
        return None
    if not _in_window(staff_event["time"], window_state["window_start"], window_state["window_end"]):
        return None
    # trigger: event_type contract正本値
    if not (staff_event.get("event_type") in ("peak_support", "solo_operation")
            and window_state.get("store_state") == "peak"
            and window_state.get("delivery_stable") is True):
        return None
    d = window_state.get("delivery_orders", 0)
    confidence = "high" if d >= 5 else "medium" if d >= 3 else "low"
    return DropCandidate("Guardian", staff_event["staff"], staff_event["date"],
        f"{window_state['window_start']}-{window_state['window_end']}", confidence,
        {"staff_event_id": staff_event.get("id"),
         "store_event_ids": window_state.get("store_event_ids", []),
         "delivery_order_ids": window_state.get("delivery_order_ids", [])},
        f"peak中 delivery {d}件をサポート")

def check_mentor(staff_event, window_state):
    if window_state.get("store_state") == "slow":
        return None
    if not _in_window(staff_event["time"], window_state["window_start"], window_state["window_end"]):
        return None
    # trigger: event_type contract正本値
    if not (staff_event.get("event_type") in ("training",)
            and window_state.get("delivery_orders", 0) >= 1):
        return None
    s = window_state.get("store_state")
    confidence = "high" if s == "peak" else "medium" if s == "normal" else "low"
    return DropCandidate("Mentor", staff_event["staff"], staff_event["date"],
        f"{window_state['window_start']}-{window_state['window_end']}", confidence,
        {"staff_event_id": staff_event.get("id"),
         "store_event_ids": window_state.get("store_event_ids", []),
         "delivery_order_ids": window_state.get("delivery_order_ids", [])},
        f"育成中に store_state={s} を維持")

RESTORER_MAX_RECOVERY_MINUTES = 30

def check_restorer(staff_event, window_state, prev_window_state, issue_event=None):
    """
    [A]近接モード: issue_eventのtimestamps差分で判定（3分以内も拾える）
    [B]windowモード: prev_window_stateのstore_state変化で判定（フォールバック）
    """
    has_issue_event = issue_event is not None
    has_prev_window = prev_window_state is not None
    # invalid_if
    if not has_issue_event and not has_prev_window:
        return None
    # trigger: event_type contract正本値
    if staff_event.get("event_type") != "issue_response":
        return None
    recovery_minutes = None
    mode = None
    if has_issue_event:
        recovery_minutes = _minutes_between(issue_event.get("time"), staff_event.get("time"))
        if recovery_minutes is not None and recovery_minutes >= 0 and recovery_minutes <= RESTORER_MAX_RECOVERY_MINUTES:
            mode = "proximity"
    if mode is None:
        if not has_prev_window:
            return None
        if not _in_window(staff_event["time"], window_state["window_start"], window_state["window_end"]):
            return None
        if not (prev_window_state.get("store_state") in ("slow", "peak")
                and window_state.get("store_state") == "normal"):
            return None
        mode = "window"
    if mode == "proximity":
        confidence = "high" if recovery_minutes <= 3 else "medium" if recovery_minutes <= 10 else "low"
        prev_state = issue_event.get("store_state", "unknown")
        window_label = f"{issue_event.get('time')}-{staff_event.get('time')}"
    else:
        prev_state = prev_window_state.get("store_state")
        confidence = "high" if prev_state == "peak" else "medium"
        window_label = f"{window_state['window_start']}-{window_state['window_end']}"
    source_refs = {
        "staff_event_id": staff_event.get("id"),
        "store_event_ids": window_state.get("store_event_ids", []),
        "delivery_order_ids": window_state.get("delivery_order_ids", []),
        "detection_mode": mode,
    }
    if mode == "proximity":
        source_refs["issue_event_id"] = issue_event.get("id")
        source_refs["recovery_minutes"] = recovery_minutes
    else:
        source_refs["prev_store_event_ids"] = prev_window_state.get("store_event_ids", [])
    note = (f"{prev_state} → normal ({recovery_minutes}分で復旧) [近接検出]"
            if mode == "proximity"
            else f"{prev_state} → normal への復旧 [window検出]")
    return DropCandidate("Restorer", staff_event["staff"], staff_event["date"],
        window_label, confidence, source_refs, note)

def check_stabilizer(staff_event, window_state):
    if window_state.get("delivery_orders", 0) < 3:
        return None
    if window_state.get("store_state") != "peak":
        return None
    if not _in_window(staff_event["time"], window_state["window_start"], window_state["window_end"]):
        return None
    # trigger: event_type contract正本値
    if not (staff_event.get("event_type") == "solo_operation"
            and "solo" in staff_event.get("tag", [])
            and window_state.get("delivery_stable") is True):
        return None
    d = window_state.get("delivery_orders", 0)
    confidence = "high" if d >= 6 else "medium" if d >= 4 else "low"
    return DropCandidate("Stabilizer", staff_event["staff"], staff_event["date"],
        f"{window_state['window_start']}-{window_state['window_end']}", confidence,
        {"staff_event_id": staff_event.get("id"),
         "store_event_ids": window_state.get("store_event_ids", []),
         "delivery_order_ids": window_state.get("delivery_order_ids", [])},
        f"ワンオペ peak完走 delivery {d}件")

def _minutes_between(start_time, end_time):
    """Restorer近接モード専用。"""
    try:
        s = datetime.strptime(start_time, "%H:%M")
        e = datetime.strptime(end_time, "%H:%M")
        return int((e - s).total_seconds() // 60)
    except (ValueError, TypeError):
        return None

def _in_window(time_str, window_start, window_end):
    try:
        t = datetime.strptime(time_str, "%H:%M")
        s = datetime.strptime(window_start, "%H:%M")
        e = datetime.strptime(window_end, "%H:%M")
        return s <= t <= e
    except (ValueError, TypeError):
        return False

def run_all_patterns(staff_event, window_state, prev_window_state=None, issue_event=None):
    """issue_event: Restorer近接モード用。省略時はwindowモードで動作。"""
    candidates = []
    for checker in [
        lambda: check_guardian(staff_event, window_state),
        lambda: check_mentor(staff_event, window_state),
        lambda: check_restorer(staff_event, window_state, prev_window_state, issue_event),
        lambda: check_stabilizer(staff_event, window_state),
    ]:
        result = checker()
        if result is not None:
            candidates.append(result)
    return candidates
