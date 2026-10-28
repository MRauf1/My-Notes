---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Non-Uniform Random Variate Generation[^1]
> The task of converting $\mathcal{U}(0,1)$ random variables (from a [[Pseudorandom Number Generator]]) into random variables $X$ with a prescribed distribution $F$, as inputs to a [[Monte Carlo Method|Monte Carlo]] simulation.

[[Inverse Transform Sampling|Inversion]] of the CDF is the gold standard: it works in principle for every distribution and enables powerful variance reduction, but it is often hard to compute, which motivates the alternatives.[^1] Inversion maps one uniform to one variate; other transformations usually consume several uniforms and exploit special relationships among distributions, and when available they can be more elegant and faster.[^2]

# Types
- [[Inverse Transform Sampling]], including numerical inversion and the [[QQ Transformation]].
- Transformations:
	- Location-scale:[^3] if $X \sim F$ has mean $0$ and standard deviation $1$, then $Y = \mu + \sigma X$ ($\sigma > 0$) has mean $\mu$, standard deviation $\sigma$ and density $f_Y(y) = \frac{1}{\sigma} f_X\!\left(\frac{y - \mu}{\sigma}\right)$ ([[Location Parameter]], [[Scale Parameter]]).
	- Monotone transformations, via the change-of-variables formula ([[Cumulative Distribution Function Transformation Technique]]).
	- [[Box-Muller Transform]] for normal variates.
	- Maxima, minima and [[Order Statistic|order statistics]]: if $X_i \overset{\text{iid}}{\sim} F$, then $\max_{i \leq r} X_i$ has CDF $F^r$ and $\min_{i \leq r} X_i$ has CDF $1 - (1 - F)^r$.[^4]
	- Sums:[^5] when $Y = X_1 + \dots + X_n$ has a known relationship to iid $X_i$ (e.g. [[Gamma Distribution Addition]]), generate and sum the $X_i$, even if $Y$ did not arise as a sum; this slows down as $n$ grows.
	- [[One-Liner (Random Variate Generation)|One-liners]].
	- Discrete transformations: [[Array Sampling Method]], resampling from the [[Empirical Distribution Function]] ([[Bootstrap]]), and the [[Gumbel-Max Trick]].
- [[Rejection Sampling|Acceptance-rejection sampling]], with [[Squeeze Function (Rejection Sampling)|squeezes]], [[Adaptive Rejection Sampling]] and the [[Ziggurat Algorithm]].
- Mixtures:[^6] if $X \sim f(\cdot\,; \theta)$ with random parameter $\theta \sim G$, sample $\theta \sim G$ and then $X \sim f(\cdot\,; \theta)$ ([[Mixture Distribution]]).

**Random vectors.**[^7] The three generic methods all extend naturally to $\mathbf{X} \in \mathbb{R}^d$, but all tend to become unwieldy:
- Inversion becomes [[Sequential Inversion]], drawing each component from its conditional given the previous ones; it needs many tractable conditional CDFs.
- [[Rejection Sampling|Acceptance-rejection]] works verbatim with vectors, but the constant $c$ is hard to keep small as $d$ grows.
- Mixtures $F(\mathbf{x}) = \sum_{k=1}^K \pi_k F_k(\mathbf{x})$ (or $\int F(\mathbf{x} \mid \mathbf{y})g(\mathbf{y})\,d\mathbf{y}$) are sampled by drawing the label $Z$ with $P(Z = k) = \pi_k$ (or $\mathbf{Y} \sim g$), then $\mathbf{X} \sim F_Z$; this helps for special problems but is not easily adapted to automated generation.
- [[Copula-Marginal Sampling]] is a fourth generic method for $d > 1$, joining the dependence structure of one family to the marginals of another.

# Properties
- Multivariate generalizations include [[Multivariate Normal Sampling (Cholesky Factorization)]]; when independent sampling is impractical, [[Markov Chain Monte Carlo]] takes over.
- The extreme difficulty of some multidimensional sampling problems is a main motivation for [[Markov Chain Monte Carlo]] and [[Sequential Monte Carlo]].[^8]

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=3&annotation=BW43RZPD); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=FNDWBTRT)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=14&annotation=5WF45XR9)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=14&annotation=M67I74UJ)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=16&annotation=78G4TDRQ); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=16&annotation=Z2IZ5BJ9)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=17&annotation=7MQ3BRIM)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=29&annotation=HB3NXFQD); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=30&annotation=D54MNGRT)
[^7]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=4&annotation=TPFJR2F8); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=7&annotation=Z9WS2PJY); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=7&annotation=4YU6HNVE); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=3&annotation=BLY9P3UL)
[^8]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=3&annotation=NFN2QEW2)
