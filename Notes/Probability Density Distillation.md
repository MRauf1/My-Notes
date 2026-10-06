---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Probability Density Distillation[^1]
> Training a [[Normalizing Flow|normalizing flow]] $Pr(\mathbf{x} | \boldsymbol{\phi})$ (the **student**) to approximate a target density $q(\mathbf{x})$ (the **teacher**) that is easy to evaluate but hard to sample from. Samples $\mathbf{x}_i = \mathbf{f}[\mathbf{z}_i, \boldsymbol{\phi}]$ are drawn from the student and the reverse [[Kullback-Leibler Divergence]] to the teacher is minimized:
> $$
> \begin{align}
> \hat{\boldsymbol{\phi}} = \underset{\boldsymbol{\phi}}{\operatorname{argmin}}\left[\mathrm{KL}\left[\frac{1}{I}\sum_{i=1}^I \delta\left[\mathbf{x} - \mathbf{f}[\mathbf{z}_i, \boldsymbol{\phi}]\right] \,\middle\|\, q(\mathbf{x})\right]\right]
> \end{align}
> $$
> In practice this is $\mathbb{E}_{\mathbf{z}}\left[\log Pr(\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}] | \boldsymbol{\phi}) - \log q(\mathbf{f}[\mathbf{z}, \boldsymbol{\phi}])\right]$, i.e. matching student and teacher likelihoods on the student's own samples.

# Properties
- **No inversion needed**: the latents $\mathbf{z}_i$ of self-generated samples are known, so the student's likelihood is computed in the forward direction. The student can therefore be a flow whose inversion is slow, e.g. an inverse [[Autoregressive Flow|autoregressive flow]] distilled from a masked autoregressive flow teacher (Parallel WaveNet).[^1]
- **Contrast with ordinary training**: fitting a flow to samples $\mathbf{x}_i$ from an unknown distribution by [[Maximum Likelihood Learning|maximum likelihood]] minimizes the forward KL divergence from the empirical distribution, whose relevant part is the cross-entropy ([[Cross-Entropy Loss]]):[^1]
$$
\begin{align}
\hat{\boldsymbol{\phi}} = \underset{\boldsymbol{\phi}}{\operatorname{argmin}}\left[\mathrm{KL}\left[\frac{1}{I}\sum_{i=1}^I \delta[\mathbf{x} - \mathbf{x}_i] \,\middle\|\, Pr(\mathbf{x} | \boldsymbol{\phi})\right]\right]
\end{align}
$$
- Reverse KL is mode-seeking: the student is penalized for placing mass where $q$ is small, but not for missing modes of $q$.
- The same trick lets normalizing flows model the approximate posterior in [[Variational Autoencoder|VAEs]].[^1]

[^1]: [Prince, p. 321](zotero://open-pdf/library/items/BWT7FYX5?page=335&annotation=JFADEZRS); [Prince, p. 321](zotero://open-pdf/library/items/BWT7FYX5?page=335&annotation=69BRXLVQ); [Prince, p. 314](zotero://open-pdf/library/items/BWT7FYX5?page=328&annotation=QWYLYBD3)
