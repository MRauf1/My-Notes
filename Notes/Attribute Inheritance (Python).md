---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Attribute Inheritance (Python)[^1]
> When `object.attribute` is used on an [[Object (Python)|object]] derived from a [[Class (Python)|class]], Python searches a tree of linked objects for the first occurrence of `attribute`: first in `object` itself, then in all classes above it, from bottom to top and left to right.

# Properties
- Objects lower in the tree "inherit" attributes attached higher up; because the search always starts at the bottom, a lower object can override a same-named attribute defined higher up simply by redefining it there[^2].
- Runs independently for every single `object.attribute` reference — including a `self.attr` reference inside a method — so nothing about a prior search is cached or reused[^3].
- Happens only on attribute reference, never on attribute assignment: `object.attr = value` always creates or changes `attr` directly on `object`, with no tree search involved[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=991&annotation=AH2D4HX7)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=993&annotation=XDUVPNZS)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1014&annotation=ZWBWNQ9B)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1088&annotation=LXHFGAVN)
