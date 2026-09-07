---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Object-Oriented Design[^1]
> A design methodology centered on the problem definition rather than on the data: objects are not real things but abstract representations of the context in which a problem will be solved, and they manipulate the data needed to represent them.

# Properties
- Builds the real-world problem domain directly into the code by binding data and the operations on it together inside objects, without regard for the hardware or for real-world data patterns and quantities, unlike [[Data-Oriented Design]].
- Lets a first version of the design document become the first version of the code, allowing a quick attempt at a solution.
- Couples the problem domain with the implementation, which creates inertia against change: because higher-level change is inevitable, whether from a genuine design change or merely a misunderstanding of the design, this coupling shows its weaknesses as designs change in the real world.
- Ties a specific [[Coupling Data to Aspect|aspect]] (intended use case) to an object's data, which is the underlying reason refactoring tends to become large and difficult as an object's responsibilities evolve.
- Can still be useful for "cold" code where maintaining internal consistency is preferred over efficiency and mutability.

[^1]: [Data-Oriented Design](zotero://open-pdf/library/items/QRB7VVMF?page=15&annotation=E29RLVLT)
