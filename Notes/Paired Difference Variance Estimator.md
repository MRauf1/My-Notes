---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Paired Difference Variance Estimator[^1]
> For IID $y_1, \dots, y_n$ with $n$ even,
> $$
> \begin{align}
> \tilde{\sigma}^2 = \frac{1}{n}\sum_{i=1}^{n/2}\left(y_{2i} - y_{2i-1}\right)^2
> \end{align}
> $$
> is an unbiased estimate of $\sigma^2$, since $E\big((y_{2i} - y_{2i-1})^2\big) = 2\sigma^2$.

Each term is a difference of two raw observations, so no running mean is needed: the estimate avoids the cancellation problems of the naive [[Sample Variance]] formula and splits trivially across parallel workers.

# Properties
- As an estimate of $\sigma^2$ itself, $s^2$ is much better (it uses all $n - 1$ degrees of freedom, versus $n/2$).
- For a [[Monte Carlo Confidence Interval]] $\hat{\mu}_n \pm 2.58\,\tilde{\sigma}/\sqrt{n}$, $\tilde{\sigma}$ is almost as good as $s$ statistically, and can be much better numerically.
- A simple alternative to [[Welford's Algorithm]] for very large $n$.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=22&annotation=6JCEEQJN)
