---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] EM Algorithm[^1][^2]
> Let $\mathbf{X} = (X_1, \dots, X_{n_1})^T$ be observed and $\mathbf{Z} = (Z_1, \dots, Z_{n_2})^T$ unobserved (missing or [[Latent Variables|latent]]), with $g(\mathbf{x}|\theta)$ the pdf of $\mathbf{X}$, $h(\mathbf{x}, \mathbf{z}|\theta)$ the joint pdf, and $k(\mathbf{z}|\theta, \mathbf{x}) = h(\mathbf{x}, \mathbf{z}|\theta)/g(\mathbf{x}|\theta)$ the [[Conditional Distribution|conditional pdf]] of the missing data. The observed likelihood is $L(\theta|\mathbf{x}) = g(\mathbf{x}|\theta)$ and the complete likelihood is $L^c(\theta|\mathbf{x}, \mathbf{z}) = h(\mathbf{x}, \mathbf{z}|\theta)$. Starting from an initial estimate $\hat{\theta}^{(0)}$, iterate:
> 1. Expectation step: compute
> $$
> \begin{align}
> Q(\theta|\hat{\theta}^{(m)}, \mathbf{x}) = E_{\hat{\theta}^{(m)}}\left[\log L^c(\theta|\mathbf{x}, \mathbf{Z}) \,\middle|\, \hat{\theta}^{(m)}, \mathbf{x}\right]
> \end{align}
> $$
> where the expectation is under $k(\mathbf{z}|\hat{\theta}^{(m)}, \mathbf{x})$.
> 2. Maximization step: $\hat{\theta}^{(m+1)} = \operatorname{Argmax}_\theta Q(\theta|\hat{\theta}^{(m)}, \mathbf{x})$.

The goal is to maximize the observed [[Likelihood Function|likelihood]], which is often intractable, by repeatedly maximizing the complete likelihood, which is often easy, with the missing data filled in by their conditional expectation. The basic identity, for any fixed $\theta_0$, is
$$
\begin{align}
\log L(\theta|\mathbf{x}) = \underbrace{E_{\theta_0}[\log L^c(\theta|\mathbf{x}, \mathbf{Z})|\theta_0, \mathbf{x}]}_{Q(\theta|\theta_0, \mathbf{x})} - E_{\theta_0}[\log k(\mathbf{Z}|\theta, \mathbf{x})|\theta_0, \mathbf{x}]
\end{align}
$$
obtained by averaging $\log g = \log h - \log k$ over $k(\mathbf{z}|\theta_0, \mathbf{x})$.

> [!abstract] Theorem 1 (Monotonicity)[^3]
> The EM iterates satisfy $L(\hat{\theta}^{(m+1)}|\mathbf{x}) \geq L(\hat{\theta}^{(m)}|\mathbf{x})$.

Proof: the M step gives $Q(\hat{\theta}^{(m+1)}) \geq Q(\hat{\theta}^{(m)})$, and by [[Jensen's Inequality]] the second term of the identity, $-E_{\theta_0}[\log k(\mathbf{Z}|\theta, \mathbf{x})]$, is minimized at $\theta = \theta_0 = \hat{\theta}^{(m)}$ (the difference is a [[Kullback-Leibler Divergence]] $\geq 0$). So both parts of the identity move the log-likelihood up.

# Properties
- Under strong assumptions $\hat{\theta}^{(m)}$ converges to the [[Maximum Likelihood Estimation|maximum likelihood estimate]] as $m \to \infty$; in general it converges only to a stationary point (possibly a local maximum or saddle), so the result depends on the initialization.
- Geometrically, the E step builds a lower bound on $\log L$ that touches it at the current estimate, and the M step maximizes that bound (a minorize-maximize algorithm).
- Convergence is typically linear and can be slow when a large fraction of the information is missing.
- Standard applications: censored data, fitting [[Mixture Distribution|mixture models]] (e.g. Gaussian mixtures, where $\mathbf{Z}$ is the component label), and hidden Markov models.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=420)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=421)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=422)
