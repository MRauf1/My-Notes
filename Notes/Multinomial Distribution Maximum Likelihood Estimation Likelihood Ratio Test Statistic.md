---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Multinomial Distribution]] [[Maximum Likelihood Estimation]] [[Likelihood Ratio Test Statistic]])
> For a [[Multinomial Distribution]]'s [[Maximum Likelihood Estimation]] with the ideal predicted $\hat{p_j} = \frac{n_j}{n}$, the statistic is
> $$
> \begin{align}
> G^2 = -2 ln(\Lambda) = 2 \sum_{j} n_j ln(\frac{n_j}{\mu_j}) \sim_{H_0} \chi^2(c - 1)
> \end{align}
> $$
> where $\mu_j = n p_{j0} = E_{H_0}[N_j]$.

$G^2$ has the form $2 \sum (\text{observed}) \cdot ln (\frac{(\text{observed})}{(\text{expected})})$.

$G^2$ is asymptotically equivalent to $X^2$ ([[Multinomial Distribution Maximum Likelihood Estimation Score Test Statistic]]), but converges to $\chi^2$ more slowly.