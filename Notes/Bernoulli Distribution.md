---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Bernoulli [[Probability Distribution]])[^1]
> Denoted as $Bernoulli(p)$
> $$
> \begin{align}
> P(x) &= \begin{cases}p & x = 1\\ 1 - p & x = 0\end{cases} = p^x(1 - p)^{1 - x}
> \end{align}
> $$

Distribution for a single binary observation (e.g. success or failure). This is a [[Binomial Distribution]] with $n = 1$.

> [!info] Definition 2 (Bernoulli Experiment and Bernoulli Trials)[^2]
> A Bernoulli experiment is a [[Random Experiment]] whose outcome falls in exactly one of two [[Mutually Exclusive Events|mutually exclusive]] and [[Exhaustive Events|exhaustive]] classes, success or failure. A sequence of Bernoulli trials is a sequence of independent performances of it with the same success probability $p$ on every trial. The Bernoulli random variable sets $X(\text{success}) = 1$ and $X(\text{failure}) = 0$.

# Properties
# Basic Statistical Properties
- [[Bernoulli Distribution Expectation]]
- [[Bernoulli Distribution Variance]]
- $\mu = p$, $\sigma^2 = p(1 - p)$, $\sigma = \sqrt{p(1 - p)}$, and mgf $M(t) = 1 - p + pe^t$.[^2]

# Related Distributions
- Counting successes in $n$ trials: [[Binomial Distribution]]; failures before the first or $r$th success: [[Geometric Distribution]], [[Negative Binomial Distribution]].

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=23)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=171)
