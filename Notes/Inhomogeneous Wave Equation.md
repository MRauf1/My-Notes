---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Inhomogeneous Wave Equation[^1]
> The [[Wave Equation]] driven by an externally applied force $f$:
> $$
> \begin{align}
> u_{tt} - c^2 \Delta u = f(\mathbf{x}, t).
> \end{align}
> $$
>
> **Theorem (whole line).** The unique solution of $u_{tt} - c^2 u_{xx} = f(x, t)$ on $-\infty < x < \infty$ with $u(x, 0) = \phi(x)$, $u_t(x, 0) = \psi(x)$ is[^2][^3]
> $$
> \begin{align}
> u(x, t) = \frac{1}{2}\left[\phi(x + ct) + \phi(x - ct)\right] + \frac{1}{2c}\int_{x - ct}^{x + ct} \psi(y)\, dy + \frac{1}{2c}\iint_{\Delta} f(y, s)\, dy\, ds,
> \end{align}
> $$
> where $\Delta = \{(y, s) : 0 \le s \le t,\ |y - x| \le c(t - s)\}$ is the characteristic triangle with apex $(x, t)$ and base $[x - ct, x + ct]$, so $\iint_\Delta f = \int_0^t \int_{x - c(t - s)}^{x + c(t - s)} f(y, s)\, dy\, ds$.

For a string, $f$ is an external force acting on an infinitely long vibrating string.[^3] The first two terms are [[D'Alembert's Formula]]; the third is [[Duhamel's Principle]] with the source operator $s(t)\psi = \frac{1}{2c}\int_{x - ct}^{x + ct}\psi$: the impulse $f(\cdot, s)\,ds$ acts as an initial velocity at time $s$ and spreads for time $t - s$, filling the triangle.[^4]

# Properties
- An [[Inhomogeneous Linear Partial Differential Equation]]: its solutions are any particular solution plus solutions of the homogeneous [[Wave Equation]].
- [[Hyperbolic Partial Differential Equation|Hyperbolic]].
- The force influences $u(x, t)$ only through its values in the characteristic triangle, the [[Domain of Dependence]] of $(x, t)$.
- On the half-line with boundary data $u(0, t) = h(t)$, the triangle is cut off by the wall and a retarded term $h(t - x/c)$ appears ([[Wave Equation on the Half-Line]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=25&annotation=BCC9SXSP)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=83&annotation=Y3NDAPYC); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=83&annotation=SDQHTZFH)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=83&annotation=7YIIRDRA)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=89&annotation=5LU5VSIW); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=90&annotation=PLKGDLVJ)
