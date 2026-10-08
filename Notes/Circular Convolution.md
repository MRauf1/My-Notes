---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Circular Convolution[^1]
> The [[Convolution|convolution]] of two finite length signals $h$ and $\ell_{\text{in}}$ of length $N$ under circular [[Padding (Convolution)|padding]]:
> $$
> \begin{align}
> \ell_{\text{out}}[n] = h[n] \circ_N \ell_{\text{in}}[n] = \sum_{k=0}^{N-1} h\left[(n - k)_N\right] \ell_{\text{in}}[k]
> \end{align}
> $$
> where $(n)_N$ is $n$ modulo $N$, so $h[(n)_N]$ is the infinite periodic extension, with period $N$, of $h[n]$.

# Properties
- The output is periodic with period $N$: $\ell_{\text{out}}[n] = \ell_{\text{out}}[(n)_N]$.
- Has the same properties as the ordinary convolution, e.g. it is commutative ([[Convolution Basic Properties]]).
- Mainly an analytical convenience: it turns a finite signal into a periodic infinite one, at the cost of boundary artifacts.
- Its matrix $\mathbf{H}$ is circulant, so it is diagonalized by the [[DFT Matrix]] ([[Convolution Theorem]]: the [[Discrete Fourier Transform|DFT]] of $h \circ_N \ell$ is the pointwise product of the DFTs).[^2]

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
