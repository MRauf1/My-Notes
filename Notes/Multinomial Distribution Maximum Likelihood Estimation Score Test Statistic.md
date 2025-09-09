---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Multinomial Distribution]] [[Maximum Likelihood Estimation]] [[Score Test Statistic]])
> For a [[Multinomial Distribution]]'s [[Maximum Likelihood Estimation]] with the ideal predicted $\hat{p_j} = \frac{n_j}{n}$, the statistic is
> $$
> \begin{align}
> X^2 = \sum_{j} \frac{(n_j - \mu_j)^2}{\mu_j} \sim_{H_0} \chi^2(c-1)
> \end{align}
> $$
> where $\mu_j = n p_{j0} = E_{H_0}[N_j]$.

$X^2$ has the form $\sum (\frac{(\text{observed} - \text{expected})^2}{(\text{expected})})$.

The score test in this case is the [[Pearson Chi-Squared Test]].