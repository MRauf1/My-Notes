---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Generalized Linear Model]] [[Deviance]])
> The deviance of GLM is the [[Likelihood Ratio Test]] [[Chi-Squared Distribution]] statistic for $H_0:$ the GLM is correct, $H_a:$ the GLM is incorrect (but the [[Saturated Model]] is correct). It is
> $$
> \begin{align}
> D(\mathbf{y}, \hat{\mathbf{\mu}}) = -2 (L(\hat{\mathbf{\mu}}, \mathbf{y}) - L(\mathbf{y}, \mathbf{y}))
> \end{align}
> $$
> It has [[Degree of Freedom]] $df =$ # means in [[Saturated Model]] $-$ # parameters in GLM, which usually is $df = N - (p + 1)$ for GLM with $p$ parameters $\beta_i$ and $1$ bias term.