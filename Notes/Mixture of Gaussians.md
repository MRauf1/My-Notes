---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Mixture of Gaussians (1D)[^1]
> A [[Latent Variable Model|latent variable model]] with a discrete latent $z \in \{1, \dots, N\}$ whose prior is a categorical distribution with one probability $\lambda_n$ per value, and whose likelihood given $z = n$ is normal:
> $$
> \begin{align}
> Pr(z = n) = \lambda_n, \qquad Pr(x | z = n) = \mathrm{Norm}_x\left[\mu_n, \sigma_n^2\right]
> \end{align}
> $$
> Marginalizing by summing over the values of $z$,
> $$
> \begin{align}
> Pr(x) = \sum_{n=1}^N Pr(x, z = n) = \sum_{n=1}^N Pr(x | z = n)\,Pr(z = n) = \sum_{n=1}^N \lambda_n \cdot \mathrm{Norm}_x\left[\mu_n, \sigma_n^2\right]
> \end{align}
> $$

> [!info] Mixture of Gaussians (Multivariate)
> For $\mathbf{x} \in \mathbb{R}^D$, the components are [[Multivariate Normal Distribution|multivariate normals]] with means $\boldsymbol{\mu}_n$ and covariances $\boldsymbol{\Sigma}_n$:
> $$
> \begin{align}
> Pr(\mathbf{x}) = \sum_{n=1}^N \lambda_n \cdot \mathrm{Norm}_{\mathbf{x}}\left[\boldsymbol{\mu}_n, \boldsymbol{\Sigma}_n\right], \qquad \lambda_n \geq 0, \quad \sum_{n=1}^N \lambda_n = 1
> \end{align}
> $$

Simple expressions for the prior and likelihood describe a complex, multi-modal distribution: the marginal is a weighted sum of Gaussian components, which is the marginalization of the joint $Pr(x, z)$ between continuous data and a discrete latent.

# Properties
- A finite [[Mixture Distribution]] whose components are normal.
- Classically fit by [[Maximum Likelihood Estimation|maximum likelihood]] using the [[Expectation-Maximization Algorithm|EM algorithm]], since the posterior over the discrete component label is tractable.
- The [[Nonlinear Latent Variable Model]] is its continuous analogue: an infinite mixture of spherical Gaussians whose means are produced by a network.
- The aggregated posterior of a [[Variational Autoencoder]] is a mixture of Gaussians in latent space.

[^1]: [Prince, p. 328](zotero://open-pdf/library/items/BWT7FYX5?page=342&annotation=3UEEC82V); [Prince, p. 329](zotero://open-pdf/library/items/BWT7FYX5?page=343&annotation=H42IM5EE)
