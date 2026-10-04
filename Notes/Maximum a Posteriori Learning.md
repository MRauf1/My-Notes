---
tags:
  - computer_science
  - deep_learning
---

# Definition

> [!info] Definition
> $$
> \begin{align}
> \underset{f}{\mathrm{\arg \max}} [p(f | \{\mathbf{x}^{(i)}, \mathbf{y}^{(i)}\}_{i=1}^N)] = \\
> = \underset{f}{\mathrm{\arg \max}} [p(\{\mathbf{y}^{(i)}\}_{i=1}^N | \{\mathbf{x}^{(i)}\}_{i=1}^N, f) p(f)]
> \end{align}
> $$

Learning using [[Maximum a Posteriori|MAP]].[^1] Trying to infer the hypothesis $f$ that assigns the highest [[Probability|probability]] to the data given some prior.

# Properties
- Prince's form: $\hat{\boldsymbol{\phi}} = \arg\max_{\boldsymbol{\phi}}\left[Pr(\boldsymbol{\phi})\prod_{i=1}^I Pr(\mathbf{y}_i | \mathbf{x}_i, \boldsymbol{\phi})\right]$; taking the negative log gives the negative log-likelihood plus $\lambda \cdot g[\boldsymbol{\phi}] = -\log[Pr(\boldsymbol{\phi})]$ ([[Regularization]]).[^3]
- [[Regularization]] can be derived as MAP learning: the data-fit loss (e.g., $L_2$ loss) plays the role of the negative log likelihood, and the regularizer plays the role of the negative log prior, so that minimizing (loss + regularizer) is equivalent to maximizing (likelihood × prior).

- Still a point estimate of the parameters, so not yet a fully Bayesian treatment, which would marginalize over them ([[Predictive Distribution]]).[^2]
- Compared with maximum likelihood in [[Maximum Likelihood vs Maximum a Posteriori Estimation]].

[^1]: https://visionbook.mit.edu/intro_to_learning.html
[^2]: [Bishop, 2006, p. 30](zotero://open-pdf/library/items/5G99AZ8U?page=50&annotation=84MJ5RRL)
[^3]: [Prince, p. 139](zotero://open-pdf/library/items/BWT7FYX5?page=153&annotation=ZZLTDSU4); [Prince, p. 140](zotero://open-pdf/library/items/BWT7FYX5?page=154&annotation=I48FKEB2)
