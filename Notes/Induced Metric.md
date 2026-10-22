---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Induced Metric[^1]
> Let $f: M \rightarrow \mathbb{R}^3$ be a [[Smooth Surface]] with [[Tangent Map|differential]] $df$. The metric induced by $f$ is the map
> $$\begin{align}
> g(X, Y) = df(X) \cdot df(Y)
> \end{align}$$
> for tangent vectors $X, Y \in T_pM$, where $\cdot$ is the standard [[Dot Product]] on $\mathbb{R}^3$. In particular, the length of a pushed-forward vector is $|df(X)| = \sqrt{df(X) \cdot df(X)} = \sqrt{g(X, X)}$, which in general differs from the original length $\sqrt{\langle X, X\rangle}$ measured in the plane.

The induced metric is "the [[Dot Product]] of $\mathbb{R}^3$ pulled back to $M$" ($g = f^*(\cdot)$): it lets one measure lengths and angles of arrows on $M$ *as they appear on the surface*, while still working in the flat domain. It is the special case of a [[Riemannian Metric]] obtained from an immersion into Euclidean space.

**Not a distance function.** Despite the name, $g$ is not a [[Metric]] in the metric-space sense: it eats two *tangent vectors at the same point* and returns a (possibly negative) number, it is an [[Inner Product]] on each [[Tangent Space]]. A genuine distance function is recovered from it by integrating lengths of curves; see [[Riemannian Metric]].

> [!abstract] Matrix Representation[^2]
> If $J$ is the $3 \times 2$ [[Jacobian Matrix]] of $f$ and $\mathrm{I} \in \mathbb{R}^{2 \times 2}$ represents $g$, then $u^T \mathrm{I} v = (Ju)^T (Jv)$ for all $u, v$, so
> $$\begin{align}
> \mathrm{I} = J^T J = \begin{bmatrix} E & F \\ F & G \end{bmatrix}, \quad E = f_x \cdot f_x,\ F = f_x \cdot f_y,\ G = f_y \cdot f_y.
> \end{align}$$

$F$ appears twice because $g$ is symmetric ($g(X,Y) = g(Y,X)$, i.e. $f_x \cdot f_y = f_y \cdot f_x$). The letters $E, F, G$ are coordinate-dependent and carry little geometric meaning on their own, but are common in older literature.[^3] $\mathrm{I}$ is the matrix of a [[Bilinear Form]], so under a change of coordinates $P$ it transforms as $\mathrm{I} \mapsto P^{-T} \mathrm{I} P^{-1}$.

# Properties
- Historically called the [[First Fundamental Form]]: $\mathrm{I}(X, Y) := g(X, Y)$.
- Symmetric and positive definite ($\mathrm{I} = J^TJ$ is a [[Positive Definite Matrix]] since $J$ has full rank for an immersion).
- $f$ is [[Conformal Map|conformal]] iff $g = a\langle \cdot, \cdot \rangle$ for a positive function $a$, and [[Isometric Parameterization|isometric]] iff $g = \langle \cdot, \cdot \rangle$.
- Principal directions are orthogonal with respect to $g$ ([[Principal Curvature]]).

[^1]: [Crane, p. 29](zotero://open-pdf/library/items/9N6JDPI2?page=30&annotation=SPIM9EV7)
[^2]: [Crane, p. 44](zotero://open-pdf/library/items/9N6JDPI2?page=45&annotation=9JFM4KPV)
[^3]: [Crane, p. 44](zotero://open-pdf/library/items/9N6JDPI2?page=45&annotation=W4WHEZJQ)
