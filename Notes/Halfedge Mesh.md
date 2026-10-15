---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Halfedge Mesh[^1]
> For every unoriented edge $\{i, j\}$ of a surface, introduce two oriented **halfedges** $ij \neq ji$; let $H$ be the set of all halfedges. A halfedge mesh is the pair of maps
> $$\begin{align}
> \eta &: H \to H, \quad \eta(ij) = ji && \text{(twin)} \\
> \rho &: H \to H, \quad \rho(ij) = jk \quad \forall\, ijk \in K && \text{(next)}
> \end{align}$$
> where "next" takes each halfedge of an oriented face to the following halfedge around that face.
>
> Conversely, **any** pair of maps $\rho, \eta$ describes a valid combinatorial surface provided[^2]
> 1. $|H|$ is even,
> 2. $\rho$ and $\eta$ are [[Permutation|permutations]] of $H$,
> 3. $\eta$ is a fixed-point-free involution: $\eta(\eta(h)) = h$ and $\eta(h) \neq h$ for all $h \in H$.

Formally, a halfedge mesh encodes a surface as a 2-dimensional CW complex, rather than a simplicial complex.[^3]

# Properties
- **Recovering mesh elements as orbits**:[^4]
	- faces = orbits of $\rho$,
	- edges = orbits of $\eta$,
	- vertices = orbits of $\rho \circ \eta$ ([[Function Composition]]; cycles through the halfedges leaving a vertex).
- $|H| = 2|E|$ for a surface without boundary.[^1]
- Indexing twins as $(0,1), (2,3), \dots$ makes $\eta(h) = h + 1$ for even $h$ and $h - 1$ for odd $h$, so the surface is described entirely by $\rho$: **every permutation of an even number of things describes a combinatorial surface.**[^5]
- Relies on two facts about an oriented manifold surface without boundary: every edge is in exactly two polygons, and the edges around a vertex have a cyclic order. These hold for $n$-gon faces, not just triangles.[^6]
- **Boundary**: treat each boundary loop as a single (marked) many-sided polygon, "filling the holes" to obtain a surface without boundary.[^7]
- **Compared with an [[Abstract Simplicial Complex]] / [[Simplicial Adjacency Matrix]]**:[^3]
	- Less general: cannot represent dangling edges or other nonmanifold configurations, nonorientable surfaces such as the Möbius band, or higher-dimensional shapes (volumes).
	- More general: supports arbitrary polygonal faces, and can describe triangulations no simplicial complex can (e.g., two triangles sharing more than one edge), sometimes with fewer elements.[^8]
- The basic data structure for most surface algorithms on a [[Combinatorial Surface]].

[^1]: [Crane, p. 18](zotero://open-pdf/library/items/9N6JDPI2?page=19&annotation=KA9N2NJ3) and [Crane, p. 18](zotero://open-pdf/library/items/9N6JDPI2?page=19&annotation=E5CZGW28)
[^2]: [Crane, p. 19](zotero://open-pdf/library/items/9N6JDPI2?page=20&annotation=93ABNIDG)
[^3]: [Crane, p. 18](zotero://open-pdf/library/items/9N6JDPI2?page=19&annotation=NJ68U9RS)
[^4]: [Crane, p. 19](zotero://open-pdf/library/items/9N6JDPI2?page=20&annotation=KR9DMP5W)
[^5]: [Crane, p. 19](zotero://open-pdf/library/items/9N6JDPI2?page=20&annotation=AD7XTU33)
[^6]: [Crane, p. 18](zotero://open-pdf/library/items/9N6JDPI2?page=19&annotation=MX9LQFXA)
[^7]: [Crane, p. 21](zotero://open-pdf/library/items/9N6JDPI2?page=22&annotation=II7APWGY)
[^8]: [Crane, p. 19](zotero://open-pdf/library/items/9N6JDPI2?page=20&annotation=9F8FSB46)
