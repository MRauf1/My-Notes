---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Optimal Importance Sampling Distribution[^1]
> Since $\mathrm{Var}[\langle I \rangle] = \int f^2/p\,d\mu - I^2$, choosing $p$ to track $f$ shrinks the [[Monte Carlo Estimator Variance|variance]]. For nonnegative $f$, the optimal choice is
> $$
> \begin{align}
> p^\star(x) = \frac{f(x)}{\int_\Omega f\,d\mu} = \frac{f(x)}{I} \implies \frac{f(X)}{p^\star(X)} \equiv I, \quad \text{zero variance}
> \end{align}
> $$

Computing $p^\star$ requires knowing $I$ — the very quantity being estimated. The practical reading: sample from whichever factor of $f$ can be inverted, and accept the rest as residual variance.

For a signed integrand, no choice of $p$ achieves zero variance — the best available is $p \propto |f|$.

# Properties
- Only attainable in the nonnegative-$f$ case; a signed integrand can only be tracked in magnitude.
- Practically approximated rather than computed exactly, since it depends on the unknown $I$.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
