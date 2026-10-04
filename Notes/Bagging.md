---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Bagging[^1]
> **Bootstrap aggregating**: generating several datasets by resampling the training data with replacement ([[Bootstrap]]), training a separate model on each, and combining their predictions as an [[Ensemble Learning|ensemble]].

# Properties
- Smooths out the data: if a point is absent from one resampled training set, that model interpolates from nearby points, so the influence of an outlier is moderated in the ensemble.

[^1]: [Prince, p. 146](zotero://open-pdf/library/items/BWT7FYX5?page=160&annotation=7RLYMCWS); [Prince, p. 147](zotero://open-pdf/library/items/BWT7FYX5?page=161&annotation=8F8EJW9W)
