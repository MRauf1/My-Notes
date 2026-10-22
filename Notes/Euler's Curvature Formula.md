---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!abstract] Euler's Curvature Formula[^1]
> Let $\kappa_1, \kappa_2$ be the [[Principal Curvature|principal curvatures]] at a point with principal directions $X_1, X_2$. If $Y$ is a unit tangent vector making angle $\theta$ with $X_1$, then its [[Normal Curvature]] is
> $$\begin{align}
> \kappa_n(Y) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta.
> \end{align}$$

It follows from writing $Y = \cos\theta\, X_1 + \sin\theta\, X_2$ (with $X_1, X_2$ orthonormal in the [[Induced Metric]]), using $SX_i = \kappa_iX_i$ and $\kappa_n(Y) = g(SY, Y)$.

# Properties
- Hence $\kappa_n$ ranges exactly over $[\kappa_2, \kappa_1]$, and the principal curvatures determine all normal curvatures at a point.
- Averaging over all directions gives the [[Mean Curvature]]: $\frac{1}{2\pi}\int_0^{2\pi} \kappa_n(\theta)\, d\theta = \frac{\kappa_1 + \kappa_2}{2} = H$.

[^1]: [Crane, p. 39–40](zotero://open-pdf/library/items/9N6JDPI2?page=41&annotation=B9YBIDRZ)
