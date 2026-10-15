---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Abstract Simplicial Surface[^1]
> An abstract simplicial surface is a pure simplicial 2-complex ([[Abstract Simplicial Complex]]) in which the [[Simplicial Link|link]] of every vertex is a single loop of edges; equivalently, the [[Simplicial Star|star]] of every vertex is a combinatorial disk made of triangles. Such a complex is called **manifold**.
>
> A **simplicial surface with boundary** additionally allows the link of a vertex to be a simple path of edges instead of a loop.[^2]

Every vertex having a "disk-like" neighborhood ([[Topological Disk]]) is the combinatorial version of the defining property of a topological surface ([[Manifold]]).[^1]

# Types
- **Oriented simplicial surface**: one whose triangles can be given a consistent orientation, i.e., any two triangles sharing an edge have the same relative orientation ([[Oriented Simplex]]). Any surface that admits a consistent orientation is assumed to be consistently oriented.[^3]
- **Nonorientable simplicial surface**: no consistent orientation exists, e.g., a combinatorial Möbius band. Greedily "growing" an orientation outward from one triangle can loop around and hit a contradiction. Such surfaces are rare in practice but do occur.[^3][^4]

# Properties
- **Nonmanifold configurations** are excluded: e.g., three or more triangles meeting at an edge, or several "cones" of triangles meeting at a single vertex.[^5]
- The [[Boundary of Simplicial Complex|boundary]] $\operatorname{bd}(K)$ is always a collection of zero or more closed loops.[^6]
- For an oriented surface without boundary, every edge is contained in exactly two faces and the edges around each vertex have a cyclic order; this is the structure exploited by the [[Halfedge Mesh]].[^7]
- It is the $n = 2$ case of a [[Simplicial Manifold]].
- Topologically classified (when closed, connected, orientable) by its [[Genus (Topology)|genus]], computable via the [[Euler Characteristic]].
- A vertex of a simplicial surface is regular when its [[Vertex Valence|valence]] is $6$.

[^1]: [Crane, p. 14](zotero://open-pdf/library/items/9N6JDPI2?page=15&annotation=A32WW72N)
[^2]: [Crane, p. 15](zotero://open-pdf/library/items/9N6JDPI2?page=16&annotation=7BTK8LH6)
[^3]: [Crane, p. 15](zotero://open-pdf/library/items/9N6JDPI2?page=16&annotation=H7RFVUT3)
[^4]: [Crane, p. 16](zotero://open-pdf/library/items/9N6JDPI2?page=17&annotation=AQYQ6TAP)
[^5]: [Crane, p. 15](zotero://open-pdf/library/items/9N6JDPI2?page=16&annotation=GNZ5PSFB)
[^6]: [Crane, p. 15](zotero://open-pdf/library/items/9N6JDPI2?page=16&annotation=EJWREBNQ)
[^7]: [Crane, p. 18](zotero://open-pdf/library/items/9N6JDPI2?page=19&annotation=MX9LQFXA)
