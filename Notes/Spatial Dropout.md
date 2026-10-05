---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Spatial Dropout[^1]
> A variant of [[Dropout]] for [[Convolutional Layer|convolutional layers]] in which entire [[Feature Map|feature maps]] are discarded instead of individual pixels.

# Properties
- Motivation: standard dropout is less effective in convolutional layers because neighbouring pixels are highly correlated, so information from a dropped unit is still passed on via adjacent positions; dropping whole channels circumvents this.[^1]
- Proposed by Tompson et al. (2015). A related input-level method is [[Cutout]].

[^1]: [Prince, p. 183](zotero://open-pdf/library/items/BWT7FYX5?page=197&annotation=V6VYB47L)
