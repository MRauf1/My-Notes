---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Spatio-Temporal Filter[^1]
> A linear spatio-temporal filter is a 3D [[Convolution|convolution]] between an input sequence $\ell_{in}[n, m, t]$ and a kernel ([[Impulse Response|impulse response]]) $h[n, m, t]$:
> $$
> \begin{align}
> \ell_{out}[n, m, t] = \sum_{k, l, \tau} h[n - k, m - l, t - \tau] \, \ell_{in}[k, l, \tau]
> \end{align}
> $$
> The extension from 2D filters adds no complications; filters are again classified as [[Low-Pass Filter|low-pass]], [[High-Pass Filter|high-pass]], etc., with the additional attribute of [[Causal Filter|causality]] in time.

# Types
- [[Causal Filter|Causal, non-causal, and anti-causal filters]]
- [[Infinite Impulse Response Filter]] (described by difference equations)
- [[Spatio-Temporal Gaussian Filter]] and its derivatives
- Box and triangular filters extend in the same way ([[Box Filter]])

# Properties
- Some filters, especially in time, are better described as **difference equations** than as convolutions (see [[Infinite Impulse Response Filter]]).
- **Temporal derivative**: the discrete approximation $\ell[n, m, t] - \ell[n, m, t - 1]$ ([[Discrete Image Derivative]] along $t$). Spatial derivatives locate image variations such as object boundaries; temporal derivatives locate moving objects.
- Motion appears as orientation in $(x, y, t)$ and as a tilted plane in the frequency domain ([[Fourier Transform of Moving Image]]), so spatio-temporal filters can be tuned to velocity.

[^1]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
