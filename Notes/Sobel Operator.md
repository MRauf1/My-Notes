---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Sobel Operator (Sobel-Feldman Operator)[^1]
> The [[Separable Filter|separable]] $3 \times 3$ [[Discrete Image Derivative|discrete derivative]] kernels formed by a centered difference $[1, 0, -1]$ along one axis and the [[Binomial Filter|binomial]] smoothing $b_2 = [1, 2, 1]$ along the other:
> $$
> \begin{align}
> \text{Sobel}_x = [1, 0, -1] \circ \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1 \end{bmatrix}, \qquad \text{Sobel}_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
> \end{align}
> $$

# Properties
- Designed to be compact and as isotropic as possible.
- It is a binomial approximation of the [[Gaussian Derivative]]: a derivative along one axis and a blur along the other, which reduces the noise sensitivity of plain differences.
- Efficient: it factors into four 2-tap kernels, $\text{Sobel}_x = b_1 \circ d_0 \circ b_1^T \circ b_1^T$ with $b_1 = [1, 1]$, $d_0 = [1, -1]$.
- Its [[Discrete Fourier Transform|DFT]] on an $N \times N$ (zero-padded) domain is separable:
$$
\begin{align}
\text{Sobel}_x[u, v] \propto D_1[u] \, B_2[v] = j \sin(2\pi u / N) \left(2 + 2\cos(2\pi v / N)\right)
\end{align}
$$
  i.e. it has the profile of the centered difference $D_1$ along $v = 0$ and is proportional to the profile of $B_2$ along $u$-constant sections.
- Counterpart: [[Roberts Cross Operator]]. Still used where efficiency matters and in descriptors such as SIFT and HOG.

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
