---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Mutual Exclusion[^1]
> A region of code where only a single processor (or thread) can operate at a time, created using lock and unlock synchronization operations.

# Properties
- Prevents [[Data Race|data races]] on shared memory locations by ensuring accesses to the protected region are serialized.
- Built from hardware-supplied [[Atomic Operation|atomic operations]], since without an atomic read-modify-write primitive, the cost of building basic synchronization mechanisms grows unreasonably as the number of processors increases.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=144&annotation=BBM2WPDS)
