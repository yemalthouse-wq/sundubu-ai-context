"""
scripts/drop_candidate_generator/patterns.py

drop_candidate 生成ロジック。
確定dropは出さない。候補生成のみ。

判定順序（全パターン共通）:
  1. invalid_if check
  2. trigger_conditions check
  3. confidence_hint attach
  4. candidate_output build
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
    if window_state.get("delivery_orders", 0) < 2:
        return None
    if not _in_window(staff_event["time"], window_state["window_start"], window_state["window_end"]):
        return None
    if not (staff_event.get("event") in ("peak_handle", "solo_op")
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
    if not (staff_event.get("event") in ("new_support", "training")
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


def check_restorer(staff_event, window_state, prev_window_state):
    if prev_window_state is None:
        return None
    if not _in_window(staff_event["time"], window_state["window_start"], window_state["window_end"]):
        return None
    prev = prev_window_state.get("store_state")
    if not (staff_event.get("event") == "issue_resolve"
            and prev in ("slow", "peak")
            and window_state.get("store_state") == "normal"):
        return None
    confidence = "high" if prev == "peak" else "medium"
    return DropCandidate("Restorer", staff_event["staff"], staff_event["date"],
        f"{window_state['window_start']}-{window_state['window_end']}", confidence,
        {"staff_event_id": staff_event.get("id"),
         "store_event_ids": window_state.get("store_event_ids", []),
         "prev_store_event_ids": prev_window_state.get("store_event_ids", []),
         "delivery_order_ids": window_state.get("delivery_order_ids", [])},
        f"{prev} → normal への復旧")


def check_stabilizer(staff_event, window_state):
    if window_state.get("delivery_orders", 0) < 3:
        return None
    if window_state.get("store_state") != "peak":
        return None
    if not _in_window(staff_event["time"], window_state["window_start"], window_state["window_end"]):
        return None
    if not (staff_event.get("event") == "solo_op"
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


def _in_window(time_str, window_start, window_end):
    try:
        t = datetime.strptime(time_str, "%H:%M")
        s = datetime.strptime(window_start, "%H:%M")
        e = datetime.strptime(window_end, "%H:%M")
        return s <= t <= e
    except (ValueError, TypeError):
        return False


def run_all_patterns(staff_event, window_state, prev_window_state=None):
    candidates = []
    for checker in [
        lambda: check_guardian(staff_event, window_state),
        lambda: check_mentor(staff_event, window_state),
        lambda: check_restorer(staff_event, window_state, prev_window_state),
        lambda: check_stabilizer(staff_event, window_state),
    ]:
        result = checker()
        if result is not None:
            candidates.append(result)
    return candidates
