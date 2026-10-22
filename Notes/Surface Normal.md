---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Surface Normal[^1]
> A vector $u \in \mathbb{R}^3$ is *normal* to the [[Smooth Surface]] $f: M \rightarrow \mathbb{R}^3$ at $p$ if
> $$\begin{align}
> df(X) \cdot u = 0 \quad \text{for all tangent vectors } X \in T_pM.
> \end{align}$$
> A normal of length one is a *unit normal* $N$. At each point there are exactly two unit normals, $+N$ and $-N$.

Tangent vectors $df(X)$ lie flat along the surface; normal vectors stick straight out of it. In coordinates one may take $N = \frac{f_x \times f_y}{|f_x \times f_y|}$ ([[Cross Product]]).

# Properties
- A consistent continuous choice of $N$ exists iff the surface is an [[Orientable Surface]].
- On an orientable surface, $N$ defines the [[Gauss Map]] $N: M \rightarrow S^2$; its differential is the [[Weingarten Map]].
- Because $|N| = 1$, $dN(X) \cdot N = 0$, so changes of the normal are always tangent to the surface (this is what makes the [[Shape Operator]] well-defined).[^2]
- Under linear maps, normals transform by the inverse transpose: [[Normal Vector Transformation]].

[^1]: [Crane, p. 30](zotero://open-pdf/library/items/9N6JDPI2?page=31&annotation=RCT3HGSY)
[^2]: [Crane, p. 39](zotero://open-pdf/library/items/9N6JDPI2?page=40&annotation=LMULAKA2)
