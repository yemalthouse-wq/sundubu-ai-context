# Drop Review

## Purpose

This file defines how generated drop candidates are reviewed before being finalized.

drop is not auto-approved.
Human review is required before final confirmation.

---

## Review Principle

The reviewer does not evaluate personality.
The reviewer checks whether the action improved store flow.

---

## Review Questions

### 1. Was there a real store-flow improvement?
Did the action reduce delay, stabilize operations, or prevent disruption?

### 2. Was the contribution above baseline?
Normal attendance or routine behavior alone does not generate extra drop.

### 3. Was the effect observable in logs?
Check correlation with:
- staff_events
- store_events
- delivery_orders
- orders (future)

### 4. Was this recovery, support, or stabilization?
Priority is given to actions that protected flow during risk.

---

## Finalization Rule

- drop candidates may be proposed from rules
- final confirmation is manual
- no subtraction
- unclear cases are held, not forced

---

## Current Reviewer

Initial reviewer:
- Sei

Future reviewer model:
- owner / store manager only
