---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Priority Queue[^1]
> A [[Queue]] variant whose `remove()` operation always returns the element with the highest priority currently stored — the smallest value, by convention — rather than the one that has been waiting longest.

Where a plain Queue's removal order is governed purely by arrival order (FIFO), a Priority Queue's is governed by a total order on the elements themselves; `add(x)` still inserts freely, but `remove()` must always be able to identify the current minimum. A [[Heap]] is the standard way to support this cheaply, without paying the cost of keeping every element in fully sorted order.[^1]

# Types
- [[Binary Heap]]
- [[Meldable Heap]]

# Properties
- [[Heap]]

[^1]: [Morin, p. 203](zotero://select/library/items/HYS8NDAB)
