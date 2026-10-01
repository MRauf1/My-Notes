---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Predictive Distribution[^1][^2]
> The probability distribution over the target $t$ for a new input $\mathbf{x}$, given the training data $\mathbf{X}, \mathbf{t}$. A fully Bayesian treatment obtains it by consistently applying the sum and product rules, marginalizing over the parameters with respect to their posterior:
> $$
> \begin{align}
> p(t | \mathbf{x}, \mathbf{X}, \mathbf{t}) = \int p(t | \mathbf{x}, \mathbf{w})\, p(\mathbf{w} | \mathbf{X}, \mathbf{t})\, d\mathbf{w}
> \end{align}
> $$

A point-estimate method instead plugs in a single parameter value, e.g. $p(t | \mathbf{x}, \mathbf{w}_{\mathrm{ML}}, \beta_{\mathrm{ML}}) = \mathcal{N}(t | y(\mathbf{x}, \mathbf{w}_{\mathrm{ML}}), \beta_{\mathrm{ML}}^{-1})$ ([[Probabilistic Formulation of Regression]]). Including a prior but still maximizing ([[Maximum a Posteriori Learning|MAP]]) remains a point estimate and is not yet Bayesian; marginalizations like the integral above lie at the heart of Bayesian methods.[^3]

> [!abstract] Bayesian [[Linear Model]] Predictive Distribution[^2]
> For $y(\mathbf{x}, \mathbf{w}) = \mathbf{w}^T\boldsymbol{\phi}(\mathbf{x})$ with Gaussian noise of known precision $\beta$ and prior $\mathcal{N}(\mathbf{w} | \mathbf{0}, \alpha^{-1}\mathbf{I})$, the posterior is Gaussian and the predictive distribution is analytically
> $$
> \begin{align}
> p(t | \mathbf{x}, \mathbf{X}, \mathbf{t}) &= \mathcal{N}\big(t \,|\, m(\mathbf{x}), s^2(\mathbf{x})\big) \\
> m(\mathbf{x}) &= \beta\,\boldsymbol{\phi}(\mathbf{x})^T\mathbf{S}\sum_{n=1}^N \boldsymbol{\phi}(\mathbf{x}_n)\, t_n \\
> s^2(\mathbf{x}) &= \beta^{-1} + \boldsymbol{\phi}(\mathbf{x})^T\mathbf{S}\,\boldsymbol{\phi}(\mathbf{x}) \\
> \mathbf{S}^{-1} &= \alpha\mathbf{I} + \beta\sum_{n=1}^N \boldsymbol{\phi}(\mathbf{x}_n)\boldsymbol{\phi}(\mathbf{x}_n)^T
> \end{align}
> $$
> For polynomial curve fitting, $\phi_i(x) = x^i$ for $i = 0, \dots, M$.

# Properties
- Both the mean and the variance of the Bayesian predictive distribution depend on $\mathbf{x}$.[^4]
- The variance splits into two sources: $\beta^{-1}$ is the noise on the targets (already present in the maximum likelihood plug-in predictive), while $\boldsymbol{\phi}(\mathbf{x})^T\mathbf{S}\boldsymbol{\phi}(\mathbf{x})$ is the uncertainty in $\mathbf{w}$, which arises only from the Bayesian treatment and is largest where training data is sparse.[^4]
- Here $\alpha, \beta$ are fixed [[Hyperparameter|hyperparameters]]; a fuller treatment infers them from data as well.
- The mean $m(\mathbf{x})$ coincides with the prediction of the MAP (ridge) solution; the difference lies in the variance.
- General form (posterior predictive distribution): $p(\tilde{y} \mid y) = \int p(\tilde{y} \mid \theta)\, p(\theta \mid y)\, d\theta$, an average of conditional predictions over the [[Posterior Distribution]]; dropping $y$ from $p(\tilde{y} \mid \theta, y)$ uses the conditional independence of $y$ and $\tilde{y}$ given $\theta$. Its pre-data counterpart is the [[Prior Predictive Distribution]].[^5]
- Averaging over parameters rather than committing to one is what lets Bayesian models avoid [[Overfitting|over-fitting]] even when parameters outnumber data points.

[^1]: [Bishop, 2006, p. 31](zotero://open-pdf/library/items/5G99AZ8U?page=51&annotation=W4DVFWL2)
[^2]: [Bishop, 2006, p. 31](zotero://open-pdf/library/items/5G99AZ8U?page=51&annotation=FF38GDUR)
[^3]: [Bishop, 2006, p. 30](zotero://open-pdf/library/items/5G99AZ8U?page=50&annotation=84MJ5RRL)
[^4]: [Bishop, 2006, p. 31](zotero://open-pdf/library/items/5G99AZ8U?page=51&annotation=D9K9DJ8G)
[^5]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=5SYNH2BZ)
