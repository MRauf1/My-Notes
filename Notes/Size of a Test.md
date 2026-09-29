---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Size (Significance Level) of a Test[^1]
> A [[Critical Region]] $C$ is of size $\alpha$ if
> $$
> \begin{align}
> \alpha = \max_{\theta \in \omega_0} P_\theta[(X_1, \dots, X_n) \in C]
> \end{align}
> $$

**Meaning of $P_\theta$.** $P_\theta$ is the probability computed under the assumption that $\theta$ is the true parameter, i.e. under the distribution $f(\cdot; \theta)$ ([[Parameter Space]]). The probabilities in hypothesis testing are therefore never unconditional: they are always computed under an assumed state of nature, one of the hypotheses. $\theta$ is fixed, not random, so this is not conditioning on an event with a prior probability. Here $P_\theta(\mathbf{X} \in C)$ for $\theta \in \omega_0$ is the probability of a Type I error when that particular $\theta$ holds, and the size is its worst case over the null hypothesis.

# Properties
- Also called the significance level, the maximum probability of a Type I error ([[Type I and Type II Errors]]), and the maximum of the [[Power Function (Statistics)|power function]] over $\omega_0$.[^2]
- For a [[Simple Hypothesis|simple]] null $H_0: \theta = \theta_0$, the maximum is just $P_{\theta_0}(\mathbf{X} \in C)$.
- For discrete test statistics, only certain sizes are attainable without a [[Randomized Test]]; in practice one reports the [[P-Value]] instead.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=284)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=287)
