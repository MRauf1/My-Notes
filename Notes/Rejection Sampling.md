---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Rejection Sampling[^1]
> Used when the CDF $F$ cannot be inverted, or the density $p$ cannot even be normalized. Take an envelope density $\tilde{p}$ with $p(x) \leq M\tilde{p}(x)$, and repeat:
> 1. Draw $x \sim \tilde{p}$, then $y \sim \mathcal{U}[0, M\tilde{p}(x))$.
> 2. If $y \leq p(x)$, return $x$; otherwise, go to 1.
>
> Accepted pairs $(x,y)$ are uniform under the graph of $p$, so their $x$-marginal is $p$, and the acceptance rate is $1/M$.

# Properties
- Pro: needs only pointwise evaluations of $p$, and only up to a normalizing constant.
- Con: wastes samples, and $M$ grows brutally with dimension; use it only when [[Inverse Transform Sampling]] is unavailable.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
