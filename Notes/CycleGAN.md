---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] CycleGAN[^1][^2]
> An unpaired image-to-image translation model that jointly trains two mappings, $\mathbf{g}_{AB}$ from domain $A$ to domain $B$ and $\mathbf{g}_{BA}$ back, using a weighted sum of three losses:
> - a **content loss** based on the [[L1 Norm|$\ell_1$ norm]] that encourages before and after images to be similar;
> - an [[Adversarial Loss|adversarial loss]] per direction, encouraging translated images to be indistinguishable from real examples of the target domain;
> - a **cycle-consistency loss** that is low when a translated image can be translated back to the original:
> $$
> \begin{align}
> L_{\text{cyc}} = \sum_{\mathbf{a}} \left\|\mathbf{g}_{BA}[\mathbf{g}_{AB}[\mathbf{a}]] - \mathbf{a}\right\|_1 + \sum_{\mathbf{b}} \left\|\mathbf{g}_{AB}[\mathbf{g}_{BA}[\mathbf{b}]] - \mathbf{b}\right\|_1
> \end{align}
> $$

# Properties
- Handles two datasets of distinct styles with no matching pairs, which [[Pix2Pix]] and the standard [[Adversarial Loss]] setup cannot.[^1]
- Cycle consistency makes the mappings approximately inverse to each other, ruling out translations that discard the content of the input.[^2]
- In the original paper the "content" term is an optional identity loss $\|\mathbf{g}_{AB}[\mathbf{b}] - \mathbf{b}\|_1$ that preserves colour composition (Zhu et al., 2017).

[^1]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=7IDRW3PG)
[^2]: [Prince, p. 296](zotero://open-pdf/library/items/BWT7FYX5?page=310&annotation=FJ7EDM5C)
