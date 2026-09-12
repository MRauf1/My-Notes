---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Object Identity (Python)[^1]
> The `is` operator's test of whether two names reference the exact same [[Object (Python)|object]] in memory — a strict form of equality — as opposed to `==`, which tests only whether the referenced objects have equal values.

# Properties
- `==` is the form almost always used for equality checks; `is` is a much stronger, rarely needed test, typically reserved for single-instance objects like `None`, `True`, and `False`[^1].
- Because CPython caches and reuses small integers and short strings, two separately written literals with the same immutable value can be `is`-identical even though they came from distinct expressions — a side effect of this caching, not a language guarantee[^2].
- The `id` built-in exposes an object's identity directly, and the `sys.getrefcount` function reports its current reference count, which [[Garbage Collection (Python)|garbage collection]] uses to decide when to reclaim it[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=204&annotation=K7BIEQLZ)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=204&annotation=XU3QDF7L)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=205&annotation=7ILET9BI)
