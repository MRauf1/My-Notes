---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Depth-First Search
> A traversal that, from the current vertex, descends as far as possible along a branch before backtracking, in contrast to [[Breadth-First Search]]'s level-by-level approach.

Depth-first traversal is naturally implemented either recursively — the call stack implicitly tracks the path back to the root — or iteratively with an explicit [[Stack]]: a vertex is pushed, processed, and its unvisited children are pushed in turn, so the most recently discovered vertex is always explored next.

# Types
- **Pre-order**: process a vertex before recursing into its children.
- **In-order**: for a [[Binary Tree]], recurse into the left child, process the vertex, then recurse into the right child — this visits the vertices of a [[Binary Search Tree]] in sorted order.
- **Post-order**: recurse into all children before processing the vertex.

# Properties
- Uses $O(h)$ auxiliary space, where $h$ is the height of the tree (or, on a general graph, the length of the longest path explored) — versus $O(w)$, the maximum level width, for [[Breadth-First Search]].
- On a general [[Graph]], visited vertices must be marked to avoid looping on a [[Graph Cycle|cycle]].
