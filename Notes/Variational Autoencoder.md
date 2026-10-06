---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Variational Autoencoder (VAE)[^1][^2]
> A neural architecture for learning a [[Nonlinear Latent Variable Model|nonlinear latent variable model]] $Pr(\mathbf{x}|\mathbf{z}, \boldsymbol{\phi}) = \mathrm{Norm}_{\mathbf{x}}[\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}], \sigma^2\mathbf{I}]$, $Pr(\mathbf{z}) = \mathrm{Norm}_{\mathbf{z}}[\mathbf{0}, \mathbf{I}]$ by maximizing a Monte Carlo estimate of the [[Evidence Lower Bound]]:
> - **Encoder** $\mathbf{g}[\mathbf{x}, \boldsymbol{\theta}]$: predicts the mean $\boldsymbol{\mu}$ and diagonal covariance $\boldsymbol{\Sigma}$ of the variational posterior $q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta}) = \mathrm{Norm}_{\mathbf{z}}[\boldsymbol{\mu}, \boldsymbol{\Sigma}]$ ([[Variational Inference|amortized variational inference]]).
> - **Sampling**: draw $\mathbf{z}^* \sim q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta})$ via the [[Reparameterization Trick|reparameterization trick]] $\mathbf{z}^* = \boldsymbol{\mu} + \boldsymbol{\Sigma}^{1/2}\boldsymbol{\epsilon}^*$, $\boldsymbol{\epsilon}^* \sim \mathrm{Norm}_{\boldsymbol{\epsilon}}[\mathbf{0}, \mathbf{I}]$.
> - **Decoder** $\mathbf{f}[\mathbf{z}^*, \boldsymbol{\phi}]$: gives the likelihood $Pr(\mathbf{x}|\mathbf{z}^*, \boldsymbol{\phi})$.
>
> The loss is the negative of
> $$
> \begin{align}
> \mathrm{ELBO}[\boldsymbol{\theta}, \boldsymbol{\phi}] &= \int q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta}) \log\left[Pr(\mathbf{x}|\mathbf{z}, \boldsymbol{\phi})\right] d\mathbf{z} - D_{KL}\left[q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta}) \,\|\, Pr(\mathbf{z})\right] \\
> &\approx \log\left[Pr(\mathbf{x}|\mathbf{z}^*, \boldsymbol{\phi})\right] - \frac{1}{2}\left(\mathrm{Tr}[\boldsymbol{\Sigma}] + \boldsymbol{\mu}^T\boldsymbol{\mu} - D_z - \log\left[\det[\boldsymbol{\Sigma}]\right]\right)
> \end{align}
> $$
> summed over the training examples, where $D_z$ is the latent dimension. The reconstruction term is a single-sample [[Monte Carlo Estimator|Monte Carlo estimate]] of an expectation under $q$, and the KL term is in closed form ([[Kullback-Leibler Divergence]]).

![[Variational Autoencoder.png]]

The two ELBO terms pull in different directions: the data example should have high probability under the decoder (reconstruction), and the variational distribution should stay similar to the prior.

The name is misleading: the VAE is not the model of $Pr(\mathbf{x})$ but the architecture that helps learn it. After training, the model contains neither the "variational" nor the "autoencoder" parts; it is the decoder plus the prior.[^1]

# Properties
- **Probabilistic but no exact likelihood**: a [[Probabilistic Generative Model|probabilistic generative model]], unlike a [[Generative Adversarial Network|GAN]], but the probability of a new example cannot be evaluated exactly, unlike a [[Normalizing Flow|normalizing flow]].[^1]
- **Monte Carlo ELBO**: for any $a[\bullet]$, $\mathbb{E}_{q}[a[\mathbf{z}]] = \int a[\mathbf{z}]\,q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta})\,d\mathbf{z} \approx \frac{1}{N}\sum_{n=1}^N a[\mathbf{z}_n^*]$ with $\mathbf{z}_n^* \sim q$; a single sample already gives a usable (very approximate) estimate.[^3]
- **Likelihood by importance sampling**: since $Pr(\mathbf{x}) = \mathbb{E}_{Pr(\mathbf{z})}[Pr(\mathbf{x}|\mathbf{z})]$, one could average $Pr(\mathbf{x}|\mathbf{z}_n)$ over $\mathbf{z}_n \sim Pr(\mathbf{z})$, but by the [[Curse of Dimensionality|curse of dimensionality]] almost every draw has negligible $Pr(\mathbf{x}|\mathbf{z}_n)$. Instead sample from an auxiliary $q(\mathbf{z})$ and reweight ([[Monte Carlo Estimator]]):[^4]
$$
\begin{align}
Pr(\mathbf{x}) = \int \frac{Pr(\mathbf{x}|\mathbf{z})Pr(\mathbf{z})}{q(\mathbf{z})}\,q(\mathbf{z})\,d\mathbf{z} = \mathbb{E}_{q(\mathbf{z})}\left[\frac{Pr(\mathbf{x}|\mathbf{z})Pr(\mathbf{z})}{q(\mathbf{z})}\right] \approx \frac{1}{N}\sum_{n=1}^N \frac{Pr(\mathbf{x}|\mathbf{z}_n)Pr(\mathbf{z}_n)}{q(\mathbf{z}_n)}, \qquad \mathbf{z}_n \sim q(\mathbf{z})
\end{align}
$$
  The integrand $Pr(\mathbf{x}|\mathbf{z})Pr(\mathbf{z})$ is proportional to the posterior $Pr(\mathbf{z}|\mathbf{x})$, which is the [[Optimal Importance Sampling Distribution|optimal importance sampling distribution]], so the encoder's $q(\mathbf{z}|\mathbf{x})$ is a sensible choice. With enough samples this beats the lower bound, and can be used for the [[Test Likelihood|test likelihood]] or for [[Novelty Detection|anomaly detection]].[^5]
- **Sample generation**: [[Ancestral Sampling|ancestral sampling]] from the prior, through the decoder, plus noise. Vanilla VAE samples are generally low quality, due to the naive spherical Gaussian noise model and the Gaussian prior and variational posterior.[^6]
- **Aggregated posterior**: sampling $\mathbf{z}$ from $q(\mathbf{z}|\boldsymbol{\theta}) = \frac{1}{I}\sum_i q(\mathbf{z}|\mathbf{x}_i, \boldsymbol{\theta})$, a [[Mixture of Gaussians]] that better represents the true latent distribution than the prior, improves generation quality.[^6]
- **Modern VAEs** reach high sample quality only with hierarchical priors and specialized architectures and regularization. [[Diffusion Model|Diffusion models]] can be viewed as VAEs with hierarchical priors.[^6]
- **Resynthesis**: encoding data, possibly modifying the latent, and decoding again. Also possible with normalizing flows and GANs, but a GAN has no encoder and needs a separate search for the latent ([[GAN Inversion]]).[^7]
- **Disentanglement**: the latent space is disentangled when each dimension represents an independent real-world factor ([[Generative Model Desiderata]]).[^8]
- **Failure mode**: [[Posterior Collapse|posterior collapse]], where the encoder always predicts the prior.

[^1]: [Prince, p. 327](zotero://open-pdf/library/items/BWT7FYX5?page=341&annotation=X4S3BA6Z); [Prince, p. 334](zotero://open-pdf/library/items/BWT7FYX5?page=348&annotation=AMFU5HZB)
[^2]: [Prince, p. 336](zotero://open-pdf/library/items/BWT7FYX5?page=350&annotation=XNTW7HL8); [Prince, p. 338](zotero://open-pdf/library/items/BWT7FYX5?page=352&annotation=MCBZG8I3)
[^3]: [Prince, p. 337](zotero://open-pdf/library/items/BWT7FYX5?page=351&annotation=2QERDKHE)
[^4]: [Prince, p. 340](zotero://open-pdf/library/items/BWT7FYX5?page=354&annotation=Y6ARSZRD)
[^5]: [Prince, p. 341](zotero://open-pdf/library/items/BWT7FYX5?page=355&annotation=7LHXYKLG)
[^6]: [Prince, p. 341](zotero://open-pdf/library/items/BWT7FYX5?page=355&annotation=BFAV7JNP); [Prince, p. 342](zotero://open-pdf/library/items/BWT7FYX5?page=356&annotation=7CERUZ8W)
[^7]: [Prince, p. 342](zotero://open-pdf/library/items/BWT7FYX5?page=356&annotation=ZSUB3U6L)
[^8]: [Prince, p. 342](zotero://open-pdf/library/items/BWT7FYX5?page=356&annotation=SBJVEB9D)
