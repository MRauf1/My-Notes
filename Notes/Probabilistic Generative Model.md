---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Probabilistic Generative Model[^1]
> A [[Generative Model|generative model]] that, besides generating new examples, assigns a probability $Pr(\mathbf{x} | \boldsymbol{\phi})$ to every data point $\mathbf{x}$, depending on the model parameters $\boldsymbol{\phi}$. It is trained by [[Maximum Likelihood Learning|maximizing the likelihood]] of the observed data $\{\mathbf{x}_i\}_{i=1}^I$, i.e. minimizing the sum of negative log-likelihoods:
> $$
> \begin{align}
> L[\boldsymbol{\phi}] = -\sum_{i=1}^{I} \log\left[Pr(\mathbf{x}_i | \boldsymbol{\phi})\right]
> \end{align}
> $$

![[Fitting Generative Models.png]]

# Types
- [[Normalizing Flow|Normalizing flows]], [[Variational Autoencoder|variational autoencoders]], and [[Diffusion Model|diffusion models]]: latent-variable based.[^1]
- [[Autoregressive Language Model|Autoregressive models]] such as the [[Transformer Decoder|transformer decoder]]: learned without labels, generate new examples, and assign probabilities to them, but rely on an autoregressive factorization rather than [[Latent Variables|latent variables]].[^2]

# Properties
- Since a probability distribution must integrate to one, raising the probability of the observed data implicitly lowers the probability of examples far from it.[^1]
- Equivalent to minimizing the [[Kullback-Leibler Divergence]] from the empirical data distribution, i.e. [[Density Estimation|density estimation]].
- The assigned probability is useful in its own right: the probability of a test set compares models quantitatively ([[Test Likelihood]]), and thresholding the probability of an example decides whether it is an outlier ([[Novelty Detection]]).[^1]
- Contrasts with [[Generative Adversarial Network|generative adversarial networks]], which only provide a sampling mechanism and are trained so that samples become indistinguishable from real examples, without assigning probabilities.

[^1]: [Prince, p. 270](zotero://open-pdf/library/items/BWT7FYX5?page=284&annotation=S4SB7AKD)
[^2]: [Prince, p. 270](zotero://open-pdf/library/items/BWT7FYX5?page=284&annotation=U59U97JN)
