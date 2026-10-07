---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!abstract] Strong Law of Large Numbers[^1]
> For i.i.d. random variables $X_n$ with $\mathbb{E}|X| < \infty$, the sample mean converges almost surely to $\mathbb{E}[X]$.

In Hogg et al.,[^2] the strong law weakens the hypotheses of the [[Weak Law of Large Numbers]] to independent $X_i$ with a finite mean: it is a first-moment theorem, while the weak law (as proved there) needs a second moment. Almost sure convergence, $P(\lim_n \bar{X}_n = \mu) = 1$, is stronger than [[Convergence in Probability]]: it controls a whole sequence of averages along one run of the experiment, not just each $\bar{X}_n$ separately.

# Properties
- Requires only a finite mean $\mathbb{E}|X| < \infty$ — not a finite variance. Consequently, the consistency of a [[Monte Carlo Estimator]] survives infinite variance.
- What does *not* survive infinite variance: the Central Limit Theorem, error bars, and any claim about $O(1/\sqrt{N})$ convergence — all of these additionally require finite variance.
- Guarantees $\langle I \rangle_N \to I$ almost surely as $N \to \infty$ for the [[Monte Carlo Estimator]].
- Guarantees the consistency of every [[Monte Carlo Method]].
- Justifies [[Simple Monte Carlo]] provided $\mu$ exists, but says nothing about how large $n$ must be; if $\mu = \infty$, $\hat{\mu}_n \to \infty$ a.s. without ever equaling $\infty$ ([[Infinite Moments in Monte Carlo]]).[^3]

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=338)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=16&annotation=SEHKY7UX); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=32&annotation=N2P9ZCZ9)
