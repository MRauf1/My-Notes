---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Model Selection (Model Comparison)[^1]
> The problem of choosing between models of different complexity, or setting a model's complexity [[Hyperparameter|hyperparameters]] (e.g. the order $M$ of a polynomial or the regularization coefficient $\lambda$), so as to obtain the best predictive performance on unseen data.

Training-set performance cannot be used for this, since under [[Maximum Likelihood Estimation|maximum likelihood]] it improves monotonically with complexity and is a poor indicator of performance on new data due to [[Overfitting|over-fitting]].[^2]

# Types
- Hold-out: train on one part of the data and select on a separate [[Validation Set]]; with heavy iteration, a third test set is also kept aside.
- [[Cross-Validation]], which re-uses all the data for both training and assessment.
- Information criteria, such as the [[Akaike Information Criterion]] and the Bayesian information criterion, which penalize the training log likelihood by a complexity term.
- Fully Bayesian model comparison, in which complexity penalties arise naturally from marginalizing over the parameters ([[Bayesian Occam's Razor]]).

# Properties
- Ideally, a selection criterion depends only on the training data, allows many hyperparameters and model types to be compared in a single training run, and does not suffer from the bias of maximum likelihood.[^3]

[^1]: [Bishop, 2006, p. 6](zotero://open-pdf/library/items/5G99AZ8U?page=26&annotation=WFS53N69)
[^2]: [Bishop, 2006, p. 32](zotero://open-pdf/library/items/5G99AZ8U?page=52&annotation=SWB3LAH4)
[^3]: [Bishop, 2006, p. 33](zotero://open-pdf/library/items/5G99AZ8U?page=53&annotation=B95CXRC2)
