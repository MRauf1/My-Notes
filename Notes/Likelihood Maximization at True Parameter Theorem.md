---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Likelihood Maximization at True Parameter Theorem[^1]
> Let $\theta_0$ be the true parameter and assume $E_{\theta_0}[f(X_i; \theta)/f(X_i; \theta_0)]$ exists. Under the [[Maximum Likelihood Regularity Conditions|regularity conditions]] (R0) and (R1),
> $$
> \begin{align}
> \lim_{n\to\infty} P_{\theta_0}[L(\theta_0; \mathbf{X}) > L(\theta; \mathbf{X})] = 1 \quad \text{for all } \theta \neq \theta_0
> \end{align}
> $$

Asymptotically, the [[Likelihood Function]] is maximized at the true value $\theta_0$, which motivates estimating $\theta_0$ by the maximizer of $L$ ([[Maximum Likelihood Estimation]]) and comparing likelihoods in the [[Likelihood Ratio Test]].

Proof idea: $L(\theta_0) > L(\theta)$ iff $\frac{1}{n}\sum_i \log\frac{f(X_i; \theta)}{f(X_i; \theta_0)} < 0$. By the [[Weak Law of Large Numbers]] the average converges to $E_{\theta_0}\left[\log\frac{f(X; \theta)}{f(X; \theta_0)}\right]$, and by [[Jensen's Inequality]] (log is strictly concave, and (R0) makes the ratio nonconstant) this is $< \log E_{\theta_0}\left[\frac{f(X; \theta)}{f(X; \theta_0)}\right] = \log 1 = 0$, using (R1) for the last equality.

# Properties
- The limit $-E_{\theta_0}[\log f(X;\theta)/f(X;\theta_0)]$ is the [[Kullback-Leibler Divergence]] $\text{KL}(f_{\theta_0}\,\|\,f_\theta) > 0$: maximizing the average log-likelihood is asymptotically minimizing the KL divergence from the true distribution.
- The proof does not depend on $\theta$ being a scalar, so it holds for vector parameters.[^2]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=372)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=403)
