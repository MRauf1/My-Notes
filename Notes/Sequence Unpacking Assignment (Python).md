---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Sequence Unpacking Assignment (Python)[^1]
> An [[Assignment Statement (Python)|assignment]] whose left side is a sequence of targets (a tuple or list) and whose right side is any iterable of the same length; Python assigns the right side's items to the left side's targets by position, left to right.

# Properties
- The right-hand collection is not restricted to matching the left side's type — a tuple of values can be assigned to a list of names, a string's characters to a tuple of names, and so on, as long as the lengths match[^1].
- Because Python builds a temporary tuple holding the right-hand side's original values before assigning, `first, second = second, first` swaps two variables' values without any explicit temporary variable[^2].
- A single starred target (`*rest`) within the left-hand sequence collects any items left over after the other targets are matched into a new [[Python List|list]]; if nothing is left over, the starred target is simply assigned an empty list rather than raising an error[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=420&annotation=XBXH2SXM)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=419&annotation=YN8QTHA3)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=426&annotation=W4X8KLH2)
