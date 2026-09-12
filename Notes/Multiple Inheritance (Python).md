---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Multiple Inheritance (Python)[^1]
> A [[Class (Python)|class]] has more than one [[Superclass and Subclass (Python)|superclass]] listed in its header's parentheses, so it and its instances inherit from all of them at once; the left-to-right order the superclasses are listed in gives the order they are searched in for a same-named attribute.

# Properties
- Useful for modeling something that genuinely belongs to more than one set of behaviors at once, combining the union of all its superclasses' attributes into one class[^2].
- When the same attribute name is defined in more than one superclass, the leftmost occurrence wins by default; an explicit reference through a specific superclass's name (e.g., `OtherSuper.attr`) overrides this default and picks a different one deliberately[^1].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=997&annotation=HDCNJWYC)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1208&annotation=IQRZ7MHE)
