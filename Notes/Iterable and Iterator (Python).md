---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Iterable and Iterator (Python)[^1]
> Python's iteration protocol: an iterable object is one that produces its items one at a time on request — either a physical sequence or a virtual one — by way of an iterator object that responds to `next()` calls to yield each successive result.

# Properties
- A [[Generator (Python)|generator]] is an iterable created either by a `yield`-based function or by wrapping [[Comprehension (Python)|comprehension]] syntax in parentheses instead of square brackets; rather than building a full collection up front, it produces each result on demand, one call to `next` at a time[^2].
- The built-in `range` generates successive integers lazily under this same protocol, which is why it must be wrapped in `list(...)` to force all its values to materialize for display[^3].
- Precisely, an iterable is any object with an `__iter__` method (equivalent to calling the `iter` built-in) that returns an iterator, and an iterator is any object with a `__next__` method (equivalent to calling the `next` built-in) that produces the next result and raises `StopIteration` once none remain; a language construct that drives this process, such as a [[For Loop (Python)|for loop]], is called an iteration tool rather than either of these[^4].
- A [[For Loop (Python)|for loop]] runs the full protocol automatically: it first calls `iter` on the iterable to obtain an iterator, then repeatedly calls `next` on that iterator until `StopIteration` signals the end[^5].
- For some objects, such as open files, the iterable and its iterator are the same object, since only a single forward scan is supported; iterators may also be nested arbitrarily, and an object like a generator expression, `enumerate`, or `zip` can act as both an iteration tool and an iterable in its own right[^6].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=126&annotation=MPW6K8XD)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=119&annotation=7H2EVS69)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=118&annotation=P73MPRMB)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=530&annotation=72MZVIKU)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=532&annotation=QE89A8Z4)
[^6]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=534&annotation=6QIZ9FSH)
