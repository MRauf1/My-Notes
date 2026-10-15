---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Euler Characteristic[^1]
> For a polygonal surface with $V$ vertices, $E$ edges, and $F$ faces,
> $$\begin{align}
> \chi = V - E + F,
> \end{align}$$
> which is a topological invariant: it does not depend on how the surface is subdivided.

# Properties
- **Euler–L'Huilier formula**: for a connected, compact, orientable surface without boundary of [[Genus (Topology)|genus]] $g$,[^2]
$$\begin{align}
V - E + F = 2 - 2g.
\end{align}$$
  It holds for [[Simplicial Surface|simplicial surfaces]] as well as surfaces made of general $n$-gons. A sphere has $\chi = 2$, a torus $\chi = 0$.
- Computable purely combinatorially from any encoding of a [[Combinatorial Surface]] (e.g., counting orbits in a [[Halfedge Mesh]]).

[^1]: [Crane, p. 22](zotero://open-pdf/library/items/9N6JDPI2?page=23&annotation=BVKCGQKP)
[^2]: [Crane, p. 22](zotero://open-pdf/library/items/9N6JDPI2?page=23&annotation=EZ2RRU5L)
