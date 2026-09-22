---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Estimator Variance[^1]
> For the [[Monte Carlo Estimator]] $\langle I \rangle = f(X)/p(X)$ with $X \sim p$,
> $$
> \begin{align}
> \mathrm{Var}[\langle I \rangle] = \int_\Omega \frac{f^2(x)}{p(x)}\,d\mu(x) - I^2
> \end{align}
> $$

If $f/p$ is unbounded — e.g. $p$ has Gaussian tails while $f$ decays only polynomially — this integral diverges, and the empirical convergence plot becomes quiet stretches punctuated by a single sample that resets the running average.

# Properties
- Minimized over choices of $p$ by the [[Optimal Importance Sampling Distribution]].
- Reduced without changing $p$ by [[Stratified Sampling|stratification]] or [[Control Variates]].
- Finiteness of this variance is not implied by the [[Strong Law of Large Numbers|consistency]] of $\langle I \rangle_N$, and is required for a Central Limit Theorem / $O(1/\sqrt{N})$ error-bar claim to hold.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
