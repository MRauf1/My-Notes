---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Asymptotic Normality of the MLE[^1]
> Let $X_1, \dots, X_n$ be iid with pdf $f(x; \theta_0)$ satisfying the [[Maximum Likelihood Regularity Conditions|regularity conditions]] (R0)-(R5), with [[Fisher Information]] $0 < I(\theta_0) < \infty$. Then any consistent sequence of solutions $\hat{\theta}_n$ of the likelihood equations satisfies
> $$
> \begin{align}
> \sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{D} N\left(0, \frac{1}{I(\theta_0)}\right)
> \end{align}
> $$

> [!abstract] Multiparameter Version[^2]
> For $\boldsymbol{\theta} \in \Omega \subseteq \mathbb{R}^p$ under regularity conditions, the likelihood equation $\partial l(\boldsymbol{\theta})/\partial\boldsymbol{\theta} = \mathbf{0}$ has a solution $\hat{\boldsymbol{\theta}}_n \xrightarrow{P} \boldsymbol{\theta}$, and any such sequence satisfies
> $$
> \begin{align}
> \sqrt{n}(\hat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}) \xrightarrow{D} N_p(\mathbf{0}, I^{-1}(\boldsymbol{\theta}))
> \end{align}
> $$
> with [[Fisher Information Matrix]] $I(\boldsymbol{\theta})$; in particular $\sqrt{n}(\hat{\theta}_{n,j} - \theta_j) \xrightarrow{D} N(0, [I^{-1}(\boldsymbol{\theta})]_{jj})$, so the MLE is asymptotically efficient componentwise.

The asymptotic variance $1/(nI(\theta_0))$ equals the [[Rao-Cramér Lower Bound]], so the MLE is asymptotically [[Efficient Estimator|efficient]]. The key step is a Taylor expansion of the likelihood equation around $\theta_0$, which gives the linear representation[^3]
$$
\begin{align}
\sqrt{n}(\hat{\theta}_n - \theta_0) = \frac{1}{I(\theta_0)}\frac{1}{\sqrt{n}}\sum_{i=1}^n \frac{\partial \log f(X_i; \theta_0)}{\partial\theta} + R_n, \quad R_n \xrightarrow{P} 0
\end{align}
$$
The MLE error is asymptotically a scaled average of iid [[Score Function|scores]], which have mean $0$ and variance $I(\theta_0)$, so the [[Central Limit Theorem]] applies.

# Properties
- Consistency:[^4] under (R0)-(R2) and differentiability of $f$ in $\theta$, the likelihood equation has a solution $\hat{\theta}_n \xrightarrow{P} \theta_0$, and if the solution is unique it is a [[Consistent Estimator]].
- Inference:[^5] since $I(\hat{\theta}_n) \xrightarrow{P} I(\theta_0)$, the asymptotic standard deviation $[nI(\theta_0)]^{-1/2}$ is consistently estimated, giving the approximate $(1-\alpha)100\%$ [[Confidence Interval]]
$$
\begin{align}
\hat{\theta}_n \pm z_{\alpha/2}\frac{1}{\sqrt{nI(\hat{\theta}_n)}}
\end{align}
$$
  ([[Wald Test Confidence Interval]], [[Maximum Likelihood Estimator Standard Error]]).
- Functions of the MLE:[^5] if $g$ is continuous and differentiable at $\theta_0$ with $g'(\theta_0) \neq 0$ (the printed "$g'(\theta_0) = 0$" is a typo), then $\sqrt{n}(g(\hat{\theta}_n) - g(\theta_0)) \xrightarrow{D} N\left(0, \frac{g'(\theta_0)^2}{I(\theta_0)}\right)$, by the [[Delta Method]] and [[Maximum Likelihood Estimator Invariance]]. For vectors,[^2] $\hat{\boldsymbol{\eta}} = g(\hat{\boldsymbol{\theta}})$ satisfies $\sqrt{n}(\hat{\boldsymbol{\eta}} - \boldsymbol{\eta}) \xrightarrow{D} N_k(\mathbf{0}, BI^{-1}(\boldsymbol{\theta})B^T)$ with $B = [\partial g_i/\partial\theta_j]$, so the information for $\boldsymbol{\eta}$ is $[BI^{-1}(\boldsymbol{\theta})B^T]^{-1}$ when the inverse exists.
- Summarized in [[Maximum Likelihood Estimation Properties]]; the approximation is the basis of the [[Wald Test]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=385)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=409)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=388)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=375)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=387)
