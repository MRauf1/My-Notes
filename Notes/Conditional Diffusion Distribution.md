---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Conditional Diffusion Distribution[^1][^2]
> The distribution of the previous latent $\mathbf{z}_{t-1}$ of the [[Diffusion Forward Process|diffusion forward process]] given both the current latent $\mathbf{z}_t$ and the clean data $\mathbf{x}$:
> $$
> \begin{align}
> q(\mathbf{z}_{t-1}|\mathbf{z}_t, \mathbf{x}) = \mathrm{Norm}_{\mathbf{z}_{t-1}}\left[\frac{1-\alpha_{t-1}}{1-\alpha_t}\sqrt{1-\beta_t}\,\mathbf{z}_t + \frac{\sqrt{\alpha_{t-1}}\,\beta_t}{1-\alpha_t}\,\mathbf{x},\; \frac{\beta_t(1-\alpha_{t-1})}{1-\alpha_t}\mathbf{I}\right]
> \end{align}
> $$
> *Derivation.* By [[Bayes' Theorem]] and the Markov property $q(\mathbf{z}_t|\mathbf{z}_{t-1}, \mathbf{x}) = q(\mathbf{z}_t|\mathbf{z}_{t-1})$,
> $$
> \begin{align}
> q(\mathbf{z}_{t-1}|\mathbf{z}_t, \mathbf{x}) &= \frac{q(\mathbf{z}_t|\mathbf{z}_{t-1}, \mathbf{x})\,q(\mathbf{z}_{t-1}|\mathbf{x})}{q(\mathbf{z}_t|\mathbf{x})} \propto q(\mathbf{z}_t|\mathbf{z}_{t-1})\,q(\mathbf{z}_{t-1}|\mathbf{x}) \\
> &= \mathrm{Norm}_{\mathbf{z}_t}\left[\sqrt{1-\beta_t}\,\mathbf{z}_{t-1}, \beta_t\mathbf{I}\right]\mathrm{Norm}_{\mathbf{z}_{t-1}}\left[\sqrt{\alpha_{t-1}}\,\mathbf{x}, (1-\alpha_{t-1})\mathbf{I}\right] \\
> &\propto \mathrm{Norm}_{\mathbf{z}_{t-1}}\left[\frac{1}{\sqrt{1-\beta_t}}\mathbf{z}_t, \frac{\beta_t}{1-\beta_t}\mathbf{I}\right]\mathrm{Norm}_{\mathbf{z}_{t-1}}\left[\sqrt{\alpha_{t-1}}\,\mathbf{x}, (1-\alpha_{t-1})\mathbf{I}\right]
> \end{align}
> $$
> using the Gaussian change of variables identity to rewrite the first factor as a density in $\mathbf{z}_{t-1}$, then the product identity to combine the two ([[Multivariate Normal Density Product]]). The proportionality constants must cancel since the result is a normalized distribution.

# Properties
- **Tractable vs intractable reverse**: the unconditioned reverse $q(\mathbf{z}_{t-1}|\mathbf{z}_t) = q(\mathbf{z}_t|\mathbf{z}_{t-1})q(\mathbf{z}_{t-1})/q(\mathbf{z}_t)$ is intractable because the marginal $q(\mathbf{z}_{t-1})$ is unknown ([[Diffusion Kernel]]); conditioning on $\mathbf{x}$ replaces it by the normal $q(\mathbf{z}_{t-1}|\mathbf{x})$.[^3]
- Normal because both factors are normal in $\mathbf{z}_{t-1}$; this is a statement about the encoder only and says nothing about the data distribution.
- **Training target**: available at training time since $\mathbf{x}$ is known. Its mean is the target for the decoder mean $\mathbf{f}_t[\mathbf{z}_t, \boldsymbol{\phi}_t]$ in the KL terms of the ELBO ([[Diffusion Model Loss Function]]).[^1]
- Averaging over the posterior of $\mathbf{x}$ recovers the true reverse step, $q(\mathbf{z}_{t-1}|\mathbf{z}_t) = \int q(\mathbf{z}_{t-1}|\mathbf{z}_t, \mathbf{x})\,q(\mathbf{x}|\mathbf{z}_t)\,d\mathbf{x}$, a [[Mixture of Gaussians|mixture of Gaussians]] that is multimodal in general.
- The variance $\tilde{\beta}_t = \beta_t(1-\alpha_{t-1})/(1-\alpha_t) \le \beta_t$; the choices $\sigma_t^2 = \beta_t$ and $\sigma_t^2 = \tilde{\beta}_t$ are the usual fixed decoder variances.

[^1]: [Prince, p. 354](zotero://open-pdf/library/items/BWT7FYX5?page=368&annotation=JE4EICIA)
[^2]: [Prince, p. 356](zotero://open-pdf/library/items/BWT7FYX5?page=370&annotation=XA24XYDT)
[^3]: [Prince, p. 354](zotero://open-pdf/library/items/BWT7FYX5?page=368&annotation=868QPHRF)
