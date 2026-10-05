---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Stride (Convolution)[^1]
> The number of positions by which the kernel of a [[Convolutional Layer|convolution]] is shifted between consecutive outputs. Evaluating the output at every position is a stride of one; a stride of $s > 1$ produces roughly $1/s$ as many outputs per dimension.

# Properties
- A stride of two is equivalent to a stride-one convolution followed by keeping every other output, i.e. it applies subsampling simultaneously with the convolution ([[Downsampling (Deep Learning)]]).[^2]
- Striding increases the [[Receptive Field]] of subsequent layers faster than stride-one convolutions.[^3]
- Its "reverse", producing $s$ times as many outputs, is the [[Transposed Convolution]].

[^1]: [Prince, p. 164](zotero://open-pdf/library/items/BWT7FYX5?page=178&annotation=NIEYTC3F); [Prince, p. 165](zotero://open-pdf/library/items/BWT7FYX5?page=179&annotation=D2WUA2RM)
[^2]: [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=GHDZ29PZ); [Prince, p. 172](zotero://open-pdf/library/items/BWT7FYX5?page=186&annotation=USAZEZPX)
[^3]: [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=2BL7VV7Z)
