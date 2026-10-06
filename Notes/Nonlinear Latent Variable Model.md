---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Nonlinear Latent Variable Model[^1]
> A [[Latent Variable Model|latent variable model]] in which both the data $\mathbf{x}$ and the latent $\mathbf{z}$ are continuous and multivariate, with $\mathbf{z}$ lower dimensional than $\mathbf{x}$. The prior is a standard [[Multivariate Normal Distribution|multivariate normal]], and the likelihood is normal with spherical covariance and a mean given by a deep network $\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}]$:
> $$
> \begin{align}
> Pr(\mathbf{z}) &= \mathrm{Norm}_{\mathbf{z}}[\mathbf{0}, \mathbf{I}] \\
> Pr(\mathbf{x} | \mathbf{z}, \boldsymbol{\phi}) &= \mathrm{Norm}_{\mathbf{x}}\left[\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}], \sigma^2\mathbf{I}\right]
> \end{align}
> $$
> The data probability is the marginal
> $$
> \begin{align}
> Pr(\mathbf{x} | \boldsymbol{\phi}) = \int Pr(\mathbf{x}, \mathbf{z} | \boldsymbol{\phi})\,d\mathbf{z} = \int Pr(\mathbf{x} | \mathbf{z}, \boldsymbol{\phi}) \cdot Pr(\mathbf{z})\,d\mathbf{z} = \int \mathrm{Norm}_{\mathbf{x}}\left[\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}], \sigma^2\mathbf{I}\right] \cdot \mathrm{Norm}_{\mathbf{z}}[\mathbf{0}, \mathbf{I}]\,d\mathbf{z}
> \end{align}
> $$

The network $\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}]$ describes the important aspects of the data, and the remaining unmodeled aspects are ascribed to the noise $\sigma^2\mathbf{I}$. The marginal is an infinite weighted sum (an infinite mixture) of spherical Gaussians, with weights $Pr(\mathbf{z})$ and means $\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}]$: the continuous analogue of a [[Mixture of Gaussians]].

This is the model that a [[Variational Autoencoder|VAE]] actually learns: the final model of $Pr(\mathbf{x})$ contains neither the "variational" nor the "autoencoder" parts.[^2]

# Properties
- **Sampling**: by [[Ancestral Sampling|ancestral sampling]], draw $\mathbf{z}^* \sim Pr(\mathbf{z})$, pass it through $\mathbf{f}[\mathbf{z}^*, \boldsymbol{\phi}]$ to get the mean of $Pr(\mathbf{x}|\mathbf{z}^*, \boldsymbol{\phi})$, and draw $\mathbf{x}^*$ from it. Both distributions are normal, so this is straightforward.[^3]
- **Training is intractable**: [[Maximum Likelihood Learning|maximum likelihood]] (treating $\sigma^2$ as known)[^4]
$$
\begin{align}
\hat{\boldsymbol{\phi}} = \underset{\boldsymbol{\phi}}{\operatorname{argmax}}\left[\sum_{i=1}^I \log\left[Pr(\mathbf{x}_i | \boldsymbol{\phi})\right]\right], \qquad Pr(\mathbf{x}_i | \boldsymbol{\phi}) = \int \mathrm{Norm}_{\mathbf{x}_i}\left[\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}], \sigma^2\mathbf{I}\right] \cdot \mathrm{Norm}_{\mathbf{z}}[\mathbf{0}, \mathbf{I}]\,d\mathbf{z}
\end{align}
$$
  has no closed-form integral and no easy way to evaluate it for a given $\mathbf{x}$. Instead one maximizes the [[Evidence Lower Bound]] over $\boldsymbol{\phi}$ and the parameters $\boldsymbol{\theta}$ of an auxiliary distribution.
- **Posterior is intractable**: $Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi})$ requires the evidence $Pr(\mathbf{x}|\boldsymbol{\phi})$ in the denominator of [[Bayes' Theorem]], so it is approximated by [[Variational Inference|variational inference]].
- **Likelihood estimation**: naive [[Monte Carlo Estimator|Monte Carlo]] with $\mathbf{z}_n \sim Pr(\mathbf{z})$ fails due to the [[Curse of Dimensionality|curse of dimensionality]]; importance sampling with the encoder's variational posterior works ([[Variational Autoencoder]]).

[^1]: [Prince, p. 328](zotero://open-pdf/library/items/BWT7FYX5?page=342&annotation=P6C3HM95); [Prince, p. 329](zotero://open-pdf/library/items/BWT7FYX5?page=343&annotation=E2NZID2E)
[^2]: [Prince, p. 327](zotero://open-pdf/library/items/BWT7FYX5?page=341&annotation=X4S3BA6Z)
[^3]: [Prince, p. 329](zotero://open-pdf/library/items/BWT7FYX5?page=343&annotation=PERWBZVB)
[^4]: [Prince, p. 331](zotero://open-pdf/library/items/BWT7FYX5?page=345&annotation=4Y3PLVG2)
