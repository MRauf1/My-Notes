---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplacian in Spherical Coordinates[^1][^2]
> In [[Spherical Coordinate System|spherical coordinates]] $(r, \theta, \phi)$ with
> $$
> \begin{align}
> r = \sqrt{x^2+y^2+z^2}, \quad s = \sqrt{x^2+y^2} = r\sin\theta, \quad z = r\cos\theta, \quad x = s\cos\phi, \quad y = s\sin\phi
> \end{align}
> $$
> ($\theta$ the polar angle from the $z$-axis, $\phi$ the azimuth), the three-dimensional [[Laplacian Operator]] is
> $$
> \begin{align}
> \Delta_3 u &= u_{rr} + \frac{2}{r}u_r + \frac{1}{r^2}\left[u_{\theta\theta} + (\cot\theta)\, u_\theta + \frac{1}{\sin^2\theta}u_{\phi\phi}\right], \\
> \Delta_3 &= \frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r} + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\phi^2}.
> \end{align}
> $$

Some calculus books swap the roles of $\theta$ and $\phi$.[^1] The computation is organized as two successive 2D polar changes, $(z, s) \to (r, \theta)$ and $(x, y) \to (s, \phi)$, each using the [[Laplacian in Polar Coordinates]].[^1]

**General case.**[^3] In $\mathbb{R}^n$, $\Delta = \partial_r^2 + \frac{n-1}{r}\partial_r + \frac{1}{r^2}\Delta_{S^{n-1}}$, where $\Delta_{S^{n-1}}$ (the Laplace–Beltrami operator of the unit sphere) acts only on the angular variables; the bracket above is $\Delta_{S^2}$.

# Properties
- Radial part $u_{rr} + \frac{2}{r}u_r = \frac{1}{r^2}(r^2 u_r)_r$; for $\theta,\phi$-independent $u$, $\Delta u = 0$ gives $u = -c_1/r + c_2$ ([[Radial Harmonic Function]]).
- Simple form reflects the [[Laplacian Operator Rigid Motion Invariance|rotational invariance]] of $\Delta_3$.
- Derived from [[Cartesian and Spherical Coordinate System Change]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=170&annotation=6HH3DN4R)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=171&annotation=28Y9B6LF)
[^3]: Added from general knowledge.
