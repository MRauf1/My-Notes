---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Reparameterization Trick[^1]
> To backpropagate through a sampling step $\mathbf{z}^* \sim \mathrm{Norm}_{\mathbf{z}}[\boldsymbol{\mu}, \boldsymbol{\Sigma}]$ whose parameters are computed by the network, move the randomness into a separate branch that draws parameter-free noise and transform it deterministically:
> $$
> \begin{align}
> \boldsymbol{\epsilon}^* \sim \mathrm{Norm}_{\boldsymbol{\epsilon}}[\mathbf{0}, \mathbf{I}], \qquad \mathbf{z}^* = \boldsymbol{\mu} + \boldsymbol{\Sigma}^{1/2}\boldsymbol{\epsilon}^*
> \end{align}
> $$
> Then $\mathbf{z}^*$ is a differentiable function of $\boldsymbol{\mu}, \boldsymbol{\Sigma}$, and the [[Backpropagation|backpropagation]] algorithm never needs to pass down the stochastic branch.

> [!info] General Form
> If $\mathbf{z} \sim q(\mathbf{z}|\boldsymbol{\theta})$ can be written as $\mathbf{z} = \mathbf{t}[\boldsymbol{\epsilon}, \boldsymbol{\theta}]$ for noise $\boldsymbol{\epsilon} \sim p(\boldsymbol{\epsilon})$ that does not depend on $\boldsymbol{\theta}$, then
> $$
> \begin{align}
> \nabla_{\boldsymbol{\theta}}\, \mathbb{E}_{q(\mathbf{z}|\boldsymbol{\theta})}\left[a[\mathbf{z}]\right] = \mathbb{E}_{p(\boldsymbol{\epsilon})}\left[\nabla_{\boldsymbol{\theta}}\, a\left[\mathbf{t}[\boldsymbol{\epsilon}, \boldsymbol{\theta}]\right]\right] \approx \frac{1}{N}\sum_{n=1}^N \nabla_{\boldsymbol{\theta}}\, a\left[\mathbf{t}[\boldsymbol{\epsilon}_n, \boldsymbol{\theta}]\right]
> \end{align}
> $$
> by the [[Interchange of Differentiation and Expectation]], since the expectation is now over a fixed distribution.

![[Reparameterization Trick.png]]

# Properties
- Needed in the [[Variational Autoencoder]]: the encoder parameters $\boldsymbol{\theta}$ precede the sampling step, so their gradients must pass through it.[^1]
- The normal case is the [[Multivariate Normal Distribution Affine Transformation|affine transformation]] of a standard normal; any square root of $\boldsymbol{\Sigma}$ works, e.g. the Cholesky factor ([[Multivariate Normal Sampling (Cholesky Factorization)]]). With a diagonal $\boldsymbol{\Sigma}$ it is elementwise scaling by the standard deviations.
- Also called the *pathwise* gradient estimator; it typically has much lower variance than the score-function estimator $\mathbb{E}_q\left[a[\mathbf{z}]\,\nabla_{\boldsymbol{\theta}} \log q(\mathbf{z}|\boldsymbol{\theta})\right]$, which is the alternative when no such reparameterization exists (e.g. discrete $\mathbf{z}$).
- Requires $a[\mathbf{t}[\boldsymbol{\epsilon}, \boldsymbol{\theta}]]$ to be differentiable in $\boldsymbol{\theta}$; it is the same idea as [[Reparameterization (Differentiable Monte Carlo)|reparameterization in differentiable Monte Carlo]], which handles discontinuous integrands by moving them to fixed locations.

[^1]: [Prince, p. 339](zotero://open-pdf/library/items/BWT7FYX5?page=353&annotation=8CUGHIKA); [Prince, p. 339](zotero://open-pdf/library/items/BWT7FYX5?page=353&annotation=TNLFLVVV)
