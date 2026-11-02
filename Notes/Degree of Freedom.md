---
tags:
  - statistics
  - mathematical_statistics
  - statistical_learning
---

# Definition

> [!info] Definition 1 (Degree of Freedom)[^2]
> The number of independent quantities that are free to vary: the dimension of the space a statistic, residual vector, or parameter ranges over once all constraints are imposed.

> [!info] Definition 2 (Degrees of Freedom of a Distribution or Test)[^2]
> The parameter $\nu$ of the [[Chi-Squared Distribution]], $t$-distribution, and $F$-distribution, counting independent squared standard normal components: $\chi^2_\nu \overset{d}{=} \sum_{i=1}^{\nu} Z_i^2$ for i.i.d. $Z_i \sim N(0, 1)$. Concretely:
> - In a likelihood-ratio, [[Wald Test Statistic|Wald]], or score test of $H_0: \theta \in \Theta_0$ against $\theta \in \Theta$, the limiting $\chi^2$ has $\nu = \dim \Theta - \dim \Theta_0$, the number of independent constraints imposed by $H_0$.
> - The residuals of a least-squares fit with $p$ parameters to $n$ observations have $n - p$ degrees of freedom.

> [!info] Definition 3 (Degrees of Freedom of a Model)[^1]
> For [[Statistical Learning]] models, the degrees of freedom measure the flexibility of the model: the number of free parameters fitted to the data. For a linear smoother $\hat{\mathbf{y}} = S \mathbf{y}$ (e.g., a smoothing spline), the effective degrees of freedom are $\operatorname{tr}(S)$.

All three are the same count. For least squares, $S$ is the orthogonal projection onto the $p$-dimensional column space, so $\operatorname{tr}(S) = \operatorname{rank}(S) = p$ model degrees of freedom, leaving $n - p$ for the residuals, whose scaled sum of squares is $\chi^2_{n-p}$ under Gaussian errors.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=40)
[^2]: [Degrees of Freedom (Statistics) (Wikipedia)](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics))
