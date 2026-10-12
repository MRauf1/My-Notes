---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Impulse Response[^1]
> The output of a [[Shift-Invariant System|LTI system]] when the input is the impulse $\delta[n]$. For an LTI filter with [[Convolution|convolution]] kernel $h[n]$, the output is the kernel itself:
> $$
> \begin{align}
> h[n] \circ \delta[n] = h[n]
> \end{align}
> $$
> so the kernel defining an LTI system is called its impulse response.

# Properties
- By translation invariance, a translated impulse $\delta[n - n_0]$ yields $h[n - n_0]$.
- For an unknown LTI system, the convolution kernel can be found by measuring its output to an impulse; this is one tool for explaining the behavior of complex systems such as neural networks.
- Its Fourier transform is the [[Transfer Function (Signal Processing)|transfer function]] of the system.
- In optics, the impulse response of an imaging system is its [[Point Spread Function]].
- Follows from the identity property of the impulse ([[Kronecker Delta]], [[Dirac Delta Function]]).
- In time, the impulse response determines [[Causal Filter|causality]] ($h[t] = 0$ for $t < 0$) and [[Bounded-Input Bounded-Output Stability|stability]]; filters whose impulse response has infinite support are [[Infinite Impulse Response Filter|IIR filters]].[^2]

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
