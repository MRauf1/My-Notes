---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Estimation of a Probability[^1]
> With the indicator $f(x) = 1_{x \in A} = 1_A(x)$ and $X \sim p$, $E(f(X)) = P(X \in A)$. The [[Simple Monte Carlo]] average of the binary $Y_i = 1_A(X_i)$ is written $\hat{p}_n$. Since $Y^2 = Y$,
> $$
> \begin{align}
> \sigma^2 = E(Y^2) - E(Y)^2 = p(1 - p)
> \end{align}
> $$
> so the variance is determined by the mean, and the CLT-based $99\%$ interval is
> $$
> \begin{align}
> \hat{p}_n \pm 2.58\sqrt{\frac{\hat{p}_n(1 - \hat{p}_n)}{n}}
> \end{align}
> $$

**Exact interval.**[^2] The number of successes $T = n\hat{p}$ is [[Binomial Distribution|Binomial]]$(n, p)$, so an exact $99\%$ interval $p_L \leq p \leq p_U$ (Clopper–Pearson; [[Exact Confidence Interval for Discrete Distribution]]) solves, for observed $T = t$,
$$
\begin{align}
0.005 &= \sum_{i=t}^n \binom{n}{i} p_L^i (1 - p_L)^{n-i} \\
0.005 &= \sum_{i=0}^t \binom{n}{i} p_U^i (1 - p_U)^{n-i}
\end{align}
$$
with $p_L = 0$ when $T = 0$ and $p_U = 1$ when $T = n$. The right-hand sides are binomial tail probabilities available in standard libraries; $p_L, p_U$ are then found by bisection or another root search.

# Properties
- **Zero successes:**[^3] if $\hat{p}_n = 0$ the CLT interval collapses to $[0, 0]$, which is not a credible upper limit. Use instead the [[Rule of Three (Statistics)|rule of three]]: $[0, 3/n]$ at $95\%$ and $[0, 4.605/n]$ at $99\%$.
- The CLT interval is the Wald interval for a [[Bernoulli Distribution|Bernoulli]] mean ([[Binomial Distribution Maximum Likelihood Estimation Wald Test Confidence Interval]]).
- A rare-event probability (tiny $p$) has relative error $\sqrt{(1-p)/(np)}$, which motivates [[Optimal Importance Sampling Distribution|importance sampling]].

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=22&annotation=AIIAPEA9); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=22&annotation=V64EZ37Q); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=23&annotation=7RVSSACK)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=24&annotation=B2SRGL96)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=23&annotation=ZZFPM53T)
