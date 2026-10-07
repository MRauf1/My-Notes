---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Ratio Estimator[^1]
> To estimate $\theta = E(Y)/E(X)$, sample $n$ IID pairs $(X_i, Y_i)$ and take
> $$
> \begin{align}
> \hat{\theta} = \frac{\bar{Y}}{\bar{X}}, \qquad \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i, \quad \bar{Y} = \frac{1}{n}\sum_{i=1}^n Y_i
> \end{align}
> $$

Two complications compared with [[Simple Monte Carlo]]:[^2] $E(\hat{\theta}) \neq \theta$ in general (the estimator is biased, though the bias becomes unimportant for large $n$), and its variance must be estimated separately to form a confidence interval, usually by the [[Delta Method]].

# Properties
- [[Bias and Consistency of an Estimator|Biased but consistent]]: $\hat{\theta} \to \theta$ almost surely when $E(X) \neq 0$, since $\bar{X}$ and $\bar{Y}$ converge by the [[Strong Law of Large Numbers]] and the ratio is continuous there.
- Distinct from $E(Y/X)$, which may not even exist when $X$ has positive density at $0$ ([[Infinite Moments in Monte Carlo]]).
- Underlies [[Monte Carlo Estimation of a Conditional Expectation]] and self-normalized importance sampling.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=30&annotation=5PCNFNUL)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=30&annotation=7DKZ7C5X)
