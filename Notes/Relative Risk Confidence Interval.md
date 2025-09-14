---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Relative Risk]] [[Confidence Interval]])
> Approximate $(1 - \alpha)100\%$ CI for $ln(RR)$ is
> $$
> \begin{align}
> ln(RR) \pm z_{\alpha/2} \sqrt{\frac{1 - \hat{p_1}}{y_1} + \frac{1 - \hat{p_2}}{y_2}}
> \end{align}
> $$
> Exponentiation of the endpoints gives the CI for $RR$: $(exp(Lower), exp(Upper))$
> If CI includes $1$, then it implies that $X, Y$ are [[Independent Random Variable]].