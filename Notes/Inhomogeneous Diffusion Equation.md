---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Inhomogeneous Diffusion Equation[^1][^2]
> The [[Diffusion Equation]] with a source (or sink) $f$, on the whole line:
> $$
> \begin{align}
> u_t - k u_{xx} = f(x, t) \ (-\infty < x < \infty,\ 0 < t < \infty), \qquad u(x, 0) = \phi(x).
> \end{align}
> $$
> Its solution is
> $$
> \begin{align}
> u(x, t) = \int_{-\infty}^{\infty} S(x - y, t)\, \phi(y)\, dy + \int_0^t \int_{-\infty}^{\infty} S(x - y, t - s)\, f(y, s)\, dy\, ds,
> \end{align}
> $$
> where $S$ is the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]]. In operator form, $u(t) = s(t)\phi + \int_0^t s(t - s) f(s)\, ds$ with the source operator $(s(t)\phi)(x) = \int S(x - y, t)\phi(y)\, dy$.

For a rod, $\phi$ is the initial temperature distribution and $f$ is heat supplied (or removed) at later times. The first term is the homogeneous solution; the second is [[Duhamel's Principle]]: heat injected at $(y, s)$ spreads as a Gaussian for the remaining time $t - s$.

# Properties
- An [[Inhomogeneous Linear Partial Differential Equation]]: particular solution (the Duhamel term, which has zero initial data) plus homogeneous solution.
- On the half-line, reflect both $\phi$ and $f$ ([[Method of Reflection]], [[Diffusion Equation on the Half-Line]]).
- A boundary source $v(0, t) = h(t)$ is converted to an extra interior source $-h'(t)$ by the [[Boundary Condition Subtraction Device]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=79&annotation=NREHNHGN)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=80&annotation=SRF943HC)
