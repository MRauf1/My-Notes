---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Mean Curvature[^1]
> The mean curvature $H$ of a surface at a point is the [[Arithmetic Mean]] of the [[Principal Curvature|principal curvatures]]:
> $$\begin{align}
> H = \frac{\kappa_1 + \kappa_2}{2}.
> \end{align}$$

Interpretation: mean curvature is like a logical "or": is there curvature along *at least one* direction? Care is needed since $H = 0$ also when $\kappa_1 = -\kappa_2$.[^2]

# Types
- $H \equiv 0$: [[Minimal Surface]].

# Properties
- $H = \frac{1}{2}\operatorname{tr} S$ ([[Shape Operator]]); coordinate-invariant since the trace is.
- Depends on the choice of normal: replacing $N$ by $-N$ negates $H$. With O'Neill's convention a sphere of radius $r$ with outward normal has $H = -1/r$.
- Equals the average of the [[Normal Curvature]] over all directions ([[Euler's Curvature Formula]]).
- Extrinsic: depends on how the surface sits in $\mathbb{R}^3$, not only on the [[Induced Metric]] (contrast [[Gaussian Curvature]]).
- Together with [[Gaussian Curvature]] it determines $\kappa_{1,2} = H \pm \sqrt{H^2 - K}$, and is often easier to compute, especially in the discrete setting.[^3]

[^1]: [Crane, p. 40](zotero://open-pdf/library/items/9N6JDPI2?page=41&annotation=484ZHDMR)
[^2]: [Crane, p. 40](zotero://open-pdf/library/items/9N6JDPI2?page=41&annotation=CIL7UXAJ)
[^3]: [Crane, p. 41](zotero://open-pdf/library/items/9N6JDPI2?page=42&annotation=JMI9Q9XC)
