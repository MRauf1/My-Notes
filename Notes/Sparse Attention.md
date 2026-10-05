---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Sparse Attention[^1]
> Extending [[Transformer|transformers]] to longer sequences by pruning the [[Self-Attention|self-attention]] interactions, i.e. sparsifying the $N \times N$ interaction matrix so that each token attends to only a subset of tokens, reducing the $\mathcal{O}(N^2)$ cost of full attention.

# Types
- **Convolutional (local) attention**: each token interacts only with a few neighbouring tokens. As with [[Convolutional Layer|convolution]] in images, the kernel can vary in size and dilation rate ([[Dilated Convolution]]).[^1]
- **Selected tokens attend globally**: certain tokens (e.g. at the start of every sentence) attend to all other tokens (encoder) or all previous tokens (decoder).[^2]
- **Global tokens**: a small number of extra tokens that connect to all other tokens and to themselves; like the <cls> token they represent no word, but provide long-distance connections.[^2]

# Properties
- With local attention, tokens still interact at larger distances across layers as the [[Receptive Field|receptive field]] expands, but a purely local approach needs many layers to integrate information over long distances; global connections speed this up.[^1][^2]

[^1]: [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=PRM9WBFC); [Prince, p. 228](zotero://open-pdf/library/items/BWT7FYX5?page=242&annotation=2JRRI8PT)
[^2]: [Prince, p. 228](zotero://open-pdf/library/items/BWT7FYX5?page=242&annotation=8YAS9JIA)
