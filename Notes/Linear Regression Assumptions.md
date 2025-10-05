---
tags: statistics, statistical_learning
---

# Definition

1) A linear model is a good fit for the data. In particular, we assume the data distribution follows $y = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p + \epsilon$, where $\epsilon$ are the errors.
	1) Additivity: the association between $X_j$ and $Y$ does not depend on the values of other predictors
	2) Linearity: the change in $Y$ associated with a 1-unit change in $X_j$ is constant
2) Errors follow [[Normal Distribution]] (have [[Mean]] of $0$ and constant variance $\sigma^2$).
3) Errors are [[Independent Random Variable|independent]] of $X$.
4) Errors are [[Correlation|uncorrelated]] with each other.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=80)