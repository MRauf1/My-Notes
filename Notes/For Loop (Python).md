---
tags:
  - computer_science
  - python
---

# Definition
> [!info] For Loop (Python)[^1]
> A generic iteration [[Compound Statement (Python)|compound statement]] that steps through the items of any ordered sequence or other iterable object, working uniformly across strings, lists, tuples, sets, dictionaries, and user-defined iterables alike.

# Properties
- Its header assigns each item of the iterable to a target — often a simple name — one at a time and runs the loop body for each; after the loop ends normally, the target still refers to the last item visited[^2].
- Supports the same `break` and `continue` statements, and the same optional [[Loop Else Clause (Python)|else clause]], as a [[While Loop (Python)|while loop]][^2].
- Drives its iterable using the same [[Iterable and Iterator (Python)|iteration protocol]] used throughout Python: it obtains an iterator from the iterable and repeatedly advances it until the iterator signals there are no items left.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=501&annotation=R9S9KCPI)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=501&annotation=V9JLF942)
