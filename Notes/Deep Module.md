---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Deep Module[^1]
> A module whose implementation provides powerful functionality behind a simple interface. Contrasted with a shallow module, whose interface is complicated relative to the functionality it actually provides.

# Properties
- Depth is the ratio of the functionality a module provides to the complexity of its interface; deep modules hide more behind less interface.
- Interfaces should be designed to make the common case as simple as possible, so that the effective complexity of an interface is dominated by its commonly used features rather than its rarely used ones.
- Favored over many small, shallow components, such as short functions or a proliferation of small classes, since a large number of shallow components increases overall system complexity; see [[Module Decomposition]].
- Achieved largely through effective [[Information Hiding]].
- [[Pass-Through Method|Pass-through methods]] make a class shallower without adding functionality and are a red flag of poor decomposition.
- It is usually better for a module to have a simpler interface at the cost of a more complex implementation, pulling complexity downward and away from the module's callers.
- Good defaults make a module deeper by letting it do the right thing without requiring the user to ask for it explicitly; overexposing rarely used features raises [[Cognitive Load (Software Design)|cognitive load]] for no benefit.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
