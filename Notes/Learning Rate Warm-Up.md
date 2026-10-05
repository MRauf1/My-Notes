---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Learning Rate Warm-Up[^1]
> Gradually increasing the [[Learning Rate|learning rate]] over the first few thousand iterations of training (Goyal et al., 2018).

# Properties
- Remedies a problem of adaptive optimizers such as [[Adam]]: their learning rates depend on accumulated gradient statistics, which are very noisy at the start of training when few samples have been seen.
- Rectified Adam (Liu et al., 2021) is an alternative that gradually changes the momentum term to avoid this high variance.
- Usually the first phase of a [[Learning Rate Schedule]].
- Essential for training [[Transformer|transformers]]: without it the gradients vanish and the [[Adam]] updates shrink (Xiong et al., 2020; Huang et al., 2020), owing to interacting effects of residual connections, Post-LN [[Layer Normalization]], and the small gradients of the query and key parameters.[^2]

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
[^2]: [Prince, p. 237](zotero://open-pdf/library/items/BWT7FYX5?page=251&annotation=X6CE7KIZ)
