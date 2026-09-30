---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] James-Stein Estimator
> Let $\mathbf{X} \sim N_p(\boldsymbol{\theta}, \sigma^2 I)$ with $\sigma^2$ known and $p \geq 3$. The James-Stein estimator of $\boldsymbol{\theta}$ is
> $$
> \begin{align}
> \hat{\boldsymbol{\theta}}_{JS} = \left(1 - \frac{(p - 2)\sigma^2}{\lVert\mathbf{X}\rVert^2}\right)\mathbf{X}
> \end{align}
> $$
> Under total squared-error loss $L(\boldsymbol{\theta}, \mathbf{a}) = \lVert\boldsymbol{\theta} - \mathbf{a}\rVert^2$, it satisfies $R(\boldsymbol{\theta}, \hat{\boldsymbol{\theta}}_{JS}) < R(\boldsymbol{\theta}, \mathbf{X}) = p\sigma^2$ for every $\boldsymbol{\theta}$.

Stein's paradox: the unbiased, maximum likelihood, and componentwise MVUE estimator $\mathbf{X}$ is inadmissible when $p \geq 3$, even though the coordinates are independent ([[Risk Function (Statistics)]]). Shrinking all coordinates toward a common point introduces bias but reduces variance by more, so the total [[Mean Squared Error]] is uniformly lower. The gain is largest when $\boldsymbol{\theta}$ is near the shrinkage target, and it vanishes as $\lVert\boldsymbol{\theta}\rVert \to \infty$.

# Properties
- The improvement is in total MSE. Individual coordinates can be estimated worse.
- The positive-part version, $(1 - (p-2)\sigma^2/\lVert\mathbf{X}\rVert^2)_+\mathbf{X}$, dominates $\hat{\boldsymbol{\theta}}_{JS}$, and is itself inadmissible.
- Shrinking toward the grand mean $\bar{X}\mathbf{1}$ instead of $\mathbf{0}$ needs $p \geq 4$, with $p - 3$ in place of $p - 2$.
- Empirical Bayes interpretation: with prior $\boldsymbol{\theta} \sim N_p(\mathbf{0}, \tau^2 I)$, the [[Bayes Estimator]] is $(1 - \sigma^2/(\sigma^2 + \tau^2))\mathbf{X}$. Estimating the shrinkage factor unbiasedly from the marginal of $\mathbf{X}$ gives James-Stein.
- A member of the family of shrinkage estimators, alongside ridge regression ([[L2 Regularization]]) and the divisor-$(n+1)$ variance estimator. All of them trade a small bias for a large drop in variance ([[Bias-Variance Tradeoff]]), and all beat the [[Minimum Variance Unbiased Estimator]] in MSE.
