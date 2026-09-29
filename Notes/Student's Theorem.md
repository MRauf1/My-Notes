---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Student's Theorem[^1]
> Let $X_1, \dots, X_n$ be [[Independent and Identically Distributed|iid]] $N(\mu, \sigma^2)$, with [[Sample Mean]] $\bar{X} = \frac1n\sum_i X_i$ and [[Sample Variance]] $S^2 = \frac{1}{n-1}\sum_i (X_i - \bar{X})^2$. Then
> 1. $\bar{X} \sim N(\mu, \sigma^2/n)$;
> 2. $\bar{X}$ and $S^2$ are independent;
> 3. $(n - 1)S^2/\sigma^2 \sim \chi^2(n - 1)$;
> 4. the random variable
> $$
> \begin{align}
> T = \frac{\bar{X} - \mu}{S/\sqrt{n}}
> \end{align}
> $$
> has a [[t-Distribution]] with $n - 1$ degrees of freedom.

Part 1 is [[Normal Distribution Linear Combination]]. Part 2 holds because $\bar{X}$ and the residual vector $(X_1 - \bar{X}, \dots, X_n - \bar{X})$ are jointly normal and uncorrelated, hence independent ([[Multivariate Normal Distribution Independence]]); $S^2$ is a function of the residuals. Part 3: the residuals live in the $(n-1)$-dimensional subspace orthogonal to $(1, \dots, 1)$, so $\sum_i (X_i - \bar{X})^2/\sigma^2$ is a sum of $n - 1$ independent squared standard normals ([[Chi-Squared Distribution]]). Part 4: $T = \frac{(\bar{X} - \mu)/(\sigma/\sqrt{n})}{\sqrt{[(n-1)S^2/\sigma^2]/(n-1)}}$ is a standard normal over the square root of an independent chi-squared divided by its degrees of freedom; the unknown $\sigma$ cancels.

# Properties
- $T$ depends on $\mu$ but not on $\sigma$, so it is a pivot for $\mu$ when $\sigma$ is unknown: it gives the $t$ confidence interval $\bar{X} \pm t_{\alpha/2, n-1}S/\sqrt{n}$ and the one-sample $t$-test.
- The independence of $\bar{X}$ and $S^2$ characterizes the normal distribution: for iid samples it holds only for normal data.
- Part 3 gives $E(S^2) = \sigma^2$ and $\text{Var}(S^2) = 2\sigma^4/(n - 1)$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=230)
