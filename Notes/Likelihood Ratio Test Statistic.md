---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Likelihood Ratio Test]] [[Chi-Squared Distribution]] Statistic)
> For an [[Maximum Likelihood Estimation]] with optimal predicted parameter $\hat{\beta}$ and a [[Hypothesis Test]] $H_0: \beta = \beta_0$, the statistic is 
> $$
> \begin{align}
> - 2 ln(\Lambda) = -2 (L(\beta_0) - L(\hat{\beta})) \sim_{H_0} \chi^2(1)
> \end{align}
> $$
> where $\Lambda = \frac{l(\beta_0)}{l(\hat{\beta})}$ is the [[Likelihood Ratio]], which cannot exceed $1$.

It has an approximate $\chi^2(1)$ distribution under $H_0$.

Reject $H_0$ if $-2 ln(\Lambda) \geq \chi^2_1(\alpha)$.

> [!info] Definition 2 ([[Likelihood Ratio Test]] Multivariate Statistic)
> For an [[Maximum Likelihood Estimation]] with optimal predicted parameter $\mathbf{\hat{\beta}}$ and a [[Hypothesis Test]] $H_0: \mathbf{\beta} = \mathbf{\beta_0}$, the statistic is 
> $$
> \begin{align}
> - 2 ln(\Lambda) = -2 (L(\mathbf{\beta_0}) - L(\mathbf{\hat{\beta}})) \sim_{H_0} \chi^2(df)
> \end{align}
> $$
> where $\Lambda = \frac{l(\mathbf{\beta_0})}{l(\mathbf{\hat{\beta}})}$ is the [[Likelihood Ratio]], and $df$ is the number of non-redundant parameters in $\mathbf{\beta}$.