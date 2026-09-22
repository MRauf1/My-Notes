---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!abstract] Strong Law of Large Numbers[^1]
> For i.i.d. random variables $X_n$ with $\mathbb{E}|X| < \infty$, the sample mean converges almost surely to $\mathbb{E}[X]$.

# Properties
- Requires only a finite mean $\mathbb{E}|X| < \infty$ — not a finite variance. Consequently, the consistency of a [[Monte Carlo Estimator]] survives infinite variance.
- What does *not* survive infinite variance: the Central Limit Theorem, error bars, and any claim about $O(1/\sqrt{N})$ convergence — all of these additionally require finite variance.
- Guarantees $\langle I \rangle_N \to I$ almost surely as $N \to \infty$ for the [[Monte Carlo Estimator]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
