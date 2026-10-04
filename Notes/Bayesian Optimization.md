---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Bayesian Optimization[^1]
> A framework for optimizing an expensive black-box objective (e.g. validation performance as a function of [[Hyperparameter|hyperparameters]]) that maintains a probabilistic surrogate model of the objective and its uncertainty, typically a Gaussian process, and chooses the next point to evaluate by trading off exploring where the uncertainty is high against exploiting regions where performance looks promising.

# Properties
- Applied to [[Hyperparameter Search]] by Snoek et al. (2012); better suited than random search for continuous hyperparameters.
- The next point is chosen by maximizing an acquisition function, such as expected improvement or an upper confidence bound, that combines the surrogate's mean and variance.[^2]
- An instance of the [[Exploration-Exploitation Tradeoff]].
- Variants with other surrogates: SMAC (random forests) and Tree-Parzen estimators, which handle discrete and conditional hyperparameters; combined with [[Hyperband]] in BOHB.

[^1]: [Prince, p. 135](zotero://open-pdf/library/items/BWT7FYX5?page=149&annotation=8V7CBB8K); [Prince, p. 136](zotero://open-pdf/library/items/BWT7FYX5?page=150&annotation=T2T8G9K2)
[^2]: Acquisition functions added from general knowledge.
