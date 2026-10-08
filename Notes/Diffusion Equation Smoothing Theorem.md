---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Diffusion Equation Smoothing Theorem[^1][^2][^3]
> The solution of the [[Diffusion Equation]] on the line is the [[Convolution]] of $\phi$ with the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]] $S(z, t) = \frac{1}{\sqrt{4\pi k t}} e^{-z^2/4kt}$; with $p = z/\sqrt{kt}$,
> $$
> \begin{align}
> u(x, t) = \int_{-\infty}^{\infty} S(x - y, t)\, \phi(y)\, dy = \int_{-\infty}^{\infty} S(z, t)\, \phi(x - z)\, dz = \frac{1}{\sqrt{4\pi}} \int_{-\infty}^{\infty} e^{-p^2/4}\, \phi(x - p\sqrt{kt})\, dp.
> \end{align}
> $$
> **Theorem 1.** If $\phi$ is bounded and continuous on $\mathbb{R}$, then $u$ is $C^\infty$ on $\mathbb{R} \times (0, \infty)$, satisfies $u_t = k u_{xx}$, and $\lim_{t \searrow 0} u(x, t) = \phi(x)$ for each $x$.
>
> **Theorem 2.** If $\phi$ is bounded and [[Piecewise Continuous Function|piecewise continuous]], then $u$ is a $C^\infty$ solution for $t > 0$ and
> $$
> \begin{align}
> \lim_{t \searrow 0} u(x, t) = \frac{1}{2}\left[\phi(x^+) + \phi(x^-)\right] \quad \text{for all } x,
> \end{align}
> $$
> which equals $\phi(x)$ at every point of continuity.

**Corollary (instant smoothing).** The solution has derivatives of all orders for $t > 0$ even if $\phi$ is not differentiable: all solutions become smooth as soon as diffusion takes effect. There are no singularities, in sharp contrast to the [[Wave Equation]] ([[Wave and Diffusion Equation Comparison]]).[^4]

**Why.** Every derivative $\partial_x^m \partial_t^n$ can be moved onto the smooth Gaussian kernel, and the rapid decay $e^{-p^2/4}$ makes the differentiated integrals converge uniformly, regardless of the regularity of $\phi$. The $t \to 0$ limit is the kernel concentrating to a [[Dirac Delta Function|delta]]: in the $p$-form, $\phi(x - p\sqrt{kt}) \to \phi(x)$ pointwise under a weight of total mass $1$. Continuity of $\phi$ is used only in this last step;[^5] at a [[Jump Discontinuity]] the Gaussian is even, so half of its mass sees $\phi(x^-)$ and half sees $\phi(x^+)$, giving the average.

# Properties
- The averaging-at-jumps limit is the same as for Fourier series at a jump (and, in image processing, Gaussian blur turns a step edge into an [[Error Function]] profile passing through the midpoint).
- The step-data solution $Q(x, t) = \frac12 + \frac12\operatorname{erf}(x/\sqrt{4kt})$ is the prototype: $Q(0, t) = \frac12$ for all $t > 0$.
- Instant smoothing is the forward face of backward ill-posedness ([[Diffusion Equation Well-Posedness]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=92&annotation=SAWNHCR9)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=93&annotation=UFLGIQGR)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=95&annotation=87XH4V57)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=94&annotation=UN9QSJWX)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=94&annotation=INGF8PNE)
