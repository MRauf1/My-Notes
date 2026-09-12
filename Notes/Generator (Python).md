---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Generator (Python)[^1]
> An object that produces a series of values over time rather than all at once; it can be created either by a generator function — an ordinary `def` whose body contains a [[Yield Statement (Python)|yield]] statement — or by a generator expression — a [[Comprehension (Python)|comprehension]] enclosed in parentheses instead of square brackets.

# Properties
- A generator function suspends and resumes execution around each yielded value, automatically retaining both its code location and its entire local scope between resumptions, so its local variables carry state forward from one produced value to the next[^1].
- Both forms automatically gain the same [[Iterable and Iterator (Python)|iteration-protocol]] interface: an `__iter__` method that simply returns the generator itself, and a `__next__` method that starts or resumes production and raises `StopIteration` once no results remain[^2].
- Because a generator is its own iterator, it supports only one active iteration pass; unlike some other iterables, two independent scans of the same generator positioned at different points are not possible[^3].
- Like other iterables, a generator saves memory and avoids upfront delay by producing results on demand instead of building an entire collection at once, which also lets it represent a series with no natural end[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=759&annotation=NPVVIRUB)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=773&annotation=ZUMAZ7A7)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=775&annotation=66KSAMR3)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=763&annotation=V8V72KSH)
