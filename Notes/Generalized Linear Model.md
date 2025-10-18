---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Generalized Linear Model)
> Generalized Linear Model consists of $3$ components:
> 1) Random Component: Dependent variable $Y$ with a [[Probability Distribution]] from the [[Exponential Family]].
> 2) [[Systematic Component]]/Linear Predictor: $\eta = X \beta$, where $X$ is an independent variable with $p$ predictors and $\beta$ are the coefficients of the linear predictor.
> 3) [[Link Function]]: [[Function]] $g$ such that for $E[Y | X] = \mu$, $g(\mu) = \eta$.
> The [[Canonical Link]] satisfies $g(\mu) = Q(\theta)$, where $Q(\theta)$ is the natural parameter of the [[Exponential Family]]. This leads to $Q(\theta) = \eta$.

# Types
- [[Linear Regression as Generalized Linear Model]]
- [[Binary Logistic Regression as Generalized Linear Model]]
- [[Binomial Regression as Generalized Linear Model]]
- [[Poisson Regression as Generalized Linear Model]]

# Properties
## Assumptions
- [[Generalized Linear Model Assumptions]]
- 
## [[Goodness of Fit Test]]
- [[Generalized Linear Model Deviance]]
- [[Nested Model Comparison]]

## [[Fisher Information Matrix]]
- [[Generalized Linear Model Fisher Information Matrix]]
- [[Distribution of Estimated Parameter]]

#TODO 
- Should Y be from exponential family or natural exponential family?
- Should it be $E[Y|X]$ or $E[Y]$?
- Make a separate link for canonical link?