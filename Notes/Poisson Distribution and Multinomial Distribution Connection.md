---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Poisson Distribution]] and [[Multinomial Distribution]] Connection)[^1]
> Consider a sum of [[Independent Random Variable|independent]] [[Poisson Distribution|Poisson RVs]] $X_i$ with parameters $\mu_i$. Then $X = \sum_{i} X_i$ has a [[Poisson Distribution]] with parameter $\mu = \sum_{i} \mu_i$.
> If $X = n$ and $n$ is fixed, then [[Random Variable]] $X_i|n$ are no longer [[Independent Random Variable]] and do not have a Poisson distribution.
> $$
> \begin{align}
> P(X_1 = n_1, \dots, X_c = n_c | \sum_{i} X_i = n) &= \frac{n!}{\prod_{i} n_i!} \prod_{i} p_i^{n_i} \\
> \text{with}\ p_i &= \frac{\mu_i}{\sum_{i} \mu_i}
> \end{align}
> $$
> Which is a [[Multinomial Distribution]] ($n, \{p_i\}$).

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=26)