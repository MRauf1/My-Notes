---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Early Stopping[^1]
> Stopping training before it has fully converged, which reduces [[Overfitting]] if the model has already captured the coarse shape of the underlying function but has not yet had time to fit the noise.

# Properties
- Since the weights are initialized to small values, they do not have time to grow large, so early stopping has an effect similar to explicit [[L2 Regularization]].
- Alternatively, it reduces the effective model complexity, moving back from the critical region of the [[Bias-Variance Tradeoff]] / [[Double Descent]] curve.
- Has a single [[Hyperparameter]], the number of steps, chosen on a [[Validation Set]] without training multiple models: train once, monitor validation performance every $T$ iterations while storing the parameters, and keep the stored parameters with the best validation performance.[^2]

[^1]: [Prince, p. 145](zotero://open-pdf/library/items/BWT7FYX5?page=159&annotation=97LB64YG)
[^2]: [Prince, p. 145](zotero://open-pdf/library/items/BWT7FYX5?page=159&annotation=DGAZ9I4A)
