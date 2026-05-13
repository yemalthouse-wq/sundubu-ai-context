"""Window definitions for Phase 1.7 (hardcoded JST v1)."""

from datetime import time

VERSION = "hardcoded_v1_jst"

WINDOW_DEFINITIONS = (
    ("lunch", time(11, 0), time(14, 30)),
    ("idle", time(14, 30), time(17, 0)),
    ("dinner", time(17, 0), time(22, 0)),
)
