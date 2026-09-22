---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Control Variates[^1]
> Take $g$ with a known integral $G = \int_\Omega g\,d\mu$, and estimate
> $$
> \begin{align}
> \langle I \rangle_{\mathrm{CV}} = \alpha G + \frac{f(X) - \alpha g(X)}{p(X)}
> \end{align}
> $$
> This is unbiased for every $\alpha$, since the correction term subtracts a quantity whose expectation is exactly $\alpha G$. The optimal choice is $\alpha^\star = \mathrm{Cov}(F,G)/\mathrm{Var}(G)$, giving
> $$
> \begin{align}
> \mathrm{Var}[\langle I \rangle_{\mathrm{CV}}] = (1-\rho^2)\,\mathrm{Var}[\langle I \rangle]
> \end{align}
> $$
> where $\rho$ is the [[Correlation]] between $F$ and $G$.

Everything depends on $\rho$: an uncorrelated control variate does nothing, and a badly scaled one can make the estimator worse.

# Properties
- Unbiased for any $\alpha$, unlike most variance-reduction techniques, which must be applied carefully to avoid introducing bias.
- Improves [[Monte Carlo Estimator Efficiency|efficiency]] precisely when a control variate correlated with $f$ and cheap to integrate exactly is available.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
