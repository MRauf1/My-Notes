---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Laplace Distribution[^1]
> A [[Continuous Random Variable]] $X$ has the standard Laplace (double exponential) distribution if its pdf is
> $$
> \begin{align}
> f(x) = \frac{1}{2} e^{-|x|}, \quad -\infty < x < \infty
> \end{align}
> $$
> More generally, with location $\mu$ and scale $b > 0$,
> $$
> \begin{align}
> f(x) = \frac{1}{2b} e^{-|x - \mu|/b}, \quad -\infty < x < \infty
> \end{align}
> $$

# Properties
- Two back-to-back copies of the [[Exponential Distribution]]: $|X - \mu|/b$ is standard exponential. If $X_1, X_2$ are independent standard exponential, $X_1 - X_2$ is standard Laplace (derivable by [[Random Vector Transformation]]).[^2]
- [[Moment Generating Function|mgf]]: $M(t) = e^{\mu t}/(1 - b^2 t^2)$ for $|t| < 1/b$; in the standard case $M(t) = (1 - t^2)^{-1}$ for $|t| < 1$.
- $E(X) = \mu$ (also the [[Median]] and [[Mode]]) and $\text{Var}(X) = 2b^2$.
- [[Kurtosis]] $6$ (excess $3$): heavier tails than the [[Normal Distribution]].
- The maximum likelihood estimator of $\mu$ is the sample median, and a Laplace likelihood corresponds to an $L^1$ (absolute error) loss, just as a normal likelihood corresponds to squared error; a Laplace prior gives the lasso penalty.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=93)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=122)
