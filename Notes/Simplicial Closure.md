---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Simplicial Closure[^1]
> For a subset $S$ of an [[Abstract Simplicial Complex]] $K$, the closure $\operatorname{Cl}(S)$ is the smallest (fewest elements) subcomplex of $K$ containing $S$; equivalently, $S$ together with all faces of its simplices:
> $$\begin{align}
> \operatorname{Cl}(S) = \{\sigma' \in K : \exists\, \sigma \in S,\ \sigma' \subseteq \sigma\}.
> \end{align}$$

# Properties
- $\operatorname{Cl}(i) = \{i\}$ for a vertex $i$, since a 0-simplex has no proper faces.[^2]
- $\operatorname{Cl}(\operatorname{St}(i))$ completes the [[Simplicial Star]] of $i$ into a subcomplex by adding the missing outer faces.[^3]
- Used to define the [[Simplicial Link]] and the [[Boundary of Simplicial Complex|boundary]] of a complex.
- Combinatorial analogue of the topological [[Closure Set|closure]].

[^1]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=KPYIVSE9)
[^2]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=CMLFNDMU)
[^3]: [Crane, p. 11](zotero://open-pdf/library/items/9N6JDPI2?page=12&annotation=5RQUF22G)
