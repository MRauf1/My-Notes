---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Dirichlet Kernel[^1]
> The Dirichlet kernel of order $N$ is the $2\pi$-periodic function
> $$
> \begin{align}
> K_N(\theta) = 1 + 2\sum_{n=1}^N \cos n\theta = \sum_{n=-N}^{N} e^{in\theta} = \frac{\sin\left(N + \frac12\right)\theta}{\sin \frac12 \theta}.
> \end{align}
> $$
> It is normalized so that
> $$
> \begin{align}
> \int_{-\pi}^{\pi} K_N(\theta)\, \frac{d\theta}{2\pi} = 1 + 0 + \cdots + 0 = 1.
> \end{align}
> $$

The partial sum of the full [[Fourier Series]] of a $2\pi$-periodic $f$ is the [[Convolution]] of $f$ with the kernel,[^2]
$$
\begin{align}
S_N(x) = \int_{-\pi}^{\pi} K_N(x - \theta)\, f(\theta)\, \frac{d\theta}{2\pi},
\end{align}
$$
so pointwise convergence of the series reduces to studying $K_N$: it concentrates at $\theta = 0$ (height $2N + 1$) and oscillates rapidly elsewhere. The closed form follows by summing the geometric series $\sum e^{in\theta}$.

# Properties
- The main tool in proving the [[Fourier Series Pointwise Convergence Theorem]] and in analyzing the [[Gibbs Phenomenon]].[^1]
- In signal processing terms, $S_N = f * K_N$ is ideal low-pass filtering: $K_N$ is the periodic sinc, whose Fourier coefficients are the box $\mathbf{1}_{|n| \le N}$.[^2]
- Not a good approximate identity: it takes negative values and $\int_{-\pi}^{\pi} |K_N|\, \frac{d\theta}{2\pi} \sim \frac{4}{\pi^2}\log N \to \infty$ (the Lebesgue constants). This unboundedness is why there exist continuous functions whose Fourier series diverge at a point.[^2]
- Averaging the kernels gives the nonnegative Fejér kernel, whose Cesàro means converge uniformly for every continuous periodic $f$ and avoid the Gibbs overshoot.[^2]
- As $N \to \infty$, $K_N \to 2\pi \sum_m \delta(\theta - 2\pi m)$ in the sense of distributions ([[Dirac Delta Function]]).[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=149&annotation=GPWRITXE)
[^2]: Added from general knowledge.
