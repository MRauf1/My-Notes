---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Odds Ratio]] [[Confidence Interval]])
> The approximate $(1 - \alpha)100\%$ CI for $ln(\theta)$ is
> $$
> \begin{align}
> ln(\hat{\theta}) \pm z_{\alpha/2} \sqrt{\frac{1}{n_{11}} + \frac{1}{n_{12}} + \frac{1}{n_{21}} + \frac{1}{n_{22}}}
> \end{align}
> $$
> Exponentiating of endpoints gives the CI for $\theta$: $(exp(Lower), exp(Upper))$
> If CI contains $1$, then it implies that $X, Y$, are [[Independent Random Variable]]