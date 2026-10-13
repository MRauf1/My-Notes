---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Jump Discontinuity[^1]
> A function $\phi$ has a jump at $x_0$ if both [[One-Sided Limit of Function|one-sided limits]]
> $$
> \begin{align}
> \phi(x_0^+) = \lim_{x \to x_0^+} \phi(x), \qquad \phi(x_0^-) = \lim_{x \to x_0^-} \phi(x)
> \end{align}
> $$
> exist but $\phi(x_0^+) \neq \phi(x_0^-)$. The jump is $\phi(x_0^+) - \phi(x_0^-)$.

# Properties
- The only kind of discontinuity allowed for a [[Piecewise Continuous Function]] (finitely many in each finite interval).
- Distinct from a removable discontinuity (equal one-sided limits differing from $\phi(x_0)$) and from essential discontinuities (a one-sided limit fails to exist).
- Smoothed instantly by the [[Diffusion Equation]], which converges to the midpoint $\frac12[\phi(x_0^+) + \phi(x_0^-)]$ as $t \to 0$ ([[Diffusion Equation Smoothing Theorem]]); transported unchanged by the [[Wave Equation]] along characteristics.
- The value of $f(x_0)$ is irrelevant; $f$ need not even be defined there.[^2]
- A Fourier series converges to the midpoint $\frac12[f(x_0^+) + f(x_0^-)]$ at a jump ([[Fourier Series Pointwise Convergence Theorem]]), with a persistent overshoot of about $9\%$ of the jump nearby ([[Gibbs Phenomenon]]).
- Special case of [[Simple Discontinuity]] (discontinuity of the first kind); see [[Discontinuity]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=94&annotation=5ZJF86GY)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=140&annotation=V7FA2XSL)
