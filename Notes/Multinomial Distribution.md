---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Multinomial [[Probability Distribution]])[^1]
> Denoted as $Multinomial(n, p_1, \dots, p_c)$
> $$
> \begin{align}
> P(n_1, \dots, n_c) &= \frac{n!}{n_1! \dots n_c!} p_1^{n_1} \dots p_c^{n_c}, \sum_{j} n_j = n
> \end{align}
> $$

Distribution for seeing $n_1$ successes of 1st category, $\dots$, $n_c$ successes of $c$th category in $n$ multi-variant observations (e.g. $c$ categories).

Since $n_c$ is [[Linearly Dependent]] on the preceding $n_j$, the input can be $(c-1)$-dimensional with $n_c = n - (n_1 + \dots + n_{c - 1})$. Same is true for the probability $p_c$.

# Types
When $c = 2$, it is the [[Binomial Distribution]].

# Properties
## Basic Statistical Properties
- [[Multinomial Distribution Expectation]]
- [[Multinomial Distribution Variance]]
- [[Multinomial Distribution Covariance]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=24)