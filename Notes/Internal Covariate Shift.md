---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Internal Covariate Shift[^1]
> The change in the distribution of the inputs to a network layer caused by updating the parameters of the preceding layers during training.

# Properties
- Reducing internal covariate shift was the original stated motivation of [[Batch Normalization]] (Ioffe & Szegedy, 2015).[^1]
- **Evidence against this explanation**: Santurkar et al. (2018) artificially induced covariate shift and found that networks with and without BatchNorm performed equally well. They instead attributed BatchNorm's benefit to a smoother loss surface whose loss and gradient change more slowly along the gradient direction (see [[Shattered Gradients]]).[^2]

[^1]: [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=JUBLEA25)
[^2]: [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=JUBLEA25); [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=JGZ9ISIE)
