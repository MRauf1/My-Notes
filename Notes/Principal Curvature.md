---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Principal Curvatures and Principal Directions[^1]
> At a point of a [[Smooth Surface]], the unit directions $X_1, X_2$ along which the [[Normal Curvature]] $\kappa_n$ attains its maximum and minimum are the *principal directions*; the corresponding extreme values $\kappa_1, \kappa_2$ are the *principal curvatures*.

![[Principal Curvatures.png]]

> [!abstract] Eigen-Characterization[^2]
> The principal directions and curvatures are the [[Eigenvector|eigenvectors]] and [[Eigenvalue|eigenvalues]] of the [[Shape Operator]]:
> $$\begin{align}
> S X_i = \kappa_i X_i,
> \end{align}$$
> and the principal directions are orthogonal with respect to the [[Induced Metric]]: $g(X_1, X_2) = df(X_1)\cdot df(X_2) = 0$.

This follows because $S$ is [[Self-Adjoint Linear Map|self-adjoint]] with respect to $g$, and $\kappa_n$ is its Rayleigh quotient. In coordinates, $\kappa_i$ are the eigenvalues of $\mathrm{I}^{-1}\mathrm{II}$.

The principal curvatures completely characterize the curvature of a surface at a point; any other tangent vector is a combination of $X_1, X_2$ ([[Euler's Curvature Formula]]).[^3] They are, however, inconvenient to work with directly, especially in the discrete setting, so their symmetric functions are used instead.[^4]

# Types
- [[Mean Curvature]] $H = \frac{\kappa_1 + \kappa_2}{2}$
- [[Gaussian Curvature]] $K = \kappa_1 \kappa_2$
- When $\kappa_1 = \kappa_2$ the principal directions are undefined: [[Umbilic Point]].

# Properties
- [[Euler's Curvature Formula]]: $\kappa_n(\theta) = \kappa_1\cos^2\theta + \kappa_2\sin^2\theta$.

[^1]: [Crane, p. 39](zotero://open-pdf/library/items/9N6JDPI2?page=40&annotation=URRUXBXN)
[^2]: [Crane, p. 39](zotero://open-pdf/library/items/9N6JDPI2?page=40&annotation=UVT6NLHB)
[^3]: [Crane, p. 41](zotero://open-pdf/library/items/9N6JDPI2?page=42&annotation=JMI9Q9XC)
[^4]: [Crane, p. 40](zotero://open-pdf/library/items/9N6JDPI2?page=41&annotation=B9YBIDRZ)
