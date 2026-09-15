---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Adjacency Lists[^1]
> A vertex-centric representation of a [[Graph]] $G = (V, E)$ as an array `adj` of lists, where `adj[i]` holds every index $j$ such that $(i, j) \in E$.

# Operations
- **`add_edge(i, j)`**: append $j$ to `adj[i]`; constant time.[^2]
- **`remove_edge(i, j)`**: search `adj[i]` for $j$ and remove it; $O(\deg(i))$ time, where $\deg(i)$ (the out-degree of $i$) counts the edges of $E$ with source $i$.[^3]
- **`has_edge(i, j)`**: search `adj[i]` for $j$; also $O(\deg(i))$ time.[^4]
- **`out_edges(i)`**: return `adj[i]` directly; constant time.[^5]
- **`in_edges(i)`**: scan every vertex $j$'s list checking for the edge $(i, j)$ — no faster way exists in this simple representation — taking $O(n+m)$ time.[^6]

> [!abstract] Theorem 12.2[^7]
> The AdjacencyLists data structure implements the Graph interface. It supports `add_edge(i, j)` in constant time; `remove_edge(i, j)` and `has_edge(i, j)` in $O(\deg(i))$ time; and `in_edges(i)` in $O(n+m)$ time. The space used by an AdjacencyLists is $O(n+m)$.

| Operation | Time Complexity |
| --- | --- |
| `add_edge(i, j)` | $O(1)$ |
| `remove_edge(i, j)` / `has_edge(i, j)` | $O(\deg(i))$ |
| `out_edges(i)` | $O(1)$ |
| `in_edges(i)` | $O(n+m)$ |

# Space Usage
$O(n+m)$: one list header per vertex plus one entry per edge — asymptotically smaller than an [[Adjacency Matrix]]'s $O(n^2)$ whenever the graph is sparse.

# Properties
- [[Graph]]
- Best suited to algorithms that repeatedly explore a vertex's out-neighbours, such as [[Breadth-First Search]] and [[Depth-First Search]] on a graph.[^8]
- Contrast with [[Adjacency Matrix]], which trades slower edge-list queries for constant-time edge lookups and is preferable for dense graphs.

[^1]: [Morin, p. 244](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 244](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 246](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 246](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 246](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 246](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 247](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 248](zotero://select/library/items/HYS8NDAB)
