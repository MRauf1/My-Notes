---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Lebesgue Integral[^1]
> Given a set $\Gamma$ (the domain of integration) and a [[Measure (Measure Theory)|measure]] $\mu$, the Lebesgue integral of $f$ over $\Gamma$ with respect to $\mu$ is
> $$
> \begin{align}
> I = \int_\Gamma f(x)\, d\mu(x)
> \end{align}
> $$

This definition requires no coordinates, no fixed dimension, and no smoothness of $\Gamma$ or $f$ — only a set $\Gamma$ and a measure $\mu$ on it. One-dimensional [[Riemann Integral|Riemann integrals]] are Lebesgue integrals with respect to the [[Borel Measure|Borel measure]] $\mu_B$; nested Riemann integrals are Lebesgue integrals with respect to the [[Lebesgue Measure|Lebesgue measure]] $\lambda$. Nothing about ordinary calculus is invalidated by this more general definition — it is only generalized.

# Properties
- Expectation is a Lebesgue integral against a [[Probability Space|probability measure]]: $\mathbb{E}[f(X)] = \int_\Omega f(x)\,dP(x)$.
- Underpins the [[Monte Carlo Estimator]], which estimates a Lebesgue integral $I = \int_\Omega f\,d\mu$ by sampling.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
