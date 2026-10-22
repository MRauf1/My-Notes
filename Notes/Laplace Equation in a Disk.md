---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation in a Disk[^1][^2]
> The Dirichlet problem
> $$
> \begin{align}
> u_{xx} + u_{yy} = 0 \ \text{ for } x^2 + y^2 < a^2, \qquad u = h(\theta) \ \text{ for } x^2 + y^2 = a^2
> \end{align}
> $$
> has the solution
> $$
> \begin{align}
> u(r, \theta) &= \tfrac{1}{2}A_0 + \sum_{n=1}^\infty r^n\big(A_n\cos n\theta + B_n \sin n\theta\big), \\
> A_n &= \frac{1}{\pi a^n}\int_0^{2\pi} h(\phi)\cos n\phi\, d\phi, \qquad B_n = \frac{1}{\pi a^n}\int_0^{2\pi} h(\phi)\sin n\phi\, d\phi .
> \end{align}
> $$

**Derivation.**[^2][^3][^4] [[Separation of Variables]] $u = R(r)\Theta(\theta)$ in the [[Laplacian in Polar Coordinates]] gives $\Theta'' + \lambda\Theta = 0$ and $r^2R'' + rR' - \lambda R = 0$.
- $\Theta$ satisfies [[Periodic Boundary Condition|periodic conditions]] $\Theta(\theta + 2\pi) = \Theta(\theta)$, so $\lambda = n^2$ and $\Theta = A\cos n\theta + B\sin n\theta$ ($n \ge 1$), or $\Theta = A$ ($n = 0$).
- The $R$-equation is of Euler type: $R = r^\alpha$ gives $\alpha(\alpha-1) + \alpha - n^2 = 0$, so $\alpha = \pm n$ and $R = Cr^n + Dr^{-n}$; for $n = 0$ the second solution is $\log r$. Separated solutions: $(Cr^n + Dr^{-n})(A\cos n\theta + B\sin n\theta)$ and $C + D\log r$.
- The "boundary condition" at $r = 0$ is finiteness: reject $r^{-n}$ and $\log r$.
- Impose $u(a, \theta) = h(\theta)$: this is the full [[Fourier Series]] of $h$, which fixes $a^n A_n, a^n B_n$.

# Properties
- The series sums in closed form to [[Poisson's Formula]].[^5]
- The circle is a natural shape for harmonic functions because of the [[Laplacian Operator Rigid Motion Invariance|rotational invariance]] of $\Delta$.[^1]
- Each $r^n\cos n\theta = \operatorname{Re} z^n$ and $r^n\sin n\theta = \operatorname{Im} z^n$ is harmonic, so the solution is the real part of a power series in $z = x + iy$ ([[Harmonic Conjugate Function]]).[^6]
- Variants: [[Laplace Equation in a Wedge]], [[Laplace Equation in an Annulus]], [[Laplace Equation in the Exterior of a Circle]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=177&annotation=99BKNZMH); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=177&annotation=86S47TVM)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=179&annotation=LDV736EZ); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=179&annotation=9CCGZLNG)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=178&annotation=M9J6B24E); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=178&annotation=746GXRHS)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=178&annotation=YPQUXGCA)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=179&annotation=JA7GJRKZ)
[^6]: Added from general knowledge.
