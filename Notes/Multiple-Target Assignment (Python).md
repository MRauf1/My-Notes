---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Multiple-Target Assignment (Python)[^1]
> An [[Assignment Statement (Python)|assignment]] of the form `a = b = c = value` that assigns every given target to the single object on the far right.

# Properties
- All of the targets end up referencing the exact same object in memory, rather than independent copies of it, so this form is worry-free only for immutable values, such as initializing a set of counters to zero[^2] — see [[Object Identity (Python)]] and [[Mutability (Python)]].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=430&annotation=MUNQJX4J)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=431&annotation=6WFEKR7N)
