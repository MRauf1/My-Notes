---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Gibbs Phenomenon[^1]
> Near a [[Jump Discontinuity]] of $f$, the partial sums $S_N(x)$ of its [[Fourier Series]] overshoot (top and bottom) by about $9\%$ of the jump. As $N \to \infty$ the width of the overshoot region shrinks to zero, but its height does not, so
> $$
> \begin{align}
> \lim_{N \to \infty} \max_x |S_N(x) - f(x)| \neq 0,
> \end{align}
> $$
> even though $S_N(x) - f(x) \to 0$ at each $x$ where $f$ does not jump.

Precisely, for a jump of size $J$ the limiting overshoot on each side is[^2]
$$
\begin{align}
\left(\frac{1}{\pi}\int_0^\pi \frac{\sin t}{t}\, dt - \frac12\right) J \approx 0.0895\, J,
\end{align}
$$
attained at distance $\approx \pi/N$ from the jump (for period $2\pi$). It arises from the oscillating side lobes of the [[Dirichlet Kernel]], whose convolution with a step is a sine integral. The convergence is therefore pointwise ([[Fourier Series Pointwise Convergence Theorem]]) and in $L^2$ ([[Fourier Series L2 Convergence Theorem]]), but never uniform near a jump: a uniform limit of continuous partial sums would have to be continuous.

# Properties
- First observed by Wilbraham (1848) and rediscovered by Gibbs (1899) after Michelson's harmonic analyzer showed the overshoot.[^2]
- Occurs at the boundary of a [[Fourier Sine Series]] whenever $f(0) \neq 0$ or $f(l) \neq 0$, since the [[Odd Extension]] then jumps.[^2]
- Removed by smoothing the coefficients (Fejér/Cesàro means, Lanczos $\sigma$-factors, or other window functions), trading overshoot for blur.[^2]
- In image processing it appears as **ringing artifacts** around edges after ideal low-pass filtering or coarse quantization of frequency coefficients (e.g. JPEG), and as truncation artifacts in MRI.[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=154&annotation=BUDZASJL)
[^2]: Added from general knowledge.
