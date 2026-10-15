---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Simplicial Star[^1]
> For a subset $S$ of an [[Abstract Simplicial Complex]] $K$ (not necessarily a subcomplex), the star $\operatorname{St}(S)$ is the collection of all simplices of $K$ that contain some simplex of $S$:
> $$\begin{align}
> \operatorname{St}(S) = \{\sigma \in K : \exists\, \tau \in S,\ \tau \subseteq \sigma\}.
> \end{align}$$
> For a single vertex $i$: $\operatorname{St}(i) = \{\sigma \in K : i \in \sigma\}$.[^2]

The star of a vertex is its "local neighborhood", but it is generally **not** a simplicial complex, since it lacks the "outer" faces (e.g., the outer ring of edges around a vertex).[^3]

# Properties
- $\operatorname{St}(\operatorname{Cl}(i)) = \operatorname{St}(i)$ for a vertex $i$, since $\{i\}$ has no proper faces.[^4]
- Taking the [[Simplicial Closure]] gives the smallest subcomplex containing it, $\operatorname{Cl}(\operatorname{St}(S))$; the difference is the [[Simplicial Link]].
- In a [[Simplicial Surface]], the star of every interior vertex is a combinatorial disk of triangles.

[^1]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=KPYIVSE9)
[^2]: [Crane, p. 10](zotero://open-pdf/library/items/9N6JDPI2?page=11&annotation=QDERX8X3)
[^3]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=5RQUF22G)
[^4]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=CMLFNDMU)
