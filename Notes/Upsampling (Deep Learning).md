---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Upsampling (Deep Learning)[^1]
> Scaling up the spatial resolution of a hidden representation (typically doubling each dimension), which is needed when the network's output is also an image.

# Types
- **Duplication** (nearest-neighbour): duplicate all channels at each spatial position four times.[^2]
- [[Max Unpooling]]
- **Bilinear interpolation**: fill in the missing values between the sampled points by interpolation.[^2]
- [[Transposed Convolution]]

# Properties
- Counterpart of [[Downsampling (Deep Learning)]]; the first three types have no parameters, whereas transposed convolution is learned.

[^1]: [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=2BL7VV7Z)
[^2]: [Prince, p. 172](zotero://open-pdf/library/items/BWT7FYX5?page=186&annotation=KJATVQIL)
