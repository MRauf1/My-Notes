---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Information Hiding[^1]
> A design technique in which a design decision is hidden inside a module's implementation and does not appear in the module's interface.

# Properties
- Makes a module's interface simpler while allowing the module to remain a [[Deep Module]].
- Only appropriate when the hidden information is not needed outside the module; hiding information that callers genuinely need is harmful rather than helpful.
- Can sometimes be improved by making the class encompassing the hidden information a bit larger.
- Its failure mode is [[Information Leakage]], where the hidden decision leaks into the interface or into another module anyway.
- Naturally furthered by writing [[General-Purpose Code]], since a general interface hides the specifics of any one use case.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
