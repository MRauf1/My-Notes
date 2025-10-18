---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Nested Model Comparison)
> For [[Generalized Linear Model]] $M_0 \subseteq M_1$ (nested: every distribution in $M_0$ is also in $M_1$), then for $H_0: M_0$ is true and $H_a: M_1$ is true, but not $M_0$, the [[Likelihood Ratio Test]] [[Chi-Squared Distribution]] statistic gives
> $$
> \begin{align}
> D(\mathbf{y}, \hat{\mathbf{\mu}}_0) - D(\mathbf{y}, \hat{\mathbf{\mu}}_1)
> \end{align}
> $$
> where $\hat{\mathbf{\mu}}_i$ is the MLE of model $M_i$.
> The statistic is always non-negative.
> The [[Degree of Freedom]] is $df =$ effective # of parameters in $M_1$ $-$ effective # of parameters in $M_0$.

# Extensions
- [[Profile Likelihood Confidence Interval]]