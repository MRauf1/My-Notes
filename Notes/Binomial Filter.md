---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Binomial Filter[^1]
> The 1D binomial kernel $b_n$ is the $n$-fold [[Convolution|convolution]] of the box filter $[1, 1]$; its coefficients are the [[Binomial Theorem|binomial coefficients]] (the $n$-th row of Pascal's triangle, [[Pascal's Identity]]):
> $$
> \begin{align}
> b_n[k] = {n \choose k}, \quad k = 0, \dots, n, \qquad b_0 = [1] \text{ (impulse)}, \; b_1 = [1, 1], \; b_2 = [1, 2, 1], \; b_4 = [1, 4, 6, 4, 1], \dots
> \end{align}
> $$
> It is an integer approximation of the [[Gaussian Filter]], via the [[Central Limit Theorem]].

# Properties
- [[DC Gain]] (sum of coefficients) is $2^n$; spatial variance is $\sigma_n^2 = n/4$ (that of a [[Binomial Distribution]] with $p = 1/2$).
- **Closed under convolution**: $b_n \circ b_m = b_{n+m}$, hence $\sigma_n^2 + \sigma_m^2 = \sigma_{n+m}^2$, the discrete analog of the Gaussian property. (The sampled Gaussian lacks this.)
- The simplest Gaussian approximation is the 3-tap kernel $b_2 = [1, 2, 1]$ ($\sigma^2 = 1/2$).
- Even binomial filters are powers of $[1, 2, 1]$, so their [[Discrete Fourier Transform|DFT]] (length $N$) is
$$
\begin{align}
B_{2n}[u] = \left(2 + 2\cos(2\pi u / N)\right)^n
\end{align}
$$
  which is real and nonnegative (a zero-phase filter) and monotonically decreasing in $|u|$.
- Every $b_n$ with $n \ge 1$ maps the highest-frequency wave $[1, -1, 1, -1, \dots]$ to the zero signal (since $[1,1]$ does), making it well suited as an antialiasing filter before downsampling ([[Aliasing]]).
- [[Separable Filter|Separable]] 2D version: $b_n[k]\,b_n[l]$.

[^1]: [MIT Vision Book - Blurring](https://visionbook.mit.edu/blurring_2.html)
