---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Separable Filter[^1]
> A 2D kernel is separable if it factors as a product of 1D kernels, $h[n, m] = h^x[n] \, h^y[m]$. Equivalently, it is the [[Convolution|convolution]] of a horizontal and a vertical 1D kernel, $h = h^x \circ h^y$ (with $h^x[n] = h^x[n]\delta[m]$, $h^y[m] = \delta[n] h^y[m]$), so
> $$
> \begin{align}
> h[n, m] \circ \ell[n, m] = h^x \circ \left(h^y \circ \ell[n, m]\right)
> \end{align}
> $$
> More generally, an $n$-dimensional separable kernel is a cascade of $n$ 1D convolutions.

# Properties
- Computational saving: a direct convolution with an $N \times N$ kernel costs $\propto N^2$ multiplications per pixel, while the cascade of two 1D kernels costs $\propto 2N$.
- Its [[Discrete Fourier Transform|DFT]] is also separable: $H[u, v] = H^x[u] \, H^y[v]$.
- Examples: the [[Box Filter]], the [[Gaussian Filter]], and 2D [[Binomial Filter|binomial filters]].
- The [[Gaussian Filter|Gaussian]] is the only circularly symmetric separable kernel.

[^1]: [MIT Vision Book - Blurring](https://visionbook.mit.edu/blurring_2.html)
