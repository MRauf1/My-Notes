---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Gaussian Filter[^1]
> The [[Blur Filter|blur filter]] whose [[Convolution|convolution]] kernel is the Gaussian ([[Normal Distribution|normal]] density). In 1D and 2D:
> $$
> \begin{align}
> g(x; \sigma) &= \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{x^2}{2\sigma^2}\right) \\
> g(x, y; \sigma) &= \frac{1}{2\pi\sigma^2} \exp\left(-\frac{x^2 + y^2}{2\sigma^2}\right)
> \end{align}
> $$
> where $\sigma$ sets the spatial extent and the constant makes the kernel integrate to $1$. The discretized kernel (value $1$ at the origin) is
> $$
> \begin{align}
> g[n, m; \sigma] = \exp\left(-\frac{n^2 + m^2}{2\sigma^2}\right)
> \end{align}
> $$
> which in practice is normalized by the sum of its values so that its [[DC Gain]] is $1$, and truncated to $(-3\sigma, 3\sigma)$, where its amplitude is about $1\%$ of the central value.

# Properties
- A good model for many naturally occurring filters; larger $\sigma$ removes more image detail.
- Positive and symmetric, hence a zero-phase filter.
- **[[Separable Filter|Separable]]**: with $g^x[n] = g[n, 0]$, $g^y[m] = g[0, m]$,
$$
\begin{align}
g[n, m] \circ \ell[n, m] = \sum_k \exp\left(-\frac{(n-k)^2}{2\sigma^2}\right) \left(\sum_l \exp\left(-\frac{(m-l)^2}{2\sigma^2}\right) \ell[k, l]\right) = g^x \circ (g^y \circ \ell[n, m])
\end{align}
$$
  and the $n$-dimensional Gaussian is the only circularly symmetric operator that is separable.
- **[[Fourier Transform]] is a Gaussian**:
$$
\begin{align}
G(w; \sigma) = \exp\left(-\frac{w^2 \sigma^2}{2}\right), \qquad G(w_x, w_y; \sigma) = \exp\left(-\frac{(w_x^2 + w_y^2)\sigma^2}{2}\right)
\end{align}
$$
  which is radially symmetric and monotonically decreasing in frequency (an ideal monotonic [[Low-Pass Filter]]). Its width decreases with $\sigma$, opposite to the spatial domain.
- **Closed under convolution**: $g(x, y; \sigma_1) \circ g(x, y; \sigma_2) = g(x, y; \sigma_3)$ with $\sigma_3^2 = \sigma_1^2 + \sigma_2^2$ (by the [[Convolution Theorem]], the product of Gaussian FTs is a Gaussian FT); the basis of the Gaussian pyramid. This mirrors the [[Normal Distribution Linear Combination|sum of independent normals]] via the [[Convolution Formula]].
- It is the solution of the [[Heat Equation]] ([[Diffusion Kernel (Partial Differential Equations)|heat kernel]]), with $\sigma^2 \propto t$.
- Repeated convolutions of any function concentrated at the origin converge to a Gaussian ([[Central Limit Theorem]]).
- As $\sigma \to 0$ it becomes an impulse ([[Dirac Delta Function]]).
- **Discretization breaks these properties**: they hold only in the continuous domain. Convolving discretized Gaussians does not give a discretized Gaussian (errors accumulate over successive convolutions), the sampled kernel's actual variance differs from $\sigma^2$, and it does not fully cancel the highest frequency $[1, -1, 1, -1, \dots]$, which matters e.g. for antialiasing before downsampling ([[Aliasing]]). The [[Binomial Filter]] fixes these.

[^1]: [MIT Vision Book - Blurring](https://visionbook.mit.edu/blurring_2.html)
