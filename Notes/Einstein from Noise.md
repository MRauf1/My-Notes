---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Einstein from Noise[^1]
> Model bias in template-based [[Particle Picking]]: when windows of pure noise are selected by high correlation with a template (e.g. an image of Einstein), the average of the selected windows reproduces the template. The selection, not the data, creates the structure.

# Properties
- The same bias can carry into reconstruction whenever a reference guides selection or alignment. Remedies: template-free picking, independent half-set validation, and checking for density absent from the template (as in baited reconstruction with 2D template matching).
- It remains a live concern in 2025, e.g. confirmation bias in particle picking[^2].
- It is the standard example of **model bias**, which makes [[Cryo-EM Validation]] necessary.

# Questions
> [!question]- Why does averaging selected noise windows reproduce the template?
> Let $n \sim \mathcal{N}(0, \sigma^2 I)$ be a noise window and $t$ the template, with $\|t\| = 1$. Write $n = \langle n, t\rangle t + n_\perp$, where $\langle n, t\rangle$ and $n_\perp$ are independent (Gaussian, orthogonal components). Selecting $\langle n, t\rangle > c$ conditions only the first component, so $\mathbb{E}[n \mid \langle n, t\rangle > c] = \mathbb{E}[\langle n, t\rangle \mid \langle n, t\rangle > c]\, t + 0$, a positive multiple of $t$. The average converges to a scaled template.

[^1]: [Singer and Sigworth, 2020, p. 12](zotero://open-pdf/library/items/FKVQSKD6?page=12&annotation=J5GKZYK4)
[^2]: [Structure from Noise: Confirmation Bias in Particle Picking in Structural Biology (arXiv:2507.03951)](https://arxiv.org/abs/2507.03951)
