---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Pass-Through Method[^1]
> A method that does nothing but pass its arguments through to another method's call, without adding meaningful functionality of its own.

# Properties
- A symptom of poor [[Module Decomposition|class decomposition]], where multiple layers share the same or a similar abstraction.
- Makes classes shallower and increases interface complexity without increasing the system's total functionality; see [[Deep Module]].
- Creates unnecessary [[Dependency (Software Design)|dependency]] between the classes involved.
- Usually indicates confusion about the division of responsibility between classes; the interface to a piece of functionality should typically live in the same class that implements it.
- Not a problem if the method's signature happens to be reused but the method itself adds genuinely new functionality.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
