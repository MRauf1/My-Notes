---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Simplicial Link[^1]
> For a subset $S$ of an [[Abstract Simplicial Complex]] $K$, the link is
> $$\begin{align}
> \operatorname{Lk}(S) = \operatorname{Cl}(\operatorname{St}(S)) \setminus \operatorname{St}(\operatorname{Cl}(S)),
> \end{align}$$
> where $\operatorname{St}$ is the [[Simplicial Star]] and $\operatorname{Cl}$ the [[Simplicial Closure]].

For a vertex $i$, the link is exactly the "ring" of outer faces around $i$ that are missing from $\operatorname{St}(i)$ but present in $\operatorname{Cl}(\operatorname{St}(i))$, i.e., the simplices of the closed star that do not contain $i$.[^2]

# Properties
- Characterizes manifoldness combinatorially:
	- [[Simplicial Surface]]: the link of every vertex is a single loop of edges (or a simple path for boundary vertices).
	- [[Simplicial Manifold|Simplicial $n$-manifold]]: the link of every vertex is a simplicial $(n-1)$-sphere.

[^1]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=KPYIVSE9)
[^2]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=6EXTKLFG)
