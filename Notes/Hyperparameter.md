---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Hyperparameter[^1]
> A variable that controls the distribution of the model parameters (or, more broadly, the model's complexity) rather than being one of the parameters themselves. E.g. the precision $\alpha$ of a Gaussian prior $p(\mathbf{w} | \alpha) = \mathcal{N}(\mathbf{w} | \mathbf{0}, \alpha^{-1}\mathbf{I})$.

# Properties
- Examples include the regularization coefficient $\lambda$ of [[Regularization]], the polynomial order $M$, and the prior and noise precisions $\alpha, \beta$; for [[L2 Regularization]] derived as MAP, $\lambda = \alpha / \beta$.
- Not fitted by maximizing the training likelihood (which would always favour maximal complexity), but set by [[Model Selection]]: a [[Validation Set]], [[Cross-Validation]], information criteria like the [[Akaike Information Criterion]], or, in a fully Bayesian treatment, by inference from the data itself.
- Searching combinations of several hyperparameters by cross-validation can require a number of training runs exponential in the number of hyperparameters.[^2]

[^1]: [Bishop, 2006, p. 30](zotero://open-pdf/library/items/5G99AZ8U?page=50&annotation=KQLPNKN2)
[^2]: [Bishop, 2006, p. 33](zotero://open-pdf/library/items/5G99AZ8U?page=53&annotation=B95CXRC2)
