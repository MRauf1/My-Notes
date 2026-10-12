---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Roberts Cross Operator[^1]
> A pair of  \times 2$ [[Discrete Image Derivative|discrete derivative]] kernels that approximate the partial derivatives along the two diagonals (a reference frame rotated by ^\circ$):
> $$
> \begin{align}
> \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}, \qquad \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}
> \end{align}
> $$

# Properties
- Introduced by Roberts (1963) for edge extraction.
- Fixes the misalignment of the axis-aligned -1$ and -1^T$ kernels: both Roberts outputs are shifted by the same half pixel (to the center of the  \times 2$ block), so they are spatially aligned with each other.
- Its [[Discrete Fourier Transform|DFT]] is similar to a rotated version of that of the centered difference $.
- Although newer edge extractors exist, such simple operators remain useful when efficiency matters. Counterpart: [[Sobel Operator]].

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
