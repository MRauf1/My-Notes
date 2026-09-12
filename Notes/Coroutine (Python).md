---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Coroutine (Python)[^1]
> A [[Function (Python)|function]] that can suspend its own execution with `await`/`async` until a required result becomes available, so that other tasks may run while it waits.

# Properties
- Chiefly used for IO-bound work: a coroutine can pause itself until a slow operation such as network or disk IO completes, letting other parts of a program run during the wait instead of blocking on it[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=595&annotation=PVWIBPB8)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=799&annotation=A95GTDV4)
