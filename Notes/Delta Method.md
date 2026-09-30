---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Delta Method[^1]
> Let $\{X_n\}$ satisfy
> $$
> \begin{align}
> \sqrt{n}(X_n - \theta) \xrightarrow{D} N(0, \sigma^2)
> \end{align}
> $$
> and let $g$ be differentiable at $\theta$ with $g'(\theta) \neq 0$. Then
> $$
> \begin{align}
> \sqrt{n}\big(g(X_n) - g(\theta)\big) \xrightarrow{D} N\big(0, \sigma^2[g'(\theta)]^2\big)
> \end{align}
> $$

> [!abstract] Multivariate Delta Method[^2]
> Let $\sqrt{n}(\mathbf{X}_n - \boldsymbol{\mu}_0) \xrightarrow{D} N_p(\mathbf{0}, \Sigma)$, and let $g(\mathbf{x}) = (g_1(\mathbf{x}), \dots, g_k(\mathbf{x}))^T$, $1 \leq k \leq p$, have a $k \times p$ [[Jacobian Matrix]] $B = [\partial g_i / \partial \mu_j]$ that is continuous and nonvanishing near $\boldsymbol{\mu}_0$. With $B_0 = B(\boldsymbol{\mu}_0)$,
> $$
> \begin{align}
> \sqrt{n}\big(g(\mathbf{X}_n) - g(\boldsymbol{\mu}_0)\big) \xrightarrow{D} N_k(\mathbf{0}, B_0\Sigma B_0^T)
> \end{align}
> $$

The condition in the printed text, "$g'(\theta) = 0$", is a typo for $g'(\theta) \neq 0$: with $g'(\theta) = 0$ the limit would be the degenerate $N(0, 0)$, and a second-order expansion is needed instead.

**Idea.** Linearize $g$ at $\theta$: $g(X_n) = g(\theta) + g'(\theta)(X_n - \theta) + o_p(|X_n - \theta|)$ ([[Little O]]). Multiplying by $\sqrt{n}$, the linear term converges to $g'(\theta)N(0, \sigma^2)$, while the remainder is $o_p(1)\cdot O_p(1) \xrightarrow{P} 0$ ([[Bounded in Probability]]) and drops out by [[Slutsky's Theorem]]. Near $\theta$, a smooth function is approximately linear, and a linear function of an approximately normal variable is approximately normal, with the standard deviation scaled by $|g'(\theta)|$. In the multivariate case the covariance transforms as $B_0\Sigma B_0^T$, exactly as for the linear map $B_0$ ([[Covariance Matrix]]).

# Properties
- Gives asymptotic [[Standard Error|standard errors]] and [[Confidence Interval|confidence intervals]] for smooth functions of estimators, e.g. $\log\bar{X}$, $1/\bar{X}$, ratios, the sample correlation, and the sample variance (a smooth function of the first two sample moments).
- Combined with the [[Central Limit Theorem]], it shows that most smooth statistics, not just the sample mean, are asymptotically normal.
- Variance-stabilizing transformations choose $g$ with $g'(\theta)\sigma(\theta)$ constant, so the limiting variance no longer depends on $\theta$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=351)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=369)
