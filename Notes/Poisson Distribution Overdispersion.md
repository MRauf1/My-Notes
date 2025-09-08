---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Poisson Distribution]] [[Probability Distribution Overdispersion]])[^1]
> Let $\theta = E[\mu]$. Then
> $$
> \begin{align}
> E[X] &= E[\mu] = \theta \\
> Var[X] &= E[\mu] + Var[\mu] = \theta + Var[\mu] > \theta
> \end{align}
> $$

[[Negative Binomial Distribution]] is a better alternative to Poisson when overdispersion is present.

#TODO 
- Should it be $\geq$ or $>$? Can't variance be 0?

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=25)