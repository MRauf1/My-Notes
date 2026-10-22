---
tags:
  - mathematics
  - differential_geometry
---

# Definition

> [!info] Definition 1 ([[Curvature]] [[Function]] on [[Curve]])[^1]
> Given a [[Curvature Vector Field on Curve]] $T'(s)$, the curvature function on curve $\beta$ is $\kappa: I \rightarrow \mathbb{R}$ is
> $$
> \begin{align}
> \kappa(s) = ||T'(s)||
> \end{align}
> $$
> Note that $\kappa \geq 0$, with the larger value indicating sharper turn. Additional restriction making $\kappa$ non-zero can be applied, in which case, the unit [[Vector Field on Curve]] $N(s) = \frac{T'(s)}{\kappa}$ on curve $\beta$ tells the direction in which $\beta$ is turning at each [[Point]].

The change of the unit tangent splits into a direction (the principal normal $N$) and a magnitude (the curvature $\kappa$): $T' = \kappa N$ (O'Neill's convention; Crane writes $dT(X) = -\kappa N$ with $N$ a quarter turn counter-clockwise from $T$).[^2] The curvature of a circle is the reciprocal of its radius, $\kappa = 1/r$; in general $1/\kappa$ is the radius of the [[Osculating Circle]].[^3]

For curves it makes little difference whether curvature is measured as the change of the tangent or of the normal (they differ by a quarter turn); for surfaces, the change of the normal is the natural choice ([[Normal Curvature]]).[^4]

# Types
- [[Principal Normal Vector Field on Curve]]
- [[Binormal Vector Field on Curve]]

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=73)
[^2]: [Crane, p. 36](zotero://open-pdf/library/items/9N6JDPI2?page=37&annotation=AI5NT94E)
[^3]: [Crane, p. 36](zotero://open-pdf/library/items/9N6JDPI2?page=37&annotation=MI485UKQ)
[^4]: [Crane, p. 37](zotero://open-pdf/library/items/9N6JDPI2?page=38&annotation=4LRWYT9N)
