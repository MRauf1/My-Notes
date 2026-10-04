---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Dataset Shift[^1]
> A mismatch between the statistics of the data a model was trained and tested on and those of real-world data, which makes held-out test performance unrepresentative of real-world performance. Its three main forms are:
> - **Covariate shift**: the distribution of the inputs (\mathbf{x})$ changes, so the model sees regions of the function that were sparsely sampled or unsampled in training.
> - **Prior shift**: the distribution of the outputs (\mathbf{y})$ changes, so outputs that were rare in training, and which the model learned not to predict in ambiguous cases, become common.
> - **Concept shift**: the relationship (\mathbf{y} | \mathbf{x})$ between input and output changes.

# Properties
- When the real-world statistics change over time, the model becomes stale and performance decays; this is **data drift**, so deployed models must be monitored.
- Reviewed by Moreno-Torres et al. (2012); see [[Robustness to Distributional Shift]] for approaches to mitigation.

[^1]: [Prince, p. 135](zotero://open-pdf/library/items/BWT7FYX5?page=149&annotation=FQEAZ3MU); [Prince, p. 135](zotero://open-pdf/library/items/BWT7FYX5?page=149&annotation=BVG72QEQ)
