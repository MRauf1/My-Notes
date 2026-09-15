---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Adjacency Matrix[^1]
> A representation of an $n$-vertex [[Graph]] $G = (V, E)$ as an $n \times n$ boolean matrix $a$, where $a[i][j] = \text{true}$ if and only if $(i, j) \in E$.[^2]

# Operations
- **`add_edge(i, j)`**, **`remove_edge(i, j)`**, **`has_edge(i, j)`**: each just sets or reads the single matrix entry $a[i][j]$, taking constant time.[^3]
- **`out_edges(i)`**, **`in_edges(i)`**: must scan the entire row (respectively column) $i$ of $a$ to gather every index $j$ where $a[i][j]$ (respectively $a[j][i]$) is true, taking $O(n)$ time.[^4]

> [!abstract] Theorem 12.1[^5]
> The AdjacencyMatrix data structure implements the Graph interface. It supports `add_edge(i, j)`, `remove_edge(i, j)`, and `has_edge(i, j)` in constant time per operation, and `in_edges(i)` and `out_edges(i)` in $O(n)$ time per operation. The space used by an AdjacencyMatrix is $O(n^2)$.

| Operation | Time Complexity |
| --- | --- |
| `add_edge(i, j)` | $O(1)$ |
| `remove_edge(i, j)` | $O(1)$ |
| `has_edge(i, j)` | $O(1)$ |
| `out_edges(i)` / `in_edges(i)` | $O(n)$ |

# Space Usage
$O(n^2)$: storing $n^2$ boolean entries requires at least $n^2$ bits; a naive implementation using one value per entry uses on the order of $n^2$ bytes, while packing $w$ boolean values per memory word reduces this to $O(n^2/w)$ words.[^6]

# Properties
- [[Graph]]
- Despite its $O(n^2)$ memory and slow `in_edges(i)`/`out_edges(i)`, it remains useful for a *dense* graph (one with close to $n^2$ edges), where $O(n^2)$ space is unavoidable regardless of representation, and for applications that exploit algebraic operations on $a$ to compute properties of $G$.[^7]
- Contrast with [[Adjacency Lists]], the vertex-centric alternative representation.

[^1]: [Morin, p. 241](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 241](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 241](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 243](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 243](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 243](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 243](zotero://select/library/items/HYS8NDAB)
