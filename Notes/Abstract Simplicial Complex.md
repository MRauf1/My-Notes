---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Abstract Simplicial Complex[^1]
> An abstract simplicial complex $K$ is a collection of [[Abstract Simplex|abstract simplices]] over a vertex set $V$ that is closed under taking faces:
> $$\begin{align}
> \sigma \in K, \ \emptyset \neq \sigma' \subseteq \sigma \implies \sigma' \in K.
> \end{align}$$

An abstract simplicial complex specifies *how* vertices are connected, but not *where* they are in space.[^2] It is simply a collection of finite subsets of the integers closed under taking (nonempty) subsets, yet it can exactly encode the topology of any surface, no matter how complicated.[^3]

# Types
- **Subcomplex**: a subset $K' \subseteq K$ that is itself a simplicial complex.[^4]
- **Pure $k$-simplicial complex**: every simplex $\sigma' \in K$ is contained in some simplex of degree $k$ (possibly itself), and $K$ has no simplices of degree higher than $k$.[^5]
- [[Oriented Simplicial Complex]]
- [[Simplicial Surface]] (pure 2-complex with disk-like vertex neighborhoods)
- [[Simplicial Manifold]]

# Properties
- Local neighborhood operators: [[Simplicial Star]] $\operatorname{St}$, [[Simplicial Closure]] $\operatorname{Cl}$, and [[Simplicial Link]] $\operatorname{Lk}$.
- [[Boundary of Simplicial Complex|Boundary and interior]] of a pure subcomplex.
- Can be encoded by [[Simplicial Adjacency Matrix|adjacency (incidence) matrices]].
- One of the encodings of a [[Combinatorial Surface]]; more general than needed for surfaces, where a [[Halfedge Mesh]] is often preferred.[^6]

[^1]: [Crane, p. 9–10](zotero://open-pdf/library/items/9N6JDPI2?page=11&annotation=2AP56Z3H)
[^2]: [Crane, p. 9](zotero://open-pdf/library/items/9N6JDPI2?page=10&annotation=UQALZZ9C)
[^3]: [Crane, p. 10](zotero://open-pdf/library/items/9N6JDPI2?page=11&annotation=GPAXEFXL)
[^4]: [Crane, p. 10](zotero://open-pdf/library/items/9N6JDPI2?page=11&annotation=8VZKSAAE)
[^5]: [Crane, p. 10](zotero://open-pdf/library/items/9N6JDPI2?page=11&annotation=YVATE67N)
[^6]: [Crane, p. 8](zotero://open-pdf/library/items/9N6JDPI2?page=9&annotation=64BSQAGC)
