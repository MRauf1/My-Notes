---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Garbage Collection (Python)[^1]
> The automatic reclamation of an [[Object (Python)|object's]] memory once it is no longer referenced by any name or other object, freeing the programmer from manually allocating and releasing memory as required in lower-level languages.

# Properties
- CPython, the standard implementation, primarily uses reference counting: every object carries a counter of the references pointing to it, and its memory is reclaimed as soon as that counter drops to zero[^2].
- CPython supplements reference counting with an optional cyclic garbage collector that detects and reclaims groups of objects that reference each other in a cycle, which reference counting alone cannot free; it is enabled by default but can be disabled if a program is known not to create cycles[^3].
- This behavior is more conceptual than literal for certain cached objects: because CPython caches and reuses some small integers and short strings, reassigning a name away from one of these does not necessarily free it immediately — it may simply remain in an internal table for reuse, a detail normally irrelevant to ordinary code (see [[Object Identity (Python)]])[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=196&annotation=HCYU7TSW)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=197&annotation=7NEFDNS6)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=197&annotation=BEJYBGX5)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=203&annotation=GGQMGQ4T)
