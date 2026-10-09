---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] DC Gain[^1]
> The gain of a filter $h[n, m]$ for a constant input (the lowest possible frequency). It equals the sum of the kernel values, which is the value of the filter's [[Discrete Fourier Transform|DFT]] at zero frequency:
> $$
> \begin{align}
> \text{DC gain} = \sum_{n, m} h[n, m] = H[0, 0]
> \end{align}
> $$
> If $\ell_{\text{in}}[n, m] = a$, then $\ell_{\text{out}}[n, m] = a \sum_{k, l} h[k, l]$.

# Properties
- $H[0,0] = \sum_{n,m} h[n,m]$ follows directly from setting $u = v = 0$ in the DFT definition.
- The DC gain multiplies the mean ([[DC Value]]) of the input signal.
- [[Blur Filter|Blur (low-pass) kernels]] are normalized to have DC gain $1$ (dividing by the kernel sum) so that the mean intensity of the image is preserved, e.g. the [[Box Filter]] $\text{box}_{N,M}$ has DC gain $(2N+1)(2M+1)$ before normalization and the [[Binomial Filter]] $b_n$ has DC gain $2^n$.
- A normalized [[High-Pass Filter]] $\delta - h_{\text{LP}}$ has DC gain $0$.

[^1]: [MIT Vision Book - Blurring](https://visionbook.mit.edu/blurring_2.html)
