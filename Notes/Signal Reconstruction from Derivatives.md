---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Signal Reconstruction from Derivatives[^1]
> A signal can be recovered from its [[Discrete Image Derivative|derivative]] by integration, up to its [[DC Value|DC component]] (mean), unless a boundary condition supplies the missing constant. In matrix form, with $\mathbf{D}$ the [[Convolution|convolution]] matrix of $d_0 = [1, -1]$ for a length-$N$ signal:
> - **Zero boundary conditions** ($\ell[-1] = 0$): $\mathbf{D}$ is square, lower bidiagonal ($1$ on the diagonal, $-1$ below), and invertible; $\mathbf{D}^{-1}$ is the lower triangular matrix of ones, reconstructing each pixel as the cumulative sum of the derivative from the left-most pixel.
> - **Valid differences only** (pixels affected by the boundary removed): $\mathbf{D} \in \mathbb{R}^{(N-1) \times N}$ with rows $[\dots, -1, 1, \dots]$ has one sample fewer than the input. Its [[Pseudoinverse]] has entries
> $$
> \begin{align}
> (\mathbf{D}^+)_{ik} = \frac{k}{N} - [k > i], \qquad i = 0, \dots, N-1, \; k = 1, \dots, N-1
> \end{align}
> $$
> e.g. for $N = 5$:
> $$
> \begin{align}
> \mathbf{D}^+ = \frac{1}{5}\begin{bmatrix} -4 & -3 & -2 & -1 \\ 1 & -3 & -2 & -1 \\ 1 & 2 & -2 & -1 \\ 1 & 2 & 3 & -1 \\ 1 & 2 & 3 & 4 \end{bmatrix}
> \end{align}
> $$
> and $\mathbf{D}^+ \mathbf{D} \boldsymbol{\ell} = \boldsymbol{\ell} - \bar{\ell}\mathbf{1}$ recovers the input minus its mean.

# Properties
- With zero boundary conditions the inversion is "cheating": the first derivative sample sees the actual value $\ell[0]$, and this boundary constraint fixes the constant of integration.
- With valid differences the inverse recovers more samples than there are observations, so one degree of freedom is lost: $\ker \mathbf{D} = \operatorname{span}(\mathbf{1})$ (constants). The pseudoinverse returns the minimum-norm solution, which is orthogonal to $\mathbf{1}$, i.e. zero mean.[^2]
- $\mathbf{D}^+$ is not Toeplitz, so it cannot be written as a convolution.
- This integration step is used by the [[Retinex Algorithm]] to recover log-reflectance from thresholded gradients.
- Discrete analog of the [[Fundamental Theorem of Calculus]]: an [[Antiderivative]] is determined only up to a constant.

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
[^2]: Added from general knowledge (property of the [[Pseudoinverse]]).
