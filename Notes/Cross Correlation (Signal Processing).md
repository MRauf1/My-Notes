---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Cross Correlation (Signal Processing)[^1]
> The cross-correlation, denoted $\star$, between an image $\ell_{\text{in}}$ and a kernel $h$ with support $[-N, N] \times [-N, N]$ is
> $$
> \begin{align}
> \ell_{\text{out}}[n, m] = \ell_{\text{in}} \star h = \sum_{k, l = -N}^{N} \ell_{\text{in}}[n + k, m + l] \, h[k, l]
> \end{align}
> $$
> In 1D, it is the [[Linear System (Signal Processing)|linear system]] with weights $h[n, k] = h[k - n]$.

It is a translation invariant filter like the [[Convolution|convolution]] $\ell_{\text{in}} \circ h = \sum_{k,l} \ell_{\text{in}}[n - k, m - l]\, h[k, l]$, but the kernel is not inverted left-right and up-down; the two use the same kernel mirrored around the origin.

# Types
- [[Normalized Cross Correlation]]

# Properties
- Provides a simple technique for locating a template $h$ in an image (template matching).
- Unlike convolution, it is neither commutative nor associative ([[Convolution Basic Properties]]): it breaks the symmetry between $h$ and $\ell_{\text{in}}$, e.g. shifting $h$ is not equivalent to shifting $\ell_{\text{in}}$ (the output moves in opposite directions).
- Convolution and cross-correlation outputs are identical when $h$ has central symmetry, $h[-k, -l] = h[k, l]$.
- What deep learning calls convolution ([[Convolutional Layer]]) is actually cross-correlation.
- Statistical analogue: the [[Cross Correlation]] of stochastic processes.

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
