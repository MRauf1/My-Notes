---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Superclass and Subclass (Python)[^1]
> In a [[Class (Python)|class's]] inheritance tree, a superclass is a class positioned higher up, whose attributes are shared by every class and instance beneath it; a subclass is a class positioned lower down that inherits from — and may override — attributes defined in its superclasses.

# Properties
- A class lists its superclasses in parentheses on its own header line; every instance and class then links automatically into this tree, letting [[Attribute Inheritance (Python)|inheritance search]] climb from a subclass toward its superclasses[^2].
- Because inheritance search starts at the bottom of the tree, a subclass can override a superclass's behavior simply by redefining the same attribute name lower down, without touching the superclass's own code at all[^1].
- A superclass whose method calls another method it expects a subclass to supply, without defining that method itself, is called an abstract superclass; if no subclass ever supplies it, the inheritance search for that method simply fails when it is finally called[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=993&annotation=XDUVPNZS)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=996&annotation=MAFBJEVG)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1099&annotation=UK4UTN2W)
