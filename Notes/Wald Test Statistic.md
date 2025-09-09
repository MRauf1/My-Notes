---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Wald Test Statistic ([[Normal Distribution]] Form))
> For a [[Maximum Likelihood Estimation]], to test the [[Null Hypothesis]] $H_0: \beta = \beta_0$, the Wald test statistic is
> $$
> \begin{align}
> z_w = \frac{\hat{\beta} - \beta_0}{SE} \sim_{H_0} N(0, 1)
> \end{align}
> $$
> where $SE = \sqrt{\frac{1}{\iota(\hat{\beta})}}$

Reject the null hypothesis if $|z_w| \geq z_{\alpha/2}$ for a [[Two-Sided Test]] with $\alpha$.

> [!info] Definition 2 (Wald Test Statistic ([[Chi-Squared Distribution]] Form))
> For a [[Maximum Likelihood Estimation]], to test the [[Null Hypothesis]] $H_0: \beta = \beta_0$, the Wald test statistic is
> $$
> \begin{align}
> z_w^2 = \frac{(\hat{\beta} - \beta_0)^2}{SE^2} \sim_{H_0} \chi^2(1)
> \end{align}
> $$
> where $SE = \sqrt{\frac{1}{\iota(\hat{\beta})}}$

> [!info] Definition 3 (Multivariate Wald Test Statistic)
> To test $H_0: \mathbf{\beta} = \mathbf{\beta_0}$, the Wald test statistic is
> $$
> \begin{align}
> W = (\mathbf{\hat{\beta}} - \mathbf{\beta_0})^T [Cov[\mathbf{\hat{\beta}}]]^{-1} (\mathbf{\hat{\beta}} - \mathbf{\beta_0}) \sim_{H_0} \chi^2(df)
> \end{align}
> $$
> where $df$ is the number of non-redundant parameters in $\mathbf{\beta}$.

Asymptotic [[Normal Distribution]] for $\mathbf{\hat{\beta}}$ implies an asymptotic [[Chi-Squared Distribution]] for $W$ with [[Degree of Freedom]] being $rank(Cov[\mathbf{\hat{\beta}}])$.
