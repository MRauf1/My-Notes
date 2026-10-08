---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] DFT Matrix[^1]
> Since the [[Discrete Fourier Transform|DFT]] is linear, in 1D it can be written as $\boldsymbol{\mathscr{L}} = \mathbf{F} \boldsymbol{\ell}$ with one basis function per row:
> $$
> \begin{align}
> \mathbf{F}_{u,n} = \exp\left(-2\pi j \frac{un}{N}\right), \qquad
> \mathbf{F} =
> \begin{bmatrix}
> 1 & 1 & 1 & \cdots & 1 \\
> 1 & e^{-2\pi j \frac{1}{N}} & e^{-2\pi j \frac{2}{N}} & \cdots & e^{-2\pi j \frac{N-1}{N}} \\
> 1 & e^{-2\pi j \frac{2}{N}} & e^{-2\pi j \frac{4}{N}} & \cdots & e^{-2\pi j \frac{2(N-1)}{N}} \\
> \vdots & \vdots & \vdots & \ddots & \vdots \\
> 1 & e^{-2\pi j \frac{N-1}{N}} & e^{-2\pi j \frac{2(N-1)}{N}} & \cdots & e^{-2\pi j \frac{(N-1)(N-1)}{N}}
> \end{bmatrix}
> \end{align}
> $$
> with $u$ indexing rows and $n$ indexing columns.
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

# Properties
- $\mathbf{F}$ is symmetric: $\mathbf{F}^T = \mathbf{F}$.
- Its inverse is its complex conjugate up to scaling: $\mathbf{F}^* \mathbf{F} = N \mathbf{I}$, so $\mathbf{F}^{-1} = \frac{1}{N} \mathbf{F}^* = \frac{1}{N} \overline{\mathbf{F}}$ (the source writes $\mathbf{F}^{-1} = \mathbf{F}^*$, which only holds for the normalized matrix).[^2]
- The normalized matrix $\frac{1}{\sqrt{N}} \mathbf{F}$ is a [[Unitary Matrix]]; its rows form an orthonormal basis of [[Discrete Complex Exponential|complex exponentials]].[^2]
- Many properties and symmetries of the Fourier transform can be read off by inspecting the matrix.
- $\mathbf{F}$ diagonalizes every circulant matrix, i.e. every [[Circular Convolution]]; this is the matrix form of the [[Convolution Theorem]].[^2]
- Direct matrix-vector multiplication costs $O(N^2)$; the [[Fast Fourier Transform]] factorizes $\mathbf{F}$ into sparse factors to reach $O(N \log N)$.[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge / corrected from the source.
