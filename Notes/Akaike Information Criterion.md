---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Akaike Information Criterion (AIC)[^1]
> Among candidate models, choose the one for which
> $$
> \begin{align}
> \ln p(\mathcal{D} | \mathbf{w}_{\mathrm{ML}}) - M
> \end{align}
> $$
> is largest, where $\ln p(\mathcal{D} | \mathbf{w}_{\mathrm{ML}})$ is the best-fit log likelihood and $M$ is the number of adjustable parameters. Equivalently, minimize $\mathrm{AIC} = 2M - 2\ln p(\mathcal{D} | \mathbf{w}_{\mathrm{ML}})$.

An information criterion: it attempts to correct for the bias of [[Maximum Likelihood Estimation|maximum likelihood]] by adding a penalty term that compensates for the [[Overfitting|over-fitting]] of more complex models.

# Types
- **Bayesian information criterion (BIC)**: $\ln p(\mathcal{D} | \mathbf{w}_{\mathrm{ML}}) - \frac{1}{2} M \ln N$, a large-$N$ approximation to the log model evidence, whose penalty grows with the data set size $N$.

# Properties
- Used for [[Model Selection]] from the training data alone, avoiding the repeated training runs of [[Cross-Validation]].
- Does not account for uncertainty in the model parameters, and in practice tends to favour overly simple models.[^1]
- Counts raw parameters, but the number of parameters is not necessarily the right measure of model complexity; fully Bayesian model comparison derives the complexity penalty in a principled way instead.

[^1]: [Bishop, 2006, p. 33](zotero://open-pdf/library/items/5G99AZ8U?page=53&annotation=KVBT894F)
