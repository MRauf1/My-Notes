---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Variational Inference (Variational Approximation)[^1]
> When the [[Posterior Distribution|posterior]] $Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi}) = Pr(\mathbf{x}|\mathbf{z}, \boldsymbol{\phi})Pr(\mathbf{z}) / Pr(\mathbf{x}|\boldsymbol{\phi})$ is intractable because the evidence $Pr(\mathbf{x}|\boldsymbol{\phi})$ cannot be evaluated, choose a simple parametric family $q(\mathbf{z}|\boldsymbol{\theta})$ and pick the member closest to the true posterior:
> $$
> \begin{align}
> \hat{\boldsymbol{\theta}} = \underset{\boldsymbol{\theta}}{\operatorname{argmin}}\; D_{KL}\left[q(\mathbf{z}|\boldsymbol{\theta}) \,\|\, Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi})\right] = \underset{\boldsymbol{\theta}}{\operatorname{argmax}}\; \mathrm{ELBO}[\boldsymbol{\theta}, \boldsymbol{\phi}]
> \end{align}
> $$
> The two problems are equivalent because $\mathrm{ELBO} = \log Pr(\mathbf{x}|\boldsymbol{\phi}) - D_{KL}[q \,\|\, Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi})]$ and the first term does not depend on $\boldsymbol{\theta}$ ([[Evidence Lower Bound]]); the ELBO never requires the evidence.

> [!info] Amortized Variational Inference[^1]
> Since the optimal $q$ is the posterior, which depends on the data example $\mathbf{x}$, let the approximation depend on $\mathbf{x}$ too, with a single network $\mathbf{g}[\mathbf{x}, \boldsymbol{\theta}]$ predicting its parameters for every example. With a [[Multivariate Normal Distribution|normal]] family with diagonal covariance,
> $$
> \begin{align}
> q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta}) = \mathrm{Norm}_{\mathbf{z}}\left[\mathbf{g}_{\boldsymbol{\mu}}[\mathbf{x}, \boldsymbol{\theta}], \mathbf{g}_{\boldsymbol{\Sigma}}[\mathbf{x}, \boldsymbol{\theta}]\right]
> \end{align}
> $$
> This is the encoder of the [[Variational Autoencoder]].

# Properties
- The chosen family will not always match the posterior well, but some parameter values match it better than others; the residual KL is the gap between the ELBO and the log-likelihood.[^1]
- Minimizes the *reverse* [[Kullback-Leibler Divergence]] $D_{KL}[q \,\|\, p]$, which is mode-seeking: $q$ is heavily penalized for putting mass where the posterior has little, so it tends to under-cover a multi-modal posterior.
- More expressive families, e.g. a [[Normalizing Flow|normalizing flow]] posterior, shrink the gap ([[Autoregressive Flow]], [[Probability Density Distillation]]).
- A deterministic, optimization-based alternative to sampling the posterior with [[Markov Chain Monte Carlo]].
- With the exact posterior in place of $q$, alternating updates reduce to the [[Expectation-Maximization Algorithm|EM algorithm]].

[^1]: [Prince, p. 336](zotero://open-pdf/library/items/BWT7FYX5?page=350&annotation=GYK93GUD)
