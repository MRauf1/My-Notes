---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Dequantization[^1]
> Adding noise to discrete data (e.g. quantized RGB values of images) before fitting a continuous density model, to prevent the training likelihood from increasing without bound. In uniform dequantization, an integer-valued $\mathbf{x}$ is replaced by $\mathbf{x} + \mathbf{u}$ with $\mathbf{u} \sim \mathrm{Uniform}[0, 1)^D$.

# Properties
- **Why it is needed**: a continuous density can place arbitrarily tall spikes on the finitely many discrete values, so the log-likelihood diverges without improving the model ([[Overfitting]]).[^1]
- With uniform noise, the continuous log-likelihood of the dequantized data lower-bounds the discrete log-likelihood $\log P(\mathbf{x}) = \log \int_{[0,1)^D} p(\mathbf{x} + \mathbf{u})\,d\mathbf{u}$ ([[Jensen's Inequality]]), so it is a meaningful objective.
- Used when training [[Normalizing Flow|normalizing flows]] such as [[Glow]] on images; results are often reported in bits per dimension.

[^1]: [Prince, p. 319](zotero://open-pdf/library/items/BWT7FYX5?page=333&annotation=TSQ29N5R)
