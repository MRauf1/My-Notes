---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Sufficient Statistic[^1]
> Let $X_1, \dots, X_n$ be a random sample from a distribution with pdf or pmf $f(x; \theta)$, $\theta \in \Omega$. Let $Y_1 = u_1(X_1, \dots, X_n)$ be a [[Statistic]] with pdf or pmf $f_{Y_1}(y_1; \theta)$. Then $Y_1$ is a sufficient statistic for $\theta$ if and only if
> $$
> \begin{align}
> \frac{f(x_1; \theta)f(x_2; \theta)\cdots f(x_n; \theta)}{f_{Y_1}[u_1(x_1, \dots, x_n); \theta]} = H(x_1, \dots, x_n)
> \end{align}
> $$
> where $H(x_1, \dots, x_n)$ does not depend on $\theta \in \Omega$.

> [!info] Non-iid Extension (Remark 7.2.1)[^2]
> The $X_i$ need not be independent or identically distributed. With joint pdf or pmf $f(x_1, \dots, x_n; \theta)$, $Y_1$ is sufficient if
> $$
> \begin{align}
> \frac{f(x_1, \dots, x_n; \theta)}{f_{Y_1}[u_1(x_1, \dots, x_n); \theta]} = H(x_1, \dots, x_n)
> \end{align}
> $$
> does not depend on $\theta \in \Omega$.

> [!info] Joint Sufficiency[^3]
> Let $\theta \in \Omega \subset \mathbb{R}^p$, let $S$ be the support of $X$, and let $\mathbf{Y} = (Y_1, \dots, Y_m)^T$ with $Y_i = u_i(X_1, \dots, X_n)$ and pdf or pmf $f_{\mathbf{Y}}(\mathbf{y}; \boldsymbol{\theta})$. Then $\mathbf{Y}$ is jointly sufficient for $\boldsymbol{\theta}$ if and only if
> $$
> \begin{align}
> \frac{\prod_{i=1}^n f(x_i; \boldsymbol{\theta})}{f_{\mathbf{Y}}(\mathbf{y}; \boldsymbol{\theta})} = H(x_1, \dots, x_n) \quad \text{for all } x_i \in S
> \end{align}
> $$
> where $H$ does not depend on $\boldsymbol{\theta}$. In general $m \neq p$: the number of sufficient statistics need not equal the number of parameters, although it usually does in practice.[^4] (The printed "In general, $m = p$" is garbled.)

The ratio is the conditional pmf of the sample given $Y_1 = y_1$. So the definition says that the conditional distribution of $X_1, \dots, X_n$ given $Y_1$ does not depend on $\theta$.

**Partition intuition.**[^5] Any statistic $Y_1 = u_1(X_1, \dots, X_n)$ partitions the sample space into the level sets $\{(x_1, \dots, x_n) : u_1(x_1, \dots, x_n) = y_1\}$. $Y_1$ is sufficient when, once we know which set the sample fell in, the conditional distribution of the sample within that set is free of $\theta$.[^6]
- Then any other statistic $Y_2$, given $Y_1 = y_1$, has a distribution free of $\theta$, so it cannot be used to infer anything more about $\theta$.
- In this sense, $Y_1$ exhausts all the information about $\theta$ contained in the sample.
- Equivalently, the data could be regenerated from $Y_1$ by a random mechanism that does not involve $\theta$.

# Properties
- Characterized by the [[Neyman Factorization Theorem]], which is usually easier to apply than the definition because the distribution of $Y_1$ is not needed.
- Not unique:[^7] if $Y_1$ is sufficient and $Y_2 = g(Y_1)$ with $g$ one-to-one, then $\prod f(x_i; \theta) = k_1[g^{-1}(y_2); \theta]\,k_2(x_1, \dots, x_n)$, so $Y_2$ is also sufficient. The same holds for one-to-one transformations of jointly sufficient vectors. The sample itself, and the vector of [[Order Statistic|order statistics]] for iid data, are always sufficient.
- MLE connection (Theorem 7.3.2):[^8] if a sufficient statistic $Y_1$ exists and the [[Maximum Likelihood Estimation|MLE]] $\hat{\theta}$ exists uniquely, then $\hat{\theta}$ is a function of $Y_1$. This is because $L(\theta) = k_1(y_1; \theta)k_2(\mathbf{x})$ is maximized through $k_1$ alone.
  - MLEs are asymptotically unbiased, so a practical route to an MVUE is: find $Y_1$, find the MLE, and adjust it into an unbiased function of $Y_1$.
- The search for an MVUE can be restricted to functions of a sufficient statistic ([[Rao-Blackwell Theorem]]). If the statistic is also complete, the unbiased function of it is the unique [[Minimum Variance Unbiased Estimator|MVUE]] ([[Lehmann-Scheffé Theorem]]).
- For the [[Regular Exponential Class]], $\sum_i K(X_i)$ (or $(\sum_i K_1(X_i), \dots, \sum_i K_m(X_i))$) is complete and sufficient.
- The smallest reduction that keeps sufficiency is the [[Minimal Sufficient Statistic]]. Its opposite is an [[Ancillary Statistic]], whose distribution is free of $\theta$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=437&annotation=UI2UUV5V)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=437&annotation=E8527QVF)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=463&annotation=MNHL6KI5)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=463&annotation=99I3X55D)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=435&annotation=M75GQ92V)
[^6]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=436&annotation=3XIF39Q7)
[^7]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=442&annotation=WQDNHY2Q)
[^8]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=443&annotation=LFI7WAUU)
