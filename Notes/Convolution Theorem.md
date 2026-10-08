---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Convolution Theorem[^1]
> The [[Discrete Fourier Transform|DFT]] of the [[Circular Convolution|circular convolution]] of two $N \times M$ signals is the product of their DFTs:
> $$
> \begin{align}
> \ell_1[n, m] \circ_{N,M} \ell_2[n, m] \xrightarrow{\mathcal{F}} \mathscr{L}_1[u, v] \, \mathscr{L}_2[u, v]
> \end{align}
> $$
> Dually, the DFT of the product of two images is the (circular) convolution of their DFTs:
> $$
> \begin{align}
> \ell_1[n, m] \, \ell_2[n, m] \xrightarrow{\mathcal{F}} \frac{1}{NM} \mathscr{L}_1[u, v] \circ \mathscr{L}_2[u, v]
> \end{align}
> $$

**Proof sketch** (with $j = \sqrt{-1}$ the [[Imaginary Unit|imaginary unit]]): substitute the convolution into the DFT definition,
$$
\begin{align}
\mathscr{L}_{\text{out}}[u, v] = \sum_{n,m} \left\{ \sum_{k,l} \ell_1[n - k, m - l] \, \ell_2[k, l] \right\} \exp\left(-2\pi j \left(\frac{nu}{N} + \frac{mv}{M}\right)\right)
\end{align}
$$
extend $\ell_1$ periodically (which removes the modulo operators), substitute $n' = n - k$, $m' = m - l$, and swap the sums. The inner sum is $\mathscr{L}_1[u, v]$ times $\exp(-2\pi j(ku/N + lv/M))$, and the remaining sum over $k, l$ is $\mathscr{L}_2[u, v]$.

# Properties
- Convolution in the spatial domain is just multiplication in the Fourier domain, so the Fourier domain is the natural domain for analyzing [[Shift-Invariant System|space invariant linear]] processes: the Fourier bases ([[Discrete Complex Exponential|complex exponentials]]) are the eigenfunctions of all space invariant linear operators.
- For a filter with kernel $h$, $\mathscr{L}_{\text{out}} = H \, \mathscr{L}_{\text{in}}$, where $H$ is the [[Transfer Function (Signal Processing)|transfer function]].
- The dual form applies, e.g., to masking an image (multiplying it by a mask with $0$ in the pixels to be masked out), and underlies the [[Fourier Modulation Theorem]].
- The DFT version holds for *circular* convolution because the DFT assumes periodic signals; a linear convolution of signals of lengths $N_1, N_2$ can be computed by zero-padding both to length $\ge N_1 + N_2 - 1$ ([[Padding (Convolution)]]).[^2]
- Continuous version (general knowledge): $\ell_1(t) \circ \ell_2(t) \xrightarrow{\mathcal{F}} \mathscr{L}_1(w) \mathscr{L}_2(w)$ and $\ell_1(t) \ell_2(t) \xrightarrow{\mathcal{F}} \frac{1}{2\pi} \mathscr{L}_1(w) \circ \mathscr{L}_2(w)$ ([[Fourier Transform]], [[Convolution]]).[^2]
- Together with the [[Fast Fourier Transform]], gives $O(N \log N)$ convolution, faster than direct convolution for large kernels.[^2]
- In matrix form: the [[DFT Matrix]] diagonalizes circulant matrices; this is also the basis of [[Spectral Graph Convolution]], which replaces the Fourier basis with the eigenvectors of the [[Graph Laplacian Matrix]].[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
