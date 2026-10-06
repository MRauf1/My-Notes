---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Adaptive Instance Normalization (AdaIN)[^1]
> [[Instance Normalization]] whose per-channel scale and offset are not learned constants but are supplied by an external style vector $\mathbf{y} = (\mathbf{y}_s, \mathbf{y}_b)$. For channel $c$ of feature map $\mathbf{h}$, with mean $\mu_c$ and standard deviation $\sigma_c$ computed over spatial positions,
> $$
> \begin{align}
> \mathrm{AdaIN}[\mathbf{h}, \mathbf{y}]_c = y_{s,c}\,\frac{\mathbf{h}_c - \mu_c[\mathbf{h}]}{\sigma_c[\mathbf{h}]} + y_{b,c}
> \end{align}
> $$

# Properties
- Normalization removes the existing channel statistics and the style vector imposes new ones, so style is transferred through first- and second-order feature statistics (Huang & Belongie, 2017).
- In [[StyleGAN]], $\mathbf{y}$ is a learned linear transform of the intermediate latent $\mathbf{w}$, and AdaIN is applied at several points of the generator so the same style acts at different scales.[^1]

[^1]: [Prince, p. 296](zotero://open-pdf/library/items/BWT7FYX5?page=310&annotation=Y8KPCTP7); [Prince, p. 298](zotero://open-pdf/library/items/BWT7FYX5?page=312&annotation=95SC89JB)
