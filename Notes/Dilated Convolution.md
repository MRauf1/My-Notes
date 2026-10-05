---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Dilated Convolution[^1]
> A [[Convolutional Layer|convolution]], also called **atrous convolution**, whose kernel values are interspersed with zeros, so that it integrates information over a larger input region without requiring more weights. The **dilation rate** $d$ is the number of zeros interspersed between the weights plus one; in 1D,
> $$
> \begin{align}
> z_i = \sum_{k=1}^{K} \omega_k\, x_{i + d\,(k - (K+1)/2)}
> \end{align}
> $$
> for odd kernel size $K$, with $d = 1$ recovering the ordinary convolution.

# Properties
- Motivation: the kernel size (typically odd, so it is centered on the current position) can be increased to integrate over a larger area, but this requires more weights. E.g. a kernel of size five with its second and fourth elements set to zero is a dilated kernel of size three with $d = 2$, covering five inputs with three weights.[^1]
- A kernel of size $K$ with dilation $d$ spans $d(K-1)+1$ inputs.[^2]
- Introduced by Chen et al. (2018) and Yu & Koltun (2015) (see REFERENCES).[^3]

[^1]: [Prince, p. 165](zotero://open-pdf/library/items/BWT7FYX5?page=179&annotation=6HJEL7FQ)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 181](zotero://open-pdf/library/items/BWT7FYX5?page=195&annotation=GA9QQRVM)
