---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Oriented Simplex[^1]
> An orientation of a $k$-simplex $\{i_0, \dots, i_k\}$ ($k \ge 1$) is an [[Equivalence Class|equivalence class]] of ordered tuples of its vertices, where two tuples are equivalent iff they differ by an even [[Permutation]] ([[Permutation Parity]]). Hence every $k$-simplex has exactly two orientations: the even permutations of a reference ordering and the odd ones.[^2] E.g. for a triangle,
> $$\begin{align}
> ijk &:= \{(i,j,k), (j,k,i), (k,i,j)\}, \\
> ikj &:= \{(i,k,j), (j,i,k), (k,j,i)\}.
> \end{align}$$
> A 0-simplex has only one ordering, but is still allowed two orientations, written $+i$ and $-i$.[^3]

Orientation is needed because it often encodes information about a quantity being measured or computed (e.g., the direction of flow along an edge).[^4] For an edge, $ij$ points from $i$ to $j$; for a triangle, the two orientations are the two directions (clockwise / counter-clockwise) of walking around it.[^5]

# Properties
- **Relative orientation of a face**: a proper face $\sigma'$ of an oriented simplex $\sigma$ has the same orientation as $\sigma$ if $\sigma'$ appears (as a prefix / consecutive sub-tuple) in some even permutation of $\sigma$. Exception for edges: $ij$ has the *same* orientation as $j$ and the *opposite* orientation of $i$ (it goes from $i$ to $j$).[^6]
- **Relative orientation of neighbors**: two oriented $k$-simplices $\sigma_1, \sigma_2$ sharing exactly $k$ vertices have the same orientation iff the orientations they induce on the shared $(k-1)$-face are opposite. E.g., $ij$ and $jk$ agree, $ij$ and $kj$ disagree.[^6]
- Building block of an [[Oriented Simplicial Complex]] and of the halfedges in a [[Halfedge Mesh]].
- These conventions lead to natural definitions of the boundary operator and of the signs in [[Simplicial Adjacency Matrix|signed adjacency matrices]].[^3]

[^1]: [Crane, p. 13](zotero://open-pdf/library/items/9N6JDPI2?page=14&annotation=54XJJNQF)
[^2]: [Crane, p. 13](zotero://open-pdf/library/items/9N6JDPI2?page=14&annotation=ZGGBQVHE)
[^3]: [Crane, p. 13](zotero://open-pdf/library/items/9N6JDPI2?page=14&annotation=2EJURYQJ)
[^4]: [Crane, p. 12–13](zotero://open-pdf/library/items/9N6JDPI2?page=13&annotation=4BVFRBDL)
[^5]: [Crane, p. 13](zotero://open-pdf/library/items/9N6JDPI2?page=14&annotation=XCLFS2FM)
[^6]: [Crane, p. 14](zotero://open-pdf/library/items/9N6JDPI2?page=15&annotation=RUWL4AEV)
