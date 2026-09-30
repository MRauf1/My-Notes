---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Fisher Information]] [[Matrix]])
> Fisher Information matrix is a matrix, denoted as $I(\mathbf{\beta}) = - E[\nabla^2 L(\mathbf{\beta})]$, whose $jk$-th element is
> $$
> \begin{align}
> \iota(\mathbf{\beta})_{jk} = -E[\frac{\partial^2 L(\mathbf{\beta})}{\partial \beta_j \partial \beta_k}]
> \end{align}
> $$

> [!info] Definition 2 (Information Matrix of One Observation)[^1]
> For $\boldsymbol{\theta} \in \Omega \subseteq \mathbb{R}^p$, the Fisher information is the $p \times p$ [[Covariance Matrix]] of the gradient of $\log f(X; \boldsymbol{\theta})$:
> $$
> \begin{align}
> I(\boldsymbol{\theta}) = \text{Cov}\big(\nabla \log f(X; \boldsymbol{\theta})\big), \qquad I_{jk} = \text{Cov}\left(\frac{\partial \log f}{\partial\theta_j}, \frac{\partial \log f}{\partial\theta_k}\right) = -E\left[\frac{\partial^2 \log f(X; \boldsymbol{\theta})}{\partial\theta_j\,\partial\theta_k}\right]
> \end{align}
> $$
> For a random sample, $\text{Cov}(\nabla \log L(\boldsymbol{\theta}; \mathbf{X})) = nI(\boldsymbol{\theta})$.[^2]

# Properties
- The diagonal entry $I_{jj}(\boldsymbol{\theta}) = \text{Var}(\partial \log f/\partial\theta_j)$ is the information about $\theta_j$ when all other parameters are treated as known.[^3] The bound for an unbiased estimator of $\theta_j$ with the others unknown is $\frac{1}{n}[I^{-1}(\boldsymbol{\theta})]_{jj} \geq \frac{1}{nI_{jj}}$ ([[Rao-Cramér Lower Bound]]).
- If $I(\boldsymbol{\theta})$ is diagonal, not knowing the other parameters costs nothing (e.g. $\mu$ and $\sigma^2$ of the normal); for a location-scale family this happens when the underlying pdf is symmetric.[^3]
- Reparametrization $\boldsymbol{\eta} = g(\boldsymbol{\theta})$ with Jacobian $B$: $I(\boldsymbol{\eta}) = [BI^{-1}(\boldsymbol{\theta})B^T]^{-1}$ ([[Maximum Likelihood Estimator Asymptotic Normality]]).
- [[Fisher Information Matrix Relationship with Covariance Matrix]]

Fisher information measures how much the data constrains $\beta$ by quantifying the [[Curvature|curvature]] of the [[Log-Likelihood Function|log-likelihood]] $L(\beta)$ around its maximum: a log-likelihood that is sharply peaked (high curvature, large $I(\beta)$) means only a narrow range of $\beta$ values fit the data well, so the estimate is precise; a flat log-likelihood (low curvature, small $I(\beta)$) means many nearby values of $\beta$ are almost equally plausible, so the estimate is imprecise. This is why $I(\beta)^{-1}$ equals the [[Fisher Information Matrix Relationship with Covariance Matrix|estimator's asymptotic covariance]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=404)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=405)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=408)
