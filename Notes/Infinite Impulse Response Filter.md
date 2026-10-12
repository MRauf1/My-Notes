---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Infinite Impulse Response Filter[^1]
> A filter whose [[Impulse Response|impulse response]] has infinite support, typically described by a **difference equation** in which the output depends on previous outputs. For example,
> $$
> \begin{align}
> \ell_{out}[n, m, t] = \ell_{in}[n, m, t] + \alpha \, \ell_{out}[n, m, t - 1]
> \end{align}
> $$
> Replacing the input with an impulse $\delta[n, m, t]$ gives the impulse response
> $$
> \begin{align}
> h[n, m, t] = \alpha^t \, \delta[n, m] \, u[t]
> \end{align}
> $$
> where $u[t]$ is the discrete [[Heaviside Function|Heaviside step function]].

# Properties
- Classified as stable or unstable ([[Bounded-Input Bounded-Output Stability]]). In unstable filters, the amplitude of the impulse response diverges to infinity.
- The example filter is stable iff $|\alpha| < 1$: then $\sum_t |h| = \sum_{t \geq 0} |\alpha|^t = \frac{1}{1 - |\alpha|}$ is a convergent [[Geometric Series]].[^2]
- The example is [[Causal Filter|causal]] ($u[t] = 0$ for $t < 0$); it is a temporal exponential smoother (leaky integrator) costing one multiply-add per pixel per frame despite its infinite support.[^2]
- Contrasts with **FIR (Finite Impulse Response)** filters, i.e. convolutions with finite-support kernels, which are always stable.[^2]
- The general form is a linear constant-coefficient difference equation $\sum_k a_k \ell_{out}[t - k] = \sum_k b_k \ell_{in}[t - k]$, whose [[Transfer Function (Signal Processing)|transfer function]] is a rational function of $e^{-jw}$.[^2]

[^1]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
[^2]: Added from general knowledge.
