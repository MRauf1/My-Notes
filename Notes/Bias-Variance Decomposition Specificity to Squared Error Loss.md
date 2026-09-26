---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Bias-Variance Decomposition Specificity to Squared Error Loss[^1]
> The exact additive decomposition of expected loss into squared [[Bias]] plus [[Variance]] holds for squared-error ([[L2 Loss|$L_2$]]) loss, and not for other [[Loss Function|loss functions]] in general. For an estimator $\hat{\theta}$ of a fixed $\theta$,
> $$
> \begin{align}
> \mathbb{E}\big[(\hat{\theta} - \theta)^2\big] &= \mathbb{E}\big[(\hat{\theta} - \mathbb{E}[\hat{\theta}] + \mathbb{E}[\hat{\theta}] - \theta)^2\big] \\
> &= \mathbb{E}\big[(\hat{\theta} - \mathbb{E}[\hat{\theta}])^2\big] + 2\big(\mathbb{E}[\hat{\theta}] - \theta\big)\underbrace{\mathbb{E}\big[\hat{\theta} - \mathbb{E}[\hat{\theta}]\big]}_{=0} + \big(\mathbb{E}[\hat{\theta}] - \theta\big)^2 \\
> &= \mathrm{Var}(\hat{\theta}) + \mathrm{Bias}(\hat{\theta})^2
> \end{align}
> $$
> The cross term vanishes because $\mathbb{E}[\hat{\theta}] - \theta$ is deterministic and a centered random variable has zero [[Expectation|expectation]]. For other losses no such cross-term cancellation occurs:
> - **Absolute ($L_1$) loss** $\mathbb{E}\big[|\hat{\theta} - \theta|\big]$: the natural center is the [[Median|median]] $m$ of $\hat{\theta}$ rather than its mean, and the natural spread is the mean absolute deviation about $m$; the loss only satisfies the [[Triangle Inequality|triangle-inequality]] bound $\mathbb{E}|\hat{\theta} - \theta| \le \mathbb{E}|\hat{\theta} - m| + |m - \theta|$, not an equality.
> - **0-1 loss** $P(\hat{Y} \neq Y)$: bias (underfitting) and variance (overfitting) remain meaningful intuitively, but the misclassification probability is not an exact additive sum $\text{Bias} + \text{Variance}$.
> - **General $L_p$ loss** $\mathbb{E}\big[|\hat{\theta} - \theta|^p\big]$, $p \neq 2$: $|a + b|^p$ does not expand into $|a|^p + |b|^p$ plus a term linear in $a$, so the interaction terms do not vanish and the loss cannot be written as $\text{Bias}^2 + \mathrm{Var}$.

# Properties
- Geometrically, the decomposition is the Pythagorean theorem in the [[Hilbert Space]] $L^2$ of square-integrable random variables: $\mathbb{E}[\hat{\theta}]$ is the [[Orthogonal Projection|orthogonal projection]] of $\hat{\theta}$ onto the constants, so $\hat{\theta} - \mathbb{E}[\hat{\theta}]$ is orthogonal to the constant $\mathbb{E}[\hat{\theta}] - \theta$. Only the $p = 2$ [[p-Norm|$p$-norm]] comes from an inner product, which is why no other $L_p$ loss decomposes.
- Underlies the [[Bias-Variance-MSE Decomposition of an Estimator]] and the [[Bias-Variance Tradeoff]] for test [[Mean Squared Error]].

[^1]: [All Models Are Wrong: Concepts of Statistical Learning](https://allmodelsarewrong.github.io/)
