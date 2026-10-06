---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Latent Variable Model[^1]
> An indirect description of a distribution $Pr(\mathbf{x})$ over a multi-dimensional variable $\mathbf{x}$: model instead the joint distribution $Pr(\mathbf{x}, \mathbf{z})$ of the data $\mathbf{x}$ and an unobserved [[Latent Variables|latent variable]] $\mathbf{z}$, and recover $Pr(\mathbf{x})$ by [[Marginal Distribution|marginalization]]. Factoring the joint by [[Conditional Probability|conditional probability]] into the likelihood $Pr(\mathbf{x}|\mathbf{z})$ and the prior $Pr(\mathbf{z})$,
> $$
> \begin{align}
> Pr(\mathbf{x}) = \int Pr(\mathbf{x}, \mathbf{z})\,d\mathbf{z} = \int Pr(\mathbf{x}|\mathbf{z})\,Pr(\mathbf{z})\,d\mathbf{z}
> \end{align}
> $$
> with a sum in place of the integral when $\mathbf{z}$ is discrete.

The point of the indirection is that relatively simple expressions for $Pr(\mathbf{x}|\mathbf{z})$ and $Pr(\mathbf{z})$ can define a complex $Pr(\mathbf{x})$. The marginal is a [[Mixture Distribution|(compound) mixture]] of the conditionals $Pr(\mathbf{x}|\mathbf{z})$ weighted by the prior.

# Types
- [[Mixture of Gaussians]]: discrete $z$ with a categorical prior and normal likelihoods.[^2]
- [[Nonlinear Latent Variable Model]]: continuous, lower-dimensional $\mathbf{z}$ whose normal likelihood has a mean given by a deep network; learned with a [[Variational Autoencoder]].[^3]

# Properties
- New examples are drawn by [[Ancestral Sampling|ancestral sampling]]: $\mathbf{z}^* \sim Pr(\mathbf{z})$, then $\mathbf{x}^* \sim Pr(\mathbf{x}|\mathbf{z}^*)$.
- The posterior $Pr(\mathbf{z}|\mathbf{x}) = Pr(\mathbf{x}|\mathbf{z})Pr(\mathbf{z})/Pr(\mathbf{x})$ ([[Bayes' Theorem]]) indicates which latent values could have been responsible for a data point; its denominator is the evidence, so it is intractable whenever the marginal is.[^4]
- [[Maximum Likelihood Learning|Maximum likelihood]] requires $\log Pr(\mathbf{x})$, which for continuous nonlinear models has no closed form. It is instead lower bounded by the [[Evidence Lower Bound]], which is maximized by the [[Expectation-Maximization Algorithm|EM algorithm]] (exact posterior) or by [[Variational Inference|variational inference]] (approximate posterior).
- [[Normalizing Flow|Normalizing flows]] are latent variable models with a deterministic, invertible likelihood and $\dim \mathbf{z} = \dim \mathbf{x}$, which makes the marginal exact.

[^1]: [Prince, p. 327](zotero://open-pdf/library/items/BWT7FYX5?page=341&annotation=DZZZT6PE); [Prince, p. 328](zotero://open-pdf/library/items/BWT7FYX5?page=342&annotation=VE37D85D)
[^2]: [Prince, p. 328](zotero://open-pdf/library/items/BWT7FYX5?page=342&annotation=3UEEC82V)
[^3]: [Prince, p. 328](zotero://open-pdf/library/items/BWT7FYX5?page=342&annotation=P6C3HM95)
[^4]: [Prince, p. 334](zotero://open-pdf/library/items/BWT7FYX5?page=348&annotation=72IX7JAJ); [Prince, p. 336](zotero://open-pdf/library/items/BWT7FYX5?page=350&annotation=GYK93GUD)
