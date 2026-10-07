---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Rule of Three (Statistics)[^1]
> If $0$ successes are observed in $n$ independent Bernoulli$(p)$ trials, an approximate $95\%$ [[Confidence Interval|confidence interval]] for $p$ is $[0, 3/n]$, and an approximate $99\%$ interval is $[0, 4.605/n]$.

Derivation: the chance of no successes is $(1 - p)^n$. Keep the values of $p$ for which this is not below the level $\alpha$: $(1 - p)^n \geq \alpha \iff p \leq 1 - \alpha^{1/n}$. For large $n$, by a first-order Taylor expansion,
$$
\begin{align}
1 - \alpha^{1/n} = 1 - e^{\frac{1}{n}\log \alpha} \approx -\frac{\log \alpha}{n} = \frac{\log(1/\alpha)}{n}
\end{align}
$$
giving $\log(20)/n \approx 3/n$ for $\alpha = 0.05$ and $\log(100)/n \approx 4.605/n$ for $\alpha = 0.01$.

# Properties
- Fixes the degenerate $[0, 0]$ CLT interval in [[Monte Carlo Estimation of a Probability]] when no event is observed.
- It is (approximately) the one-sided Clopper–Pearson upper bound for $T = 0$ ([[Exact Confidence Interval for Discrete Distribution]]).

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=23&annotation=ZZFPM53T)
