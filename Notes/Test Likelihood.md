---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Test Likelihood[^1]
> A metric comparing [[Probabilistic Generative Model|probabilistic generative models]] by the [[Likelihood Function|likelihood]] (in practice the log-likelihood) they assign to a held-out test dataset $\{\mathbf{x}_i^{\text{test}}\}$:
> $$
> \begin{align}
> \sum_{i} \log\left[Pr(\mathbf{x}_i^{\text{test}} | \boldsymbol{\phi})\right]
> \end{align}
> $$

# Properties
- Training likelihood is ineffective: a model can put very high probability on each training point and very low probability in between, attaining huge training likelihood while only reproducing the training data ([[Overfitting]]).[^1]
- Captures both [[Generalization|generalization]] and coverage: if the model concentrates probability on a subset of the data, it must assign lower probability elsewhere, so part of the test set receives low probability.
- Not applicable to [[Generative Adversarial Network|GANs]], which assign no probability.
- Expensive to estimate for [[Variational Autoencoder|VAEs]] and [[Diffusion Model|diffusion models]], though a lower bound on the log-likelihood is computable.
- [[Normalizing Flow|Normalizing flows]] are the only family for which it is computed exactly and efficiently.
- See also [[Inception Score]], [[Fréchet Inception Distance]], [[Manifold Precision and Recall]] ([[Generative Model Desiderata]]).

[^1]: [Prince, p. 272](zotero://open-pdf/library/items/BWT7FYX5?page=286&annotation=G3RHP8AP)
