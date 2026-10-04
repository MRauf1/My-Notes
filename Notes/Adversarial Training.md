---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Adversarial Training[^1]
> Training in which the optimization algorithm actively searches for small perturbations of the input that cause large changes to the output, and trains the model on them; these perturbations act as worst-case additive noise vectors.

# Properties
- The extreme variant of input [[Noise Injection (Regularization)|noise injection]], which smooths the learned function.
- Commonly formulated as the min-max problem $\min_{\boldsymbol{\phi}} \sum_i \max_{\lVert \boldsymbol{\delta}_i \rVert \leq \epsilon} \ell_i[\mathbf{x}_i + \boldsymbol{\delta}_i, \mathbf{y}_i]$.[^2]

[^1]: [Prince, p. 149](zotero://open-pdf/library/items/BWT7FYX5?page=163&annotation=8LN97ID5)
[^2]: Min-max formulation added from general knowledge (Madry et al., 2018).
