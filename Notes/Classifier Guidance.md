---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Classifier Guidance[^1][^2]
> Conditional generation in a [[Diffusion Model|diffusion model]] using a separately trained classifier $Pr(c|\mathbf{z}_t)$ on the noisy latents: the gradient of its log-probability is added to each denoising update,
> $$
> \begin{align}
> \mathbf{z}_{t-1} = \hat{\mathbf{z}}_{t-1} + \sigma_t^2\frac{\partial\log Pr(c|\mathbf{z}_t)}{\partial\mathbf{z}_t} + \sigma_t\boldsymbol{\epsilon}
> \end{align}
> $$
> so each step moves toward latents that make the class $c$ more likely (Dhariwal & Nichol, 2021).

# Properties
- **Score interpretation**: by [[Bayes' Theorem]], $\nabla\log q(\mathbf{z}_t|c) = \nabla\log q(\mathbf{z}_t) + \nabla\log Pr(c|\mathbf{z}_t)$, so adding the classifier gradient turns the unconditional score into the conditional one. A guidance scale $s > 1$ multiplying the classifier term sharpens the conditional, $\propto q(\mathbf{z}_t)Pr(c|\mathbf{z}_t)^s$.
- **Classifier**: maps features from the downsampling half of the [[U-Net]] to the class; usually shared across all time steps and takes $t$ as input.[^1]
- Conditioning makes denoising easier, as with [[Conditional GAN|conditional GANs]], and improves sample quality.[^2]
- Drawback: training a separate noise-robust classifier is expensive, motivating [[Classifier-Free Guidance]].[^2]

[^1]: [Prince, p. 365](zotero://open-pdf/library/items/BWT7FYX5?page=379&annotation=6J8U4333); [Prince, p. 366](zotero://open-pdf/library/items/BWT7FYX5?page=380&annotation=3N4ZYVFJ)
[^2]: [Prince, p. 371](zotero://open-pdf/library/items/BWT7FYX5?page=385&annotation=MA6WXVUW)
