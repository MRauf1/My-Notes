---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Breadth-First Search
> A traversal that visits a tree's (or graph's) vertices level-by-level, starting at the root and moving downward, visiting the vertices within each level in order — much like reading a page of English text.[^1]

Breadth-first traversal is implemented with a [[Queue]], $q$, initialized to contain only the root $r$. At each step, the next vertex $u$ is dequeued from $q$, processed, and its non-nil children are enqueued onto $q$.[^1] Because $q$ enforces FIFO order, every vertex of one level is guaranteed to be processed before any vertex of the next.

## On a general Graph
Run on a [[Graph]] rather than a tree, the algorithm is otherwise identical, with one addition: since a graph vertex can have several incoming edges (and cycles can lead back to it), an auxiliary boolean array `seen` tracks which vertices have already been enqueued, so that no vertex is added to $q$ more than once.[^2] Given an [[Adjacency Lists|Adjacency List]]-represented graph, each vertex is enqueued/dequeued in $O(1)$ time (total $O(n)$), and each vertex's adjacency list is scanned exactly once, processing each edge in $O(1)$ time (total $O(m)$).[^3]

> [!abstract] Theorem 12.3[^4]
> When given as input a Graph, $g$, implemented using the AdjacencyLists data structure, `bfs(g, r)` runs in $O(n+m)$ time.

`bfs(g, r)` enqueues (and eventually dequeues) exactly every vertex reachable from $r$, and — since $q$'s FIFO order forces every vertex at distance $k$ from $r$ to be enqueued before any vertex at distance $k+1$ — visits vertices in strictly nondecreasing order of [[Graph Distance|distance]] from $r$; vertices unreachable from $r$ are never visited.[^5]

### Shortest Paths
This distance-ordering property makes `bfs(g, r)` a direct way to compute shortest paths from $r$ to every other vertex: an auxiliary array $p$ of length $n$ records, for each newly-enqueued vertex $j$ discovered from $i$, $p[j] \leftarrow i$ — the second-to-last vertex on a shortest path from $r$ to $j$. Following $p[j], p[p[j]], \dots$ back to $r$ reconstructs (the reversal of) a shortest path.[^6] This only computes a shortest path by *number of edges*, and so only gives correct shortest paths on an unweighted graph (equivalently, one where every edge has the same weight); on a graph with unequal edge weights, the fewest-edges path found this way need not be the minimum-total-weight path, and an algorithm such as Dijkstra's is needed instead.

A more refined bound accounts for unreachable vertices: letting $n_r$ and $m_r$ be the number of vertices reachable from $r$ and the edges sourced at them, respectively,

> [!abstract] Theorem 12.5[^7]
> When given as input a Graph, $g$, implemented using the AdjacencyLists data structure, `bfs(g, r)`, `dfs(g, r)`, and `dfs2(g, r)` each run in $O(n_r + m_r)$ time.

# Properties
- Visits vertices in nondecreasing order of [[Tree Level|level]] (or of [[Graph Distance|distance]] from the source, for a general graph).
- Uses $O(w)$ auxiliary space, where $w$ is the maximum number of vertices at any one level.
- Contrast with [[Depth-First Search]], which descends as far as possible along a branch before backtracking.

[^1]: [Morin, p. 132](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 248](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 249](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 249](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 249](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 250](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 253](zotero://select/library/items/HYS8NDAB)
