---
tags:
  - statistics
  - bayesian_statistics
---

# Definition

> [!info] Definition 1 ([[Exponentiation|Exponential]] [[Probability Distribution]])
> Exponential distribution, with [[Function Support]] $[0, \infty)$, denoted as $Exponential(\lambda)$ is
> $$
> \begin{align}
> f(x) = \begin{cases}\lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0\end{cases}
> \end{align}
> $$
> Alternatively, one can use $\theta = 1/\lambda$ as the parameter.

If $X \sim Exponential(\lambda)$, then $X \sim Gamma(\alpha = 1, \lambda = \lambda)$. Thus, the exponential distribution is a special case of the [[Gamma Distribution]]: in Hogg et al.'s scale form, $f(x) = \frac{1}{\beta}e^{-x/\beta}$ is $\Gamma(1, \beta)$, the exponential with rate $1/\beta$.[^1]

It is the waiting time until the first event of a [[Poisson Process]] with rate $\lambda$, and the interarrival times of the process are iid exponential with mean $1/\lambda$; a sum of $k$ of them is $\Gamma(k, 1/\lambda)$ ([[Gamma Distribution Addition]]).[^2]

# Properties
## Basic Statistical Properties
- [[Exponential Distribution Expectation]]
- [[Exponential Distribution Variance]]

## Other
- Memoryless: $P(X > s + t \mid X > s) = P(X > t)$; it is the only continuous memoryless distribution, the continuous counterpart of the [[Geometric Distribution]].
- The difference of two independent standard exponentials is [[Laplace Distribution|Laplace]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=192)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=194)
