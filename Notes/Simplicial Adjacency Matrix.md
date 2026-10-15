---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Simplicial Adjacency Matrix[^1]
> Index the $k$-simplices of an [[Abstract Simplicial Complex]] $K$ for each degree $k$. The adjacency (incidence) matrix $A_k$ has one row per $(k+1)$-simplex and one column per $k$-simplex, with
> $$\begin{align}
> (A_k)_{rc} = \begin{cases} 1 & \text{if the } r\text{th } (k+1)\text{-simplex contains the } c\text{th } k\text{-simplex}, \\ 0 & \text{otherwise.} \end{cases}
> \end{align}$$
> So $A_0$ records which edges contain which vertices, $A_1$ which triangles contain which edges, etc., and $A_k \in \{0,1\}^{|K_{k+1}| \times |K_k|}$.

For an [[Oriented Simplicial Complex]], the **signed adjacency matrix** replaces each nonzero entry by $+1$ if the two simplices have the same relative orientation and $-1$ if opposite ([[Oriented Simplex]]).[^2]

# Properties
- Makes computation on simplicial complexes possible via numerical linear algebra.[^3]
- Signed adjacency matrices are closely linked to discrete [[Differential Form|differential forms]] (they are the discrete exterior derivative / transposed boundary operator), the foundation of many geometric algorithms.[^3]
- Each row of $A_k$ has exactly $k+2$ nonzeros, so for large complexes almost all entries are zero and $A_k$ must be stored as a [[Sparse Matrix]].[^4]
- Generalizes the vertex–edge incidence structure of a [[Graph]] (cf. [[Adjacency Matrix]]).
- More general than a [[Halfedge Mesh]]: it can represent nonmanifold configurations, nonorientable surfaces, and higher-dimensional complexes.

[^1]: [Crane, p. 17](zotero://open-pdf/library/items/9N6JDPI2?page=18&annotation=RBND4CK9)
[^2]: [Crane, p. 17](zotero://open-pdf/library/items/9N6JDPI2?page=18&annotation=2K3YBDEL)
[^3]: [Crane, p. 16](zotero://open-pdf/library/items/9N6JDPI2?page=17&annotation=DWRC7VLK)
[^4]: [Crane, p. 17](zotero://open-pdf/library/items/9N6JDPI2?page=18&annotation=XNERYYRK)
