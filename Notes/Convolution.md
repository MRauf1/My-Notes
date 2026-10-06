---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Convolution[^1]
> The convolution, denoted $\circ$, of a signal $\ell_{\text{in}}[n]$ with a **convolution kernel** $h[n]$ is
> $$
> \begin{align}
> \ell_{\text{out}}[n] = h[n] \circ \ell_{\text{in}}[n] = \sum_{k=-\infty}^{\infty} h[n - k] \, \ell_{\text{in}}[k]
> \end{align}
> $$
> In 2D:
> $$
> \begin{align}
> \ell_{\text{out}}[n, m] = h[n, m] \circ \ell_{\text{in}}[n, m] = \sum_{k, l} h[n - k, m - l] \, \ell_{\text{in}}[k, l]
> \end{align}
> $$
> For continuous signals the sum becomes an integral:
> $$
> \begin{align}
> \ell_{\text{out}}(t) = h(t) \circ \ell_{\text{in}}(t) = \int_{-\infty}^{\infty} h(t - \tau) \, \ell_{\text{in}}(\tau) \, d\tau
> \end{align}
> $$

It is the [[Linear System (Signal Processing)|linear system]] $h[n, k]$ whose weights depend only on the relative position of input and output samples, $h[n, k] = h[n - k]$; this is exactly the form forced on a linear system by translation invariance ([[Shift-Invariant System|LTI system]]). Procedurally: mirror the kernel $h[k] \to h[-k]$, shift it so its origin is at $n$, multiply with the input values around $n$, and sum; in 2D the kernel is flipped vertically and horizontally and slid over the image, recording the inner product everywhere.

# Types
- [[Circular Convolution]]
- [[Convolutional Layer]] (a learned convolution in neural networks)

# Properties
- [[Convolution Basic Properties]]: commutative, associative, distributive, shift, support, and identity ([[Dirac Delta Function|impulse]]).
- For a finite length signal of length $N$, the sum runs over $k \in [0, N-1]$, and the system matrix $\mathbf{H}$ is banded with constant diagonals (a Toeplitz matrix), e.g. for a kernel with non-zero values only at $h[-1], h[0], h[1]$:
$$
\begin{align}
\begin{bmatrix} \ell_{\text{out}}[0] \\ \ell_{\text{out}}[1] \\ \ell_{\text{out}}[2] \\ \vdots \\ \ell_{\text{out}}[N-1] \end{bmatrix}
=
\begin{bmatrix}
h[0] & h[-1] & 0 & \cdots & 0 \\
h[1] & h[0] & h[-1] & \cdots & 0 \\
0 & h[1] & h[0] & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & h[0]
\end{bmatrix}
\begin{bmatrix} \ell_{\text{in}}[0] \\ \ell_{\text{in}}[1] \\ \ell_{\text{in}}[2] \\ \vdots \\ \ell_{\text{in}}[N-1] \end{bmatrix}
\end{align}
$$
- Closely related to [[Cross Correlation (Signal Processing)|cross-correlation]], whose weights are $h[n, k] = h[k - n]$: the same kernel, mirrored about the origin.
- The kernel $h$ of an LTI system is its [[Impulse Response]].
- Near the image boundary the kernel extends past the input; this is handled by [[Padding (Convolution)|padding]].
- The [[Convolution Formula]] of probability is the continuous convolution of densities: the pdf of the sum of independent random variables is $f_{X_1} \circ f_{X_2}$.

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
