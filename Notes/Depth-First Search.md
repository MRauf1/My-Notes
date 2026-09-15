---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Depth-First Search
> A traversal that, from the current vertex, descends as far as possible along a branch before backtracking, in contrast to [[Breadth-First Search]]'s level-by-level approach.

Depth-first traversal is naturally implemented either recursively — the call stack implicitly tracks the path back to the root — or iteratively with an explicit [[Stack]]: a vertex is pushed, processed, and its unvisited children are pushed in turn, so the most recently discovered vertex is always explored next. Equivalently, depth-first search is breadth-first search with the [[Queue]] replaced by a [[Stack]].[^1]

## On a general Graph
On a [[Graph]], each vertex $i$ is assigned a colour $c[i]$: **white** if never seen, **grey** while currently being visited (i.e. it is an ancestor of the vertex currently being explored), and **black** once fully processed. Visiting $r$ colours it grey, recursively visits every white vertex in $r$'s adjacency list, then colours $r$ black.[^2] Although most naturally recursive, this risks a stack overflow on large graphs, so an explicit stack is preferred in practice, replacing the recursion stack.[^3]

> [!abstract] Theorem 12.4[^4]
> When given as input a Graph, $g$, implemented using the AdjacencyLists data structure, `dfs(g, r)` and `dfs2(g, r)` each run in $O(n+m)$ time.

A key structural property: if $i$ is coloured grey and some white-vertices-only path leads from $i$ to $j$, then $j$ will be coloured grey, then black, *before* $i$ is coloured black.[^5] This underlies **cycle detection**: for any cycle $C$ reachable from $r$, let $i$ be the first vertex of $C$ coloured grey and $j$ the vertex preceding $i$ on $C$ — by the property above, $j$ is still grey (or becomes grey) while the edge $(j, i)$ is examined, revealing a path from $i$ back to $j$ in the depth-first-search tree together with the edge $(j, i)$, i.e. a cycle.[^6]

As with [[Breadth-First Search]], a refined bound in terms of $n_r$ (vertices reachable from $r$) and $m_r$ (edges sourced at them) applies:

> [!abstract] Theorem 12.5[^7]
> When given as input a Graph, $g$, implemented using the AdjacencyLists data structure, `bfs(g, r)`, `dfs(g, r)`, and `dfs2(g, r)` each run in $O(n_r + m_r)$ time.

# Types
- **Pre-order**: process a vertex before recursing into its children.
- **In-order**: for a [[Binary Tree]], recurse into the left child, process the vertex, then recurse into the right child — this visits the vertices of a [[Binary Search Tree]] in sorted order.
- **Post-order**: recurse into all children before processing the vertex.

# Properties
- Uses $O(h)$ auxiliary space, where $h$ is the height of the tree (or, on a general graph, the length of the longest path explored) — versus $O(w)$, the maximum level width, for [[Breadth-First Search]].
- On a general [[Graph]], visited vertices must be marked to avoid looping on a [[Graph Cycle|cycle]].
- [[Adjacency Lists]]

[^1]: [Morin, p. 250](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 250](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 251](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 252](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 252](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 252](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 253](zotero://select/library/items/HYS8NDAB)
