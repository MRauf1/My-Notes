---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Binomial [[Probability Distribution]])[^1]
> Denoted as $Binomial(n, p)$
> $$
> \begin{align}
> P(x) &= {n \choose x} p^x (1 - p)^{n - x}, x \in \{0, 1, 2, \dots, n\}
> \end{align}
> $$

Distribution for $x$ successes in $n$ binary observations (e.g. success or failure). In other words, distribution for $n$ (summed) [[i.i.d.]] [[Bernoulli Distribution|Bernoulli trials]].

This is a [[Multinomial Distribution]] with $c = 2$.

Derivation:[^2] an outcome of $n$ [[Bernoulli Distribution|Bernoulli trials]] is an $n$-tuple of zeros and ones. There are $\binom{n}{x}$ ways to place $x$ successes ([[Combination]]), each with probability $p^x(1-p)^{n-x}$ by independence, and these are mutually exclusive events, so their probabilities add. Hogg et al. write $b(n, p)$.

# Properties
## Basic Statistical Properties
- [[Binomial Distribution Expectation]]
- [[Binomial Distribution Variance]]
- [[Moment Generating Function|mgf]]:[^3] $M(t) = \sum_x \binom{n}{x}(pe^t)^x(1-p)^{n-x} = [(1 - p) + pe^t]^n$ for all $t$ (by the [[Binomial Theorem]]), giving $\mu = np$ and $\sigma^2 = np(1-p)$.

## Operation
- [[Binomial Distribution Addition]]

## [[Probability Distribution Skewness]]
- [[Binomial Distribution Skewness]]

## [[Approximation]]
- [[Binomial Distribution Normal Approximation]]
- [[Binomial Distribution Poisson Approximation]]

## [[Parameter Estimation]]
### [[Maximum Likelihood Estimation]]
- [[Binomial Distribution Maximum Likelihood Estimation]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=23)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=172)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=173)
