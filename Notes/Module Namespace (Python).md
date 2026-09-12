---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Module Namespace (Python)[^1]
> Every name assigned at the top level of a [[Module (Python)|module]] file — not nested inside a function or class — becomes an attribute of that module's object once the file is imported; the module's global [[Scope (Python)|scope]] morphs into the module object's attribute namespace.

# Properties
- Module statements run only once, on the first import: Python creates an empty module object and executes the file's statements from top to bottom to populate it[^1].
- Internally, a module's namespace is just an ordinary [[Python Dictionary|dictionary]], reachable through the module object's `__dict__` attribute[^2].
- At a module's top level, the local and global scope are one and the same, so name lookup there follows the [[LEGB Rule (Python)|LEGB rule]] without its local or enclosing layers[^1].
- Unlike a function's local scope, which disappears once its call ends, a module's scope lives on for as long as the module stays loaded, providing a lasting source of tools to its importers[^1].
- Reaching an attribute with `object.attribute` ("qualification") is independent of scope lookup: the LEGB rule resolves only a bare leftmost name, while every name following a dot is looked up directly in that specific object instead[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=894&annotation=FYDYXGZC)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=896&annotation=6LAGQ9YF)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=897&annotation=IGT3SYIM)
