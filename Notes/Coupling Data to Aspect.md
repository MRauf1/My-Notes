---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Coupling Data to Aspect[^1]
> In [[Object-Oriented Design]], binding data to the concept of an object ties that data to a single aspect — the particular intention or use case through which the data is given purpose — making it hard to view or manipulate the data from any other point of view.

# Properties
- An object's data layout is defined as the union of the data required for its expected manipulations, so when different aspects need different, overlapping subsets of that data, the set of values that must travel around the system as one unit only grows, which is what eventually forces a class to be refactored into two or more classes.
- It is easier to recognize when a relationship needs to exist than to recognize when it no longer does, so statically typed objects tend to accumulate connections, including defunct ones, over time rather than shed them.
- [[Data-Oriented Design]] avoids this by keeping data in one place and operations in another, linking them only through the aspect intrinsic to a given transform rather than through a fixed object definition; this makes refactors that would be large and difficult in [[Object-Oriented Design]] trivial or unnecessary, at the cost of having to track which data each operation requires and the risk of desynchronization between data and operations.

[^1]: [Data-Oriented Design](zotero://open-pdf/library/items/QRB7VVMF?page=18&annotation=XDLQZTVC)
