---
tags:
  - statistics
  - categorical_variable_prediction
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

[[Negative Binomial Distribution]] is a better alternative to Poisson when overdispersion is present. The strict inequality $>$ is correct: $Var[\mu] = 0$ means there is no overdispersion, reducing to the plain Poisson case where $Var[X] = \theta$.

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=25)