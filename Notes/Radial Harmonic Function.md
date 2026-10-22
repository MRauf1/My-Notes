---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Radial Harmonic Function[^1][^2][^3]
> The [[Harmonic Function|harmonic functions]] that are themselves rotation invariant, i.e. depend only on $r = |\mathbf{x}|$, are, away from the origin,
> $$
> \begin{align}
> n = 2&: \quad (r u_r)_r = 0 \ \Rightarrow\ u = c_1 \log r + c_2, \\
> n = 3&: \quad (r^2 u_r)_r = 0 \ \Rightarrow\ u = -\frac{c_1}{r} + c_2 .
> \end{align}
> $$
> In general, $(r^{n-1}u_r)_r = 0$ gives $u = c_1 r^{2-n} + c_2$ for $n \ge 3$.[^4]

$1/r = (x^2+y^2+z^2)^{-1/2}$ is the 3D analogue of $\log r = \log (x^2+y^2)^{1/2}$; neither is finite at the origin.[^3]

# Properties
- Obtained from the radial parts of the [[Laplacian in Polar Coordinates]] and [[Laplacian in Spherical Coordinates]]; the ODE comes from [[Laplacian Operator Rigid Motion Invariance|rotational invariance]].
- In electrostatics $u = r^{-1}$ is the [[Electric Potential]] of a unit charge at the origin.[^3]
- Normalized, they are the fundamental solutions of $-\Delta$: $\Phi = -\frac{1}{2\pi}\log|\mathbf{x}|$ ($n=2$) and $\Phi = \frac{1}{4\pi|\mathbf{x}|}$ ($n=3$), satisfying $-\Delta\Phi = \delta$ ([[Dirac Delta Function]]); the solution of the [[Poisson Equation]] $-\Delta u = f$ on $\mathbb{R}^n$ is $\Phi * f$.[^4]
- $\log r$ reappears as the $n = 0$ second radial solution when separating variables in polar coordinates ([[Laplace Equation in a Disk]], [[Laplace Equation in an Annulus]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=169&annotation=4Y4G9EHN); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=170&annotation=VT7NJJUD)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=171&annotation=28Y9B6LF)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=172&annotation=WA4WD8TR)
[^4]: Added from general knowledge.
