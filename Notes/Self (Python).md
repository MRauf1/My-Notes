---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Self (Python)[^1]
> The special first argument automatically received by a [[Method (Python)|method]] — a function defined inside a class — named `self` by very strong convention, giving the method a handle back to the [[Instance (Python)|instance]] being processed.

# Properties
- Because a class is a factory for many instances, a method must go through `self` whenever it needs to fetch or set an attribute belonging to the one particular instance the current call is operating on, rather than the class itself or any other instance[^1].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=998&annotation=RA3Y5Q2W)
