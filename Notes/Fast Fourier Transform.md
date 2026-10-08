---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fast Fourier Transform (FFT)[^1]
> Any algorithm computing the [[Discrete Fourier Transform|DFT]] of a length $N$ signal in $O(N \log N)$ operations, instead of the $O(N^2)$ of the direct sum ([[DFT Matrix]]). The most common is the **Cooley–Tukey algorithm** (1965), which recursively splits a DFT of size $N$ into smaller DFTs. For radix-2 ($N$ a power of $2$), with $E[u]$ and $O[u]$ the length-$N/2$ DFTs of the even- and odd-indexed samples:[^2]
> $$
> \begin{align}
> \mathscr{L}[u] &= E[u] + e^{-2\pi j u / N} \, O[u] \\
> \mathscr{L}[u + N/2] &= E[u] - e^{-2\pi j u / N} \, O[u], \qquad u \in [0, N/2 - 1]
> \end{align}
> $$
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

# Properties
- The DFT became very popular thanks to the FFT.
- The recursion $T(N) = 2T(N/2) + O(N)$ gives $O(N \log N)$.[^2]
- Enables fast convolution: by the [[Convolution Theorem]], a convolution can be computed as FFT, pointwise product, inverse FFT, in $O(N \log N)$.[^2]
- An image DFT is computed by applying 1D FFTs along rows and then columns, using the separability of the 2D [[Discrete Complex Exponential|complex exponentials]].[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
