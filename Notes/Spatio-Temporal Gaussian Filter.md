---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Spatio-Temporal Gaussian Filter[^1]
> The extension of the [[Gaussian Filter]] to image sequences, a [[Low-Pass Filter|low-pass]] [[Spatio-Temporal Filter|spatio-temporal filter]]:
> $$
> \begin{align}
> g(x, y, t; \sigma_x, \sigma_t) = \frac{1}{(2\pi)^{3/2} \sigma_x^2 \sigma_t} \exp\left(-\frac{x^2 + y^2}{2\sigma_x^2}\right) \exp\left(-\frac{t^2}{2\sigma_t^2}\right)
> \end{align}
> $$
> where $\sigma_x$ is the width along both spatial dimensions and $\sigma_t$ the width in time. Since the units of $t$ and $x, y$ are unrelated, there is no reason to set $\sigma_x = \sigma_t$.

# Properties
- Discretized by sampling into a 3D [[Convolution|convolution]] kernel, or approximated with the [[Binomial Filter]].
- **[[Separable Filter|Separable]]**: implemented efficiently as a cascade of three 1D convolutions (along $x$, $y$, $t$).
- **Non-[[Causal Filter|causal]]** in time (symmetric in $t$), hence not physically realizable. Fine for a video stored in memory; for a streamed video it must be bounded and shifted to be causal, delaying the output.
- **Derivatives** ([[Gaussian Derivative]]): the temporal derivative is
$$
\begin{align}
\frac{\partial g}{\partial t} = \frac{-t}{\sigma_t^2} g(x, y, t)
\end{align}
$$
  and the spatio-temporal gradient is
$$
\begin{align}
\nabla g = (g_x, g_y, g_t) = \left(\frac{-x}{\sigma_x^2}, \frac{-y}{\sigma_x^2}, \frac{-t}{\sigma_t^2}\right) g(x, y, t)
\end{align}
$$
  Sampling these analytic forms at discrete space-time locations gives discrete kernels for filtering sequences; they smooth the noisy temporal finite difference $\ell[n, m, t] - \ell[n, m, t-1]$ as in the spatial case ([[Discrete Image Derivative]]).
- **Velocity-selective filtering**:[^2] for a single object moving at constant velocity $(v_x, v_y)$, the [[Brightness Constancy Assumption|brightness constancy constraint]] gives $\ell_t = -v_x \ell_x - v_y \ell_y$, so the linear combination of derivative filters
$$
\begin{align}
h = v_x g_x + v_y g_y + g_t
\end{align}
$$
  outputs zero exactly for content moving at the target velocity $(v_x, v_y)$, removing it while passing other motions. In the frequency domain, $H = j(v_x w_x + v_y w_y + w_t)G$ vanishes on the plane carrying the [[Fourier Transform of Moving Image|moving image's spectrum]].

[^1]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
[^2]: Added from general knowledge; the highlights pose this question without the answer.
