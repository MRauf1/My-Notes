---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Invariance of the Maximum Likelihood Estimator[^1]
> Let $X_1, \dots, X_n$ be iid with pdf $f(x; \theta)$, $\theta \in \Omega$, let $\eta = g(\theta)$ be a parameter of interest for a specified function $g$, and let $\hat{\theta}$ be the MLE of $\theta$. Then $g(\hat{\theta})$ is the MLE of $\eta = g(\theta)$.

For non-injective $g$, the likelihood of $\eta$ is defined as the induced (profile) likelihood $L^*(\eta) = \sup_{\theta : g(\theta) = \eta} L(\theta)$, which is maximized at $\eta = g(\hat{\theta})$. The result holds for vector $\theta$ as well.[^2]

# Properties
- Estimation commutes with reparametrization: the MLE of $\sigma$ is $\sqrt{\hat{\sigma}^2}$, and the MLE of $e^\theta$ is $e^{\hat{\theta}}$. Unbiasedness has no such property ([[Unbiased Estimator]]).
- Combined with the [[Delta Method]], it gives the asymptotic distribution of $g(\hat{\theta})$ ([[Maximum Likelihood Estimator Asymptotic Normality]]).
- A property of [[Maximum Likelihood Estimation]], listed in [[Maximum Likelihood Estimation Properties]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=374)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=403)
