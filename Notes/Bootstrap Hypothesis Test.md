---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Bootstrap Two-Sample Location Test[^1][^2]
> Let $X_1, \dots, X_{n_1}$ be a [[Random Sample]] from a cdf $F(x)$ and $Y_1, \dots, Y_{n_2}$ one from $F(x - \Delta)$, and test $H_0: \Delta = 0$ versus $H_1: \Delta > 0$ with [[Test Statistic]] $V = \bar{Y} - \bar{X}$ and observed value $v = \bar{y} - \bar{x}$. The [[P-Value]] $P_{H_0}(V \geq v)$ is estimated by:
> 1. Combine the samples into one sample $\mathbf{z} = (\mathbf{x}, \mathbf{y})$.
> 2. For $j = 1, \dots, B$: draw with replacement a sample of size $n_1$ from $\mathbf{z}$ (new $x$'s) and a sample of size $n_2$ from $\mathbf{z}$ (new $y$'s), and compute $v_j^* = \bar{y}_j^* - \bar{x}_j^*$.
> 3. The bootstrap p-value is
> $$
> \begin{align}
> \hat{p}^* = \frac{\#_{j=1}^B\{v_j^* \geq v\}}{B}
> \end{align}
> $$

The key difference from a [[Percentile Bootstrap Confidence Interval]] is that the resampling must be done under $H_0$. Pooling the two samples and resampling both groups from the pool imposes a single common distribution, i.e. $\Delta = 0$. The bootstrap distribution of $V^*$ then approximates the null distribution of $V$.

# Properties
- Here $\Delta$ is a shift in [[Location Parameter|location]]; when the means exist, $\Delta = \mu_Y - \mu_X$.
- Valid by the same theory as bootstrap confidence intervals; it needs no normality assumption, unlike the pooled $t$-test ([[Two-Sample Confidence Interval for Difference of Means]]).
- Resampling without replacement from the pooled sample gives the closely related permutation test.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=324)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=325)
