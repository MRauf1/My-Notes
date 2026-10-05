---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Receptive Field[^1]
> The region of the original input that feeds into a given hidden unit of a network.

# Properties
- In a [[Convolutional Neural Network]], the receptive field grows with depth: with kernel size three, first-layer units see three inputs, second-layer units see five, and in general after $L$ stride-one layers of kernel size $K$ the receptive field is $1 + L(K-1)$.[^1]
- With [[Stride (Convolution)|strides]] $s_l$, kernel sizes $K_l$ (or effective sizes $d_l(K_l-1)+1$ for [[Dilated Convolution|dilated]] kernels), the receptive field obeys $r_l = r_{l-1} + (K_l - 1)\prod_{i<l} s_i$ with $r_0 = 1$, so [[Downsampling (Deep Learning)|downsampling]] grows it multiplicatively rather than linearly.[^2]
- The growth of receptive fields is how information from across the input is gradually integrated, from local to global.[^1]
- The term is borrowed from neuroscience, where it denotes the region of sensory space that drives a neuron's response.[^2]

[^1]: [Prince, p. 167](zotero://open-pdf/library/items/BWT7FYX5?page=181&annotation=LMGVCYWW); [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=2BL7VV7Z)
[^2]: Added from general knowledge.
