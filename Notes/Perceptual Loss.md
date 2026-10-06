---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Perceptual Loss (VGG Loss)[^1]
> A loss that passes the synthesized output $\hat{\mathbf{x}}$ and the ground truth $\mathbf{x}$ through a fixed pretrained network (typically VGG) and measures the squared difference between their activations $\boldsymbol{\psi}_l[\bullet]$ at one or more layers $l$:
> $$
> \begin{align}
> L_{\text{perc}} = \sum_l \left\|\boldsymbol{\psi}_l[\hat{\mathbf{x}}] - \boldsymbol{\psi}_l[\mathbf{x}]\right\|_2^2
> \end{align}
> $$

# Properties
- Encourages semantic similarity to the target rather than pixel-wise agreement, so it penalizes less the plausible high-frequency deviations that pixel losses average into blur.[^1]
- Used in [[SRGAN]] alongside a pixel content loss and an [[Adversarial Loss]].
- Related in spirit to the [[Fréchet Inception Distance]], which also compares images in a pretrained network's feature space.

[^1]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=PFWVG6XU)
