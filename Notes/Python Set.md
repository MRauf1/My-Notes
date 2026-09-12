---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python Set[^1]
> An unordered collection of unique, immutable ("hashable") objects, storing each distinct object only once and supporting the usual mathematical set operations.

# Properties
- Neither a [[Sequence (Python)|sequence]] nor a mapping like [[Python Dictionary|dictionaries]]; a set is created by calling the `set` built-in on an iterable or by using a set-literal expression.
- The set itself is mutable — items can be added or removed with methods like `add` and `remove` — even though the items it contains must be immutable by definition[^2].
- Because sets rely on hashability, [[Python List|lists]] and [[Python Dictionary|dictionaries]] cannot be stored as set members, though tuples of other immutables can; a set also cannot directly contain another set, since sets are themselves mutable — nesting requires the immutable `frozenset` variant instead[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=133&annotation=JWU74ZTA)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=133&annotation=2CWCGHMG)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=182&annotation=DU7VQPKZ)
