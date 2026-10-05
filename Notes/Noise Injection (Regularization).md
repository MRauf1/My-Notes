---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Noise Injection (Regularization)[^1]
> Adding noise to parts of a network during training to make the final model more robust, generalizing [[Dropout]] (multiplicative Bernoulli noise on the activations).

# Types
- **Noise on the inputs**: smooths the learned function; for regression it is equivalent to a regularization term penalizing the derivatives of the output with respect to the input. Its extreme variant is [[Adversarial Training]].
- **Noise on the weights**: encourages sensible predictions under small weight perturbations, so training converges to minima in the middle of wide, flat regions where individual weights matter little.
- **Noise on the labels**: [[Label Smoothing]].
- **Noise from batch statistics**: [[Batch Normalization]] normalizes each example by statistics depending on the random batch composition.

[^1]: [Prince, p. 149](zotero://open-pdf/library/items/BWT7FYX5?page=163&annotation=76BUIMJ6); [Prince, p. 149](zotero://open-pdf/library/items/BWT7FYX5?page=163&annotation=8LN97ID5); [Prince, p. 149](zotero://open-pdf/library/items/BWT7FYX5?page=163&annotation=D87QRYZI)
