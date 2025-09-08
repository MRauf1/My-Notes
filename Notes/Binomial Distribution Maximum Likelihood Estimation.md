---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Binomial Distribution]] [[Maximum Likelihood Estimation]])[^1]
> The maximum likelihood estimation for the binomial parameter $p$ is
> $$
> \begin{align}
> L(p) &= x log(p) + (n - x)log(1 - p) \\
> \frac{\partial L(p)}{\partial p} &= \frac{x - np}{p(1 - p)}
> \end{align}
> $$
> Giving us $\hat{p} = \frac{x}{n}$. This [[Random Variable]] has the statistics
> $$
> \begin{align}
> E[\hat{p}] &= p \\
> Var[\hat{p}] &= \frac{p(1 - p)}{n}
> \end{align}
> $$

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=28)