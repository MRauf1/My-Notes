---
tags: statistics, categorical_variable_prediction
---

# Definition

A technique for [[Parameter Estimation]]. The maximum likelihood estimate is the parameter value that maximizes the [[Likelihood Function]], denoted as $\hat{\beta}$ (parameter value under which the observed data has the highest probability of occurring).

Instead of maximizing the likelihood function directly, we instead maximize the [[Log-Likelihood Function]], which converts products into sums, which are easier to deal with.[^1]

Steps:
1) Calculate the [[Log-Likelihood Function]] ($L(\beta) = log(l(\beta))$).
2) Calculate the [[Score Function]] and set it equal to $0$ ($u(\beta) = \frac{\partial L(\beta)}{\partial \beta} = 0$). If solving for multiple parameters, the [[Partial Derivative]] will turn into the [[Gradient]].
4) Solve for $\beta$. Once solved, it is now denoted as $\hat{\beta}$.

# Properties
- [[Maximum Likelihood Estimation Properties]]

## Basic Statistical Properties
- [[Maximum Likelihood Estimator Variance]]
- [[Maximum Likelihood Estimator Standard Error]]

## Hypothesis Testing
These three have certain asymptotic equivalences.

- [[Wald Test]]
- [[Likelihood Ratio Test]]
- [[Score Test]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=27)