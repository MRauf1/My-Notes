---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Score Test]] Statistic [[Normal Distribution]] Form)
> For a [[Maximum Likelihood Estimation]] with [[Hypothesis Test]] $H_0: \beta = \beta_0$, the statistic is
> $$
> \begin{align}
> z_S = \frac{u(\beta_0)}{\sqrt{\iota(\beta_0)}} \sim_{H_0} N(0, 1)
> \end{align}
> $$
> where $u(\beta)$ is the [[Score Function]] and $\iota(\beta)$ is the [[Fisher Information]].

Its distribution under $H_0$ is approximately $N(0, 1)$.

Reject $H_0$ if $|z_S| \geq z_{\alpha/2}$.

> [!info] Definition 2 ([[Score Test]] Statistic [[Chi-Squared Distribution]] Form)
> For a [[Maximum Likelihood Estimation]] with [[Hypothesis Test]] $H_0: \beta = \beta_0$, the statistic is
> $$
> \begin{align}
> z^2_S = \frac{u(\beta_0)^2}{\iota(\beta_0)} \sim_{H_0} \chi^2(1)
> \end{align}
> $$
> where $u(\beta)$ is the [[Score Function]] and $\iota(\beta)$ is the [[Fisher Information]].

> [!info] Definition 3 ([[Score Test]] Multivariate Statistic)
> For a [[Maximum Likelihood Estimation]] with [[Hypothesis Test]] $H_0: \mathbf{\beta} = \mathbf{\beta_0}$, the statistic is
> $$
> \begin{align}
> z_S = u(\mathbf{\beta_0})^T I(\mathbf{\beta_0})^{-1} u(\mathbf{\beta_0}) \sim_{H_0} \chi^2(df)
> \end{align}
> $$
> where $u(\beta)$ is the [[Score Function]] and $\iota(\beta)$ is the [[Fisher Information]], and $df$ is the number of non-redundant parameters in $\mathbf{\beta}$.
