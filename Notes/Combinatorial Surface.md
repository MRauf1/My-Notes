---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Combinatorial Surface[^1]
> A combinatorial surface is a description of a surface (roughly, the "outer shell" of a shape)[^2] that records only its *connectivity* — which pieces (vertices, edges, faces) are attached to which, and how — but not *where* those pieces are in space (no lengths, angles, or positions).

In discrete differential geometry, combinatorial surfaces play the same role that topological surfaces play in the smooth setting ([[Smooth Surface]]): they fix the topology before any geometry is attached.[^1]

# Types
Encodings of the connectivity of a combinatorial surface:[^3]
- [[Abstract Simplicial Complex]] — general; can encode objects far more complicated than surfaces (any dimension, nonmanifold configurations). Specialized to surfaces as a [[Simplicial Surface]].
- [[Simplicial Adjacency Matrix|Adjacency (incidence) matrices]] — a matrix encoding of a simplicial complex suited to numerical linear algebra.
- [[Halfedge Mesh]] — tailored to manifold, orientable 2-dimensional surfaces with general polygonal faces; the basic data structure of most surface-processing algorithms.

# Properties
- The basic simplifying assumption of differential geometry is that shapes are [[Manifold|manifold]]; for surfaces the most basic version is that every point has a neighborhood that is a [[Topological Disk]].[^4]
- Topological invariants such as the [[Euler Characteristic]] and [[Genus (Topology)|genus]] can be computed purely combinatorially.
- [[Vertex Valence]] is a purely combinatorial local quantity.

[^1]: [Crane, p. 7](zotero://open-pdf/library/items/9N6JDPI2?page=8&annotation=IATTC353)
[^2]: [Crane, p. 7](zotero://open-pdf/library/items/9N6JDPI2?page=8&annotation=GB5TGPU8)
[^3]: [Crane, p. 8](zotero://open-pdf/library/items/9N6JDPI2?page=9&annotation=64BSQAGC)
[^4]: [Crane, p. 8](zotero://open-pdf/library/items/9N6JDPI2?page=9&annotation=C6E3JGS5)
