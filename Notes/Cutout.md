---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Cutout[^1]
> A [[Regularization|regularization]] method in which a square patch of each input image is masked at training time.

# Properties
- Like [[Spatial Dropout]], it addresses the weakness of [[Dropout]] on images, where neighbouring correlated pixels carry the same information as a dropped one; masking a contiguous region removes it.[^1]
- Can be viewed as a form of [[Data Augmentation]].
- Proposed by DeVries & Taylor (2017).

[^1]: [Prince, p. 183](zotero://open-pdf/library/items/BWT7FYX5?page=197&annotation=V6VYB47L)
