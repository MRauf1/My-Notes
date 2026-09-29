---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Density Estimation[^1]
> The [[Unsupervised Learning|unsupervised learning]] problem of modelling the unknown probability distribution $p(\mathbf{x})$ of the data within the input space, given only a finite set of observations $\mathbf{x}_1, \dots, \mathbf{x}_N$ drawn from it.

# Properties
- Fitting a parametric model $q(\mathbf{x} | \boldsymbol{\theta})$ by minimizing the [[Kullback-Leibler Divergence]] $\mathrm{KL}(p \| q)$ is, after approximating the expectation over $p$ by the sample average, equivalent to [[Maximum Likelihood Estimation|maximum likelihood]].[^2]
- Intimately related to data compression: by the [[Noiseless Coding Theorem]] the most efficient code is achieved with the true distribution, and coding with an approximation $q$ costs, on average, an extra $\mathrm{KL}(p \| q)$ nats per symbol.[^2]
- A [[Generative Model|generative model]] of the inputs is a density estimate, and it enables [[Novelty Detection|novelty detection]] via the marginal $p(\mathbf{x})$.
- Naive non-parametric approaches that divide the input space into cells suffer from the [[Curse of Dimensionality]].
- Nonparametric estimators: the [[Histogram]] and [[Kernel Density Estimation]].

[^1]: [Bishop, 2006, p. 3](zotero://open-pdf/library/items/5G99AZ8U?page=23&annotation=FBYN8VEI)
[^2]: [Bishop, 2006, p. 57](zotero://open-pdf/library/items/5G99AZ8U?page=77&annotation=ZLT8Z9K5)
