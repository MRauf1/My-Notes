---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Information Leakage[^1]
> Occurs when a design decision is reflected in more than one module, creating a dependency between them so that any change to the decision requires changes to all the involved modules. Also occurs when the decision is reflected in a module's interface rather than being hidden inside its implementation.

# Properties
- The failure mode of [[Information Hiding]].
- A source of [[Dependency (Software Design)|dependency]] between otherwise separate modules.
- Reduced by making each module as independent of the others as possible.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
