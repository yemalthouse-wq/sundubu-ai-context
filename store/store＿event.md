# Store Events

## Purpose

Store events record changes in the operational state of the store.

These events are **not tied to a specific staff member**, but describe conditions affecting store performance.

Examples include peak periods, preparation delays, equipment failures, and inventory shortages.

---

## Initial Event Types

To maintain consistent logging, the initial set of events is intentionally limited.

- peak_start
- peak_end
- prep_delay
- equipment_issue
- inventory_shortage
- delivery_pause

New events should only be added after operational validation.

---

## Example

```json
{
  "timestamp": "2026-03-17T18:10:00",
  "event": "prep_delay",
  "note": "vegetable prep running late"
}
