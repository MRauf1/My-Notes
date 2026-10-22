---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Weingarten Map[^1]
> The Weingarten map is the differential $dN$ of the [[Gauss Map]] $N: M \rightarrow S^2 \subset \mathbb{R}^3$. For a tangent direction $X$, $dN(X) \in \mathbb{R}^3$ is the change in the unit normal as one moves along $X$.

# Properties
- $dN(X) \cdot N = 0$ (since $|N| = 1$), so $dN(X)$ is always tangent to the surface. Hence $dN(X) = -df(SX)$ for a unique $SX \in TM$: the [[Shape Operator]] $S$ is (minus) the Weingarten map expressed on $M$ rather than in $\mathbb{R}^3$ (O'Neill's sign convention).[^2] Many authors identify the two via an isometric identification of $TM$ with the tangent planes in $\mathbb{R}^3$.
- [[Normal Curvature]]: $\kappa_n(X) = -\frac{df(X) \cdot dN(X)}{|df(X)|^2}$.
- [[Second Fundamental Form]]: $\mathrm{II}(X, Y) = g(SX, Y) = -dN(X) \cdot df(Y)$.

[^1]: [Crane, p. 30](zotero://open-pdf/library/items/9N6JDPI2?page=31&annotation=KXR94S9R)
[^2]: [Crane, p. 39](zotero://open-pdf/library/items/9N6JDPI2?page=40&annotation=LMULAKA2)
