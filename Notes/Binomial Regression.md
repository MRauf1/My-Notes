---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Binomial Regression)[^1]
> A [[Generalized Linear Model]] for counts of successes $Y_i \sim \operatorname{Binomial}(n_i, \pi_i)$ out of $n_i$ trials at predictor values $x_i$, with
> $$
> \begin{align}
> g(\pi_i) = x_i \beta
> \end{align}
> $$
> for a [[Link Function|link function]] $g$ mapping $(0, 1)$ to $\mathbb{R}$. The [[Logit Function|logit]] link gives grouped [[Logistic Regression|logistic regression]]; $n_i = 1$ recovers [[Binary Logistic Regression]].


# Properties
- [[Binomial Regression Fisher Information Matrix]]
- [[Binomial Regression Deviance]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L)
