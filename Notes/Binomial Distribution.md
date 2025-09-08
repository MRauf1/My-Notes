---
tags: statistics, categorical_variable_prediction
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

# Properties
## Basic Statistical Properties
- [[Binomial Distribution Expectation]]
- [[Binomial Distribution Variance]]

## [[Probability Distribution Skewness]]
- [[Binomial Distribution Skewness]]

## [[Approximation]]
- [[Binomial Distribution Normal Approximation]]
- [[Binomial Distribution Poisson Approximation]]

## [[Parameter Estimation]]
### [[Maximum Likelihood Estimation]]
- [[Binomial Distribution Maximum Likelihood Estimation]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=23)