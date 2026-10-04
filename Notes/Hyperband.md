---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Hyperband[^1]
> A multi-armed bandit strategy for [[Hyperparameter Search|hyperparameter optimization]] (Li et al., 2017). It assumes performance can be measured cheaply but approximately under a budget (e.g. a fixed number of training iterations). Random configurations are sampled and run until the budget is used; the best fraction $\eta$ of runs is kept, the budget is multiplied by /\eta$, and this is repeated until the maximum budget is reached.

# Properties
- Efficient because bad configurations are not run to completion.
- Inefficient in that configurations are chosen at random; **BOHB** (Falkner et al., 2018) replaces the random sampling with Tree-Parzen estimators ([[Bayesian Optimization]]).

[^1]: [Prince, p. 136](zotero://open-pdf/library/items/BWT7FYX5?page=150&annotation=MD5JJYK2)
