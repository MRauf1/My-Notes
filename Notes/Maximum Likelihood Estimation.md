---
tags: statistics, categorical_variable_prediction
---

# Definition

A technique for [[Parameter Estimation]]. It works by calculating a [[Likelihood Function]] as a function of the parameter. The maximum likelihood estimate is the parameter value that maximizes this function, denoted as $\hat{\beta}$ (parameter value under which the observed data has the highest probability of occurring).

Instead of maximizing the likelihood function directly, we instead maximizes the [[Logarithm]] of it, which converts products into sums, which are easier to deal with.[^1]

Steps:
1) Calculate $L(\beta) = log(l(\beta))$.
2) Calculate and set the [[Equation]] $\frac{\partial L(\beta)}{\partial \beta} = 0$.
3) Solve for $\beta$. Once solved, it is now denoted as $\hat{\beta}$.

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=27)