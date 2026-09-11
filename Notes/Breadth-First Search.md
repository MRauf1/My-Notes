---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Breadth-First Search
> A traversal that visits a tree's (or graph's) vertices level-by-level, starting at the root and moving downward, visiting the vertices within each level in order — much like reading a page of English text.[^1]

Breadth-first traversal is implemented with a [[Queue]], $q$, initialized to contain only the root $r$. At each step, the next vertex $u$ is dequeued from $q$, processed, and its non-nil children are enqueued onto $q$.[^1] Because $q$ enforces FIFO order, every vertex of one level is guaranteed to be processed before any vertex of the next.

# Properties
- Visits vertices in nondecreasing order of [[Tree Level|level]] (or of [[Graph Distance|distance]] from the source, for a general graph).
- Uses $O(w)$ auxiliary space, where $w$ is the maximum number of vertices at any one level.
- Contrast with [[Depth-First Search]], which descends as far as possible along a branch before backtracking.

[^1]: [Morin, p. 132](zotero://select/library/items/HYS8NDAB)
