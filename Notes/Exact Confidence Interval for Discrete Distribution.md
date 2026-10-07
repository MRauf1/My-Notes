---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Exact Confidence Interval for a Discrete Distribution[^1]
> Let $X_1, \dots, X_n$ be a [[Random Sample]] from a discrete pmf $p(x; \theta)$, $\theta \in \Omega$ an interval, and let $T$ be an [[Estimator]] of $\theta$ with cdf $F_T(t; \theta)$ that is nonincreasing and continuous in $\theta$ for every $t$ in the support of $T$. Let $\alpha_1, \alpha_2 > 0$ with $\alpha = \alpha_1 + \alpha_2 < 0.5$, let $t$ be the realized value of $T$, and let $\underline{\theta}$ and $\overline{\theta}$ solve
> $$
> \begin{align}
> F_T(t^-; \underline{\theta}) = 1 - \alpha_2, \qquad F_T(t; \overline{\theta}) = \alpha_1
> \end{align}
> $$
> where $t^-$ is the support value of $T$ immediately below $t$. Then $(\underline{\theta}, \overline{\theta})$ is a [[Confidence Interval]] for $\theta$ with confidence coefficient at least $1 - \alpha$.

Interpretation: $\overline{\theta}$ is the largest parameter value under which observing $T \leq t$ still has probability at least $\alpha_1$, and $\underline{\theta}$ the smallest under which observing $T \geq t$ still has probability at least $\alpha_2$. The interval collects all $\theta$ not rejected by the two one-sided tests at levels $\alpha_1$ and $\alpha_2$ (test inversion).

# Properties
- Because $T$ is discrete, an exact coverage of $1 - \alpha$ is generally unattainable; the interval is conservative (coverage $\geq 1 - \alpha$).
- Needs no large-sample approximation; for binomial data it is the Clopper-Pearson interval.
- Binomial form used in [[Monte Carlo Estimation of a Probability]]:[^2] with $T = t$ successes, the $99\%$ limits solve $0.005 = \sum_{i=t}^n \binom{n}{i} p_L^i(1-p_L)^{n-i}$ and $0.005 = \sum_{i=0}^t \binom{n}{i} p_U^i(1-p_U)^{n-i}$, found by bisection; for $t = 0$ the upper limit is approximately the [[Rule of Three (Statistics)|rule of three]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=265)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=24&annotation=B2SRGL96)
