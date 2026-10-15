---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Abstract Simplex[^1]
> Given a vertex set $V = \{0, 1, \dots, n\}$, an **abstract $k$-simplex** is a [[Set|set]] of $k+1$ distinct vertices
> $$\begin{align}
> \sigma = \{i_0, i_1, \dots, i_k\} \subseteq V,
> \end{align}$$
> where $k \in \mathbb{Z}_{\ge 0}$ is called the **degree** of the simplex. The order of the vertices does not matter.
>
> Any nonempty subset $\sigma' \subseteq \sigma$ is again a simplex, called a **face** of $\sigma$; a strict subset $\sigma' \subsetneq \sigma$ is a **proper face**.[^2]

The simplex is *abstract*: it does not pin down a concrete shape in space, only which vertices are "right next to each other".[^3] Geometrically, it is the combinatorial counterpart of the convex hull of $k+1$ affinely independent points (compare the probability [[Simplex]] $\Delta^{K-1}$, which is one concrete geometric realization).

# Types
- 0-simplex $\{i\}$: a vertex (usually identified with $i \in V$).[^4]
- 1-simplex $\{i, j\}$: an edge.
- 2-simplex $\{i, j, k\}$: a triangle.
- 3-simplex: a tetrahedron.
- [[Oriented Simplex]] — a simplex together with a choice of vertex ordering up to even permutation.

# Properties
- A $k$-simplex has $\binom{k+1}{m+1}$ faces of degree $m$.
- Building block of an [[Abstract Simplicial Complex]].

[^1]: [Crane, p. 9](zotero://open-pdf/library/items/9N6JDPI2?page=10&annotation=ZRPI52H3)
[^2]: [Crane, p. 9](zotero://open-pdf/library/items/9N6JDPI2?page=10&annotation=IS3YJEFC)
[^3]: [Crane, p. 9](zotero://open-pdf/library/items/9N6JDPI2?page=10&annotation=PKKWUXTA)
[^4]: [Crane, p. 9](zotero://open-pdf/library/items/9N6JDPI2?page=10&annotation=XXL44CC4)
