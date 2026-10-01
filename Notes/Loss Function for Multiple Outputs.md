---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Loss Function for Multiple Outputs[^1]
> When the target $\mathbf{y}$ is a vector (e.g. [[Multivariate Regression|multivariate regression]], or a class at every pixel), it is usual to treat each prediction as [[Independent Random Variable|independent]], so the likelihood factorizes into univariate terms
> $$
> \begin{align}
> Pr(\mathbf{y} | \mathbf{f}[\mathbf{x}, \boldsymbol{\phi}]) = \prod_d Pr(y_d | \mathbf{f}_d[\mathbf{x}, \boldsymbol{\phi}])
> \end{align}
> $$
> where $\mathbf{f}_d[\mathbf{x}, \boldsymbol{\phi}]$ is the $d$-th set of network outputs, describing the parameters of the distribution over $y_d$.

# Properties
- The negative log-likelihood becomes a sum of per-output losses, $L[\boldsymbol{\phi}] = -\sum_i \sum_d \log[Pr(y_{id} | \mathbf{f}_d[\mathbf{x}_i, \boldsymbol{\phi}])]$ ([[Maximum Likelihood Loss Function Recipe]]).
- The same independence assumption is used to make two or more prediction types simultaneously (e.g. a regression and a classification output), adding their losses.
- The alternative is to model the outputs jointly with a multivariate distribution, such as a [[Multivariate Normal Distribution]], whose parameters the network predicts.

[^1]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
