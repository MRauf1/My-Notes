---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Sharpening Filter[^1]
> A filter that makes an image appear sharper (containing more fine detail) by amplifying its high [[Spatial Frequency|spatial-frequency]] content. By the linearity of [[Convolution|convolution]], it can be built by starting from twice the image and subtracting a [[Blur Filter|blurred]] copy, e.g. with the $3 \times 3$ [[Binomial Filter]]:
> $$
> \begin{align}
> \text{sharpening filter} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{bmatrix} - \frac{1}{16}\begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}
> \end{align}
> $$

# Properties
- Its [[DC Gain]] is $1$: it equals $\delta + (\delta - h_{\text{blur}})$, the original image plus the [[High-Pass Filter|high-pass]] (sharp detail) component. This is the idea of unsharp masking.[^2]
- Can be applied successively to further enhance detail, but too much sharpening enhances noise and introduces [[Image Artifact|artifacts]].
- Subtracting a multiple of the [[Laplacian Filter|Laplacian]] from the image also sharpens it.[^2]

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
[^2]: Added from general knowledge.
