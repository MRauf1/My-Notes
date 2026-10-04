---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] $S$-Fold Cross-Validation[^1]
> Partition the available data into $S$ groups (in the simplest case of equal size). For each of the $S$ choices of held-out group, train on the remaining $S - 1$ groups and evaluate on the held-out group; the $S$ performance scores are then averaged.

Each run uses a fraction $(S-1)/S$ of the data for training, while all of the data is ultimately used to assess performance. This resolves the dilemma of a small [[Validation Set]], which gives a noisy estimate of predictive performance, versus a large one, which wastes training data.[^2]

# Types
- **Leave-one-out**: the case $S = N$, where $N$ is the number of data points, appropriate when data is particularly scarce.[^3]

# Properties
- In deep learning, the training and validation data are split into $K$ disjoint folds and hyperparameters are chosen by average validation performance. Final test performance is assessed on a separate test set using the average of the predictions of the $K$ models with the best hyperparameters. All variants aim to use a larger proportion of the data for training, reducing variance ([[Hyperparameter Search]]).[^5]
- The number of training runs is multiplied by $S$ ($N$ for leave-one-out), which is problematic when training itself is expensive.[^4]
- With several complexity [[Hyperparameter|hyperparameters]], exploring combinations of settings can, in the worst case, require a number of training runs exponential in the number of hyperparameters.[^4]
- A frequentist evaluation method that remains useful for [[Model Selection|model comparison]], even within Bayesian workflows, as protection against poor choices of prior.

[^1]: [Bishop, 2006, p. 33](zotero://open-pdf/library/items/5G99AZ8U?page=53&annotation=RGFPMUEC)
[^2]: [Bishop, 2006, p. 32](zotero://open-pdf/library/items/5G99AZ8U?page=52&annotation=3DMU7JNE)
[^3]: [Bishop, 2006, p. 33](zotero://open-pdf/library/items/5G99AZ8U?page=53&annotation=TEEH5LI3)
[^4]: [Bishop, 2006, p. 33](zotero://open-pdf/library/items/5G99AZ8U?page=53&annotation=B95CXRC2)
[^5]: [Prince, p. 134](zotero://open-pdf/library/items/BWT7FYX5?page=148&annotation=96Y2TTSV)
