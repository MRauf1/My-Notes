---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Evidence Lower Bound (ELBO)[^1]
> For a [[Latent Variable Model|latent variable model]] $Pr(\mathbf{x}, \mathbf{z}|\boldsymbol{\phi})$ and any distribution $q(\mathbf{z}|\boldsymbol{\theta})$ over the latent variables,
> $$
> \begin{align}
> \log\left[Pr(\mathbf{x}|\boldsymbol{\phi})\right] \geq \mathrm{ELBO}[\boldsymbol{\theta}, \boldsymbol{\phi}] := \int q(\mathbf{z}|\boldsymbol{\theta}) \log\left[\frac{Pr(\mathbf{x}, \mathbf{z}|\boldsymbol{\phi})}{q(\mathbf{z}|\boldsymbol{\theta})}\right] d\mathbf{z}
> \end{align}
> $$
> *Proof.* Multiply and divide by $q$, then apply [[Jensen's Inequality]] to the concave $\log$:
> $$
> \begin{align}
> \log\left[Pr(\mathbf{x}|\boldsymbol{\phi})\right] = \log\left[\int q(\mathbf{z}|\boldsymbol{\theta}) \frac{Pr(\mathbf{x}, \mathbf{z}|\boldsymbol{\phi})}{q(\mathbf{z}|\boldsymbol{\theta})}\,d\mathbf{z}\right] \geq \int q(\mathbf{z}|\boldsymbol{\theta}) \log\left[\frac{Pr(\mathbf{x}, \mathbf{z}|\boldsymbol{\phi})}{q(\mathbf{z}|\boldsymbol{\theta})}\right] d\mathbf{z}
> \end{align}
> $$
> The name comes from $Pr(\mathbf{x}|\boldsymbol{\phi})$ being the *evidence* in [[Bayes' Theorem]].

> [!abstract] Three Equivalent Forms[^2][^3]
> $$
> \begin{align}
> \mathrm{ELBO}[\boldsymbol{\theta}, \boldsymbol{\phi}] &= \int q(\mathbf{z}|\boldsymbol{\theta}) \log\left[\frac{Pr(\mathbf{x}, \mathbf{z}|\boldsymbol{\phi})}{q(\mathbf{z}|\boldsymbol{\theta})}\right] d\mathbf{z} \\
> &= \log\left[Pr(\mathbf{x}|\boldsymbol{\phi})\right] - D_{KL}\left[q(\mathbf{z}|\boldsymbol{\theta}) \,\|\, Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi})\right] \\
> &= \underbrace{\int q(\mathbf{z}|\boldsymbol{\theta}) \log\left[Pr(\mathbf{x}|\mathbf{z}, \boldsymbol{\phi})\right] d\mathbf{z}}_{\text{reconstruction}} - \underbrace{D_{KL}\left[q(\mathbf{z}|\boldsymbol{\theta}) \,\|\, Pr(\mathbf{z})\right]}_{\text{distance to prior}}
> \end{align}
> $$
> The second follows by factoring $Pr(\mathbf{x}, \mathbf{z}|\boldsymbol{\phi}) = Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi})Pr(\mathbf{x}|\boldsymbol{\phi})$: the $\log Pr(\mathbf{x}|\boldsymbol{\phi})$ term does not depend on $\mathbf{z}$ and $q$ integrates to one. The third follows by factoring $Pr(\mathbf{x}, \mathbf{z}|\boldsymbol{\phi}) = Pr(\mathbf{x}|\mathbf{z}, \boldsymbol{\phi})Pr(\mathbf{z})$. Both use the definition of the [[Kullback-Leibler Divergence]].

![[Evidence Lower Bound.png]]

**Intuition.** For each fixed $\boldsymbol{\theta}$, the ELBO is a function of $\boldsymbol{\phi}$ lying everywhere below the log-likelihood. Changing $\boldsymbol{\theta}$ swaps in a different lower-bound curve, which may lie closer to or further from the log-likelihood; changing $\boldsymbol{\phi}$ moves along the current curve. The log-likelihood can therefore be raised by improving the ELBO in either set of parameters.[^4]

# Properties
- **Tightness**: since $D_{KL} \geq 0$ (Gibbs' inequality), the second form re-proves the bound and shows the gap is exactly $D_{KL}[q \,\|\, Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi})]$. The bound is tight (ELBO and log-likelihood coincide at fixed $\boldsymbol{\phi}$) if and only if $q(\mathbf{z}|\boldsymbol{\theta}) = Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi})$, the [[Posterior Distribution|posterior]] over the latents.[^2]
- **Optimizing $\boldsymbol{\theta}$** minimizes the KL divergence from $q$ to the true posterior, moving the bound upward; this is [[Variational Inference|variational inference]].[^5]
- **Reconstruction vs prior form**: the first term measures how well the latents explain the data (reconstruction accuracy) and the second how far $q$ is from the prior. This is the form computed by the [[Variational Autoencoder]].[^3]
- **Learning**: the [[Nonlinear Latent Variable Model]] is learned by maximizing the ELBO jointly in $\boldsymbol{\phi}$ and $\boldsymbol{\theta}$, since the log-likelihood itself is intractable.[^6]
- **Coordinate ascent**: alternately setting $q$ to the exact posterior (bound tight) and maximizing over $\boldsymbol{\phi}$ is the [[Expectation-Maximization Algorithm|EM algorithm]]; the ELBO with $q = Pr(\mathbf{z}|\mathbf{x}, \boldsymbol{\phi}_0)$ equals EM's $Q(\boldsymbol{\phi}|\boldsymbol{\phi}_0)$ plus the entropy of $q$.
- Reported in place of the [[Test Likelihood|test likelihood]] for VAEs and [[Diffusion Model|diffusion models]], whose exact likelihoods are unavailable.

[^1]: [Prince, p. 331](zotero://open-pdf/library/items/BWT7FYX5?page=345&annotation=GYDXKU9C); [Prince, p. 333](zotero://open-pdf/library/items/BWT7FYX5?page=347&annotation=TYLV95LJ)
[^2]: [Prince, p. 334](zotero://open-pdf/library/items/BWT7FYX5?page=348&annotation=72IX7JAJ)
[^3]: [Prince, p. 335](zotero://open-pdf/library/items/BWT7FYX5?page=349&annotation=WKPEVSXI); [Prince, p. 336](zotero://open-pdf/library/items/BWT7FYX5?page=350&annotation=54KPHGYN)
[^4]: [Prince, p. 334](zotero://open-pdf/library/items/BWT7FYX5?page=348&annotation=WBMDSI85); [Prince, p. 333](zotero://open-pdf/library/items/BWT7FYX5?page=347&annotation=5ILD8AW5)
[^5]: [Prince, p. 336](zotero://open-pdf/library/items/BWT7FYX5?page=350&annotation=GYK93GUD)
[^6]: [Prince, p. 334](zotero://open-pdf/library/items/BWT7FYX5?page=348&annotation=AMFU5HZB)
