---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Binomial Distribution]] [[Maximum Likelihood Estimation]] [[Likelihood Ratio Test Confidence Interval]])
> For a [[Binomial Distribution]] [[Maximum Likelihood Estimation]] with the obtained parameter $\hat{p} = \frac{x}{n}$, the [[Hypothesis Test]] $H_0: p = p_0$ with the [[Likelihood Ratio Test]] produces the [[Confidence Interval]]
> $$
> \begin{align}
> \{p:& -2 ln(\Lambda) < \chi_1^2(\alpha)\} = \\
> &= \{p: 2 (x ln(\frac{x}{n p_0}) + (n - x) ln(\frac{n - x}{n - n p_0})) < \chi_1^2(\alpha)\}
> \end{align}
> $$
> at confidence level $\alpha$.