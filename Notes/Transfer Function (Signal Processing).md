---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Transfer Function (Signal Processing)[^1]
> For a linear filter written as a [[Convolution|convolution]] $\ell_{\text{out}}[n, m] = h[n, m] \circ \ell_{\text{in}}[n, m]$ with [[Impulse Response|impulse response]] (convolution kernel) $h$, the transfer function $H[u, v]$ is the [[Discrete Fourier Transform|Fourier transform]] of the kernel, so that in the Fourier domain the filter is a product ([[Convolution Theorem]]):
> $$
> \begin{align}
> \mathscr{L}_{\text{out}}[u, v] = H[u, v] \, \mathscr{L}_{\text{in}}[u, v]
> \end{align}
> $$
> In polar form,
> $$
> \begin{align}
> H[u, v] = \left| H[u, v] \right| \exp\left(j \angle H[u, v]\right)
> \end{align}
> $$
> where $|H[u, v]|$ is the **amplitude gain** and $\angle H[u, v]$ the **phase shift**. $|H[0, 0]|$ is the **DC gain**: the average value of the output equals the average value of the input times the DC gain.
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

# Types
Filters are often classified by the frequencies they let pass:
- [[Low-Pass Filter]]
- [[Band-Pass Filter]]
- [[High-Pass Filter]]

# Properties
- Interprets filters by how they modify the spectral content of the input: a linear filter only reweights the spectral components already present in the input; it cannot create new spectral content. Creating spectral components not present in the input requires nonlinearities.
- Equivalently, the [[Discrete Complex Exponential|complex exponential]] $e_{u,v}$ is an eigenfunction of the filter with eigenvalue $H[u, v]$ ([[Shift-Invariant System]]).
- In many cases, what a filter does is block or let pass certain frequencies.
- For an optical imaging system, the transfer function is the [[Optical Transfer Function]], and its amplitude gain is the [[Modulation Transfer Function]].
- The [[DC Value|DC]] gain is $H[0, 0] = \sum_{n,m} h[n, m]$; a kernel normalized to sum to $1$ preserves the image mean.[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
