---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Padding (Convolution)[^1]
> Extending the edges of the input of a [[Convolutional Layer|convolution]] with new values, so that outputs whose kernel extends beyond the input (e.g. the first and last outputs) can be computed as usual.

For a kernel with support $[-N, N] \times [-M, M]$, adding $N$ pixels left and right and $M$ pixels at the top and bottom makes the output the same size as the input image.[^3]

# Types
- **Zero-padding**: assumes the input is zero outside its valid range (or some other constant, such as the mean image value); the default in most neural networks.[^3]
- **Circular padding**: treats the input as periodic; for a $P \times Q$ image, $\ell_{\text{in}}[n, m] = \ell_{\text{in}}[(n)_P, (m)_Q]$ with $(n)_P$ the remainder of $n / P$. Introduces many artifacts but is convenient analytically, yielding the [[Circular Convolution]].[^3]
- **Reflection (mirror) padding**: reflects the input at the boundaries; the most common approach in image processing and the one that gives the best results.[^3]
- **Repeat padding**: sets each outside value to that of the nearest valid input pixel.[^3]
- **No padding (valid convolution)**: discard the output positions where the kernel exceeds the range of input positions.

# Properties
- There is no satisfactory boundary handling that works well for all applications; omitting boundary-affected outputs changes the output size and, for large kernels, can discard a large portion of the image.[^3]
- Valid convolutions introduce no extra information at the edges of the input, but the representation shrinks with each layer (by $K-1$ per dimension for kernel size $K$ and stride one).[^1]
- With stride one and odd kernel size $K$, zero-padding by $(K-1)/2$ on each side preserves the spatial size ("same" convolution).[^2]

[^1]: [Prince, p. 164](zotero://open-pdf/library/items/BWT7FYX5?page=178&annotation=FKRMB93U)
[^2]: Added from general knowledge.
[^3]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
