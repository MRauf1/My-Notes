---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Discrete Image Derivative[^1]
> The [[Derivative|derivative]] operator is linear and translation invariant ([[Shift-Invariant System|LTI]]), so its discrete approximations are [[Convolution|convolutions]] with small kernels. In 1D:
> $$
> \begin{align}
> \ell \circ d_0 &= \ell[n] - \ell[n-1], & d_0 &= [1, -1] \\
> \ell \circ d_1 &= \frac{\ell[n+1] - \ell[n-1]}{2}, & d_1 &= [1, 0, -1]/2
> \end{align}
> $$
> $d_0$ is the finite difference $\frac{\ell(x) - \ell(x - \epsilon)}{\epsilon}$ with $\epsilon = 1$; $d_1$ is the centered (central) difference. In 2D, partial derivatives along $n$ and $m$ are approximated by $[1, -1]$ and its transpose $[1, -1]^T$.

# Types
- [[Roberts Cross Operator]] (2-tap, rotated frame)
- [[Sobel Operator]] (3-tap, built from [[Binomial Filter|binomial filters]])
- [[Gaussian Derivative]] (derivative of a smoothing kernel; its binomial approximations $d_n = b_n \circ d_0$)
- [[Laplacian Filter]] (second order)

# Properties
- The output is zero where the input is constant and large where the input varies.
- $d_0$ is not centered at the origin, so its output is displaced by half a sample relative to the input; $d_1$ is centered, so its peak response lies at the midpoint of the variation. In 2D, the $[1,-1]$ and $[1,-1]^T$ outputs are therefore spatially misaligned with each other.
- **Fourier domain**: in the continuous domain, differentiation is multiplication by $jw$ ([[Fourier Transform]]):
$$
\begin{align}
\frac{\partial \ell(x)}{\partial x} \xrightarrow{\mathscr{F}} jw\mathscr{L}(w)
\end{align}
$$
  The [[Discrete Fourier Transform|DFTs]] (length $N$) of the discrete approximations are[^2]
$$
\begin{align}
D_0[u] &= 1 - e^{-2\pi j u/N} = 2j \sin(\pi u / N) \, e^{-\pi j u/N} \\
D_1[u] &= j \sin(2\pi u / N)
\end{align}
$$
  Both approximate $jw$ (with $w = 2\pi u/N$) at low frequencies. The linear phase $e^{-\pi j u/N}$ of $D_0$ is the half-sample shift ([[Fourier Shift Theorem]]); $D_1$ is purely imaginary (no shift) but vanishes at the highest frequency $u = N/2$.
- **Noise sensitivity**: for pixelwise independent noise of variance $\sigma^2$, the difference of two adjacent pixels has noise variance $2\sigma^2$ ([[Normal Distribution Linear Combination]]), while the signal difference is small for slowly varying images (except at object boundaries), so the output is dominated by noise. This motivates smoothing first with a [[Gaussian Derivative]].
- **Undefined derivatives**: a continuous image with a step (e.g. $\ell(x, y) = 0$ for $x < 0$ and $1$ otherwise) has no derivative at the discontinuity, whereas its discrete approximation is always defined. The [[Gaussian Derivative]] resolves this in the continuous domain.
- The derivative loses only the [[DC Value|DC component]] of the signal: see [[Signal Reconstruction from Derivatives]].
- Discrete derivatives are fundamental components of descriptors such as SIFT and HOG.
- **Temporal derivative**: $\ell[n, m, t] - \ell[n, m, t-1]$ approximates $\partial \ell / \partial t$ in image sequences and locates moving objects ([[Spatio-Temporal Filter]]).[^3]

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
[^2]: Derived from the DFT definition; the textbook's DFT discussion was not highlighted.
[^3]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
