---
tags: mathematics, differential_geometry
---

# Definition

> [!info] Definition 1 (Frenet [[Frame Field]])[^1]
> Let $\beta$ be a [[Unit Speed Curve]] in $\mathbb{R}^3$ with $\kappa > 0$ ([[Curvature Function on Curve]]). Then the three [[Vector Field]] $T, N, B$ ([[Unit Tangent Vector Field on Curve]], [[Principal Normal Vector Field on Curve]], [[Binormal Vector Field on Curve]]) are [[Unit Vector Field on Curve]] that are mutually [[Orthogonal Vector|orthogonal]] at every [[Point]]. We call $T, N, B$ the Frenet Frame Field on $\beta$.
> More specifically, $T = \beta', N = \frac{T'}{\kappa}, B = T \times N$.

For studying curves, it is more informative and effective to use the curve's Frenet Frame Field rather than the [[Natural Frame Field]].

While Frenet Frame Field deals with [[Unit Speed Curve]], by applying a [[Unit Speed Curve Reparameterization]] $\overline{\beta}$ on $\beta$, all of the corresponding functions are given (e.g. $\kappa(t) = \overline{\kappa}(s(t))$ where $s(t)$ is the [[Curve Arc Length Function]] for $\beta$). The Frenet apparatus is the same for the two curves. However, finding this [[Unit Speed Curve Reparameterization]] is not always possible.

Curve $\beta$ can be approximated with the Frenet Frame Field by using the [[Taylor Series]].[^2] The result is called the [[Frenet Approximation of Curve]]. The approximation is different near each [[Point]] on the curve.

> [!abstract] Theorem 3 (Full Frenet Apparatus)
> For a Frenet Frame Field, the formulas are
> - $T = \frac{\alpha'}{||\alpha'||}$
> - $N = B \times T$
> - $B = \frac{\alpha' \times \alpha''}{||\alpha' \times \alpha''||}$
> - $\kappa = \frac{||\alpha' \times \alpha''||}{||\alpha'||^3}$
> - $\tau = \frac{(\alpha' \times \alpha'') \cdot \alpha'''}{||\alpha' \times \alpha''||^2}$

# Components
- [[Unit Tangent Vector Field on Curve]]
- [[Principal Normal Vector Field on Curve]]
- [[Binormal Vector Field on Curve]]
- [[Curvature Function on Curve]]
- [[Torsion Function on Curve]]

# Properties
- [[Frenet Formula]]

#TODO 
is s(t) an arc length function or the reparameterization?

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=74)
[^2]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=78)