---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Exception Propagation (Python)[^1]
> Python stacks active [[Try Statement (Python)|try statements]] at runtime; when an exception is raised, it returns control to the most recently entered try statement with a matching handler, found by inspecting this stack of markers from the top down.

# Properties
- Once an exception reaches and is caught by a matching handler, its life is over — control never jumps back to any other matching try statement further up the stack; only the first (nearest) one gets the chance to handle it[^2].
- Where an exception ends up therefore depends on the runtime flow of control that led to it, not merely on the static structure of the code: the same `raise` can propagate to different handlers depending on what called what[^3].
- A [[Finally Clause (Python)|finally]] clause never stops this propagation: every enclosing try's finally block still runs on the way out as the exception unwinds outward, but none of them catches it, unlike a matching `except`[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1403&annotation=M8B3GQDS)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1404&annotation=82PY8LKM)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1405&annotation=NPZ6P9K6)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1404&annotation=KTFPGLIF)
