---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Hermite Polynomial[^1]
> The (physicists') Hermite polynomials $H_n$ are the family of polynomials of degree $n$ defined by
> $$
> \begin{align}
> H_0(x) = 1, \quad H_1(x) = 2x, \quad H_n(x) = 2xH_{n-1}(x) - 2(n-1)H_{n-2}(x)
> \end{align}
> $$
> so $H_2(x) = 4x^2 - 2$. Equivalently (Rodrigues' formula),[^2]
> $$
> \begin{align}
> H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2}
> \end{align}
> $$

# Properties
- They arise from differentiating the Gaussian: the $n$-th [[Gaussian Derivative]] is $\left(\frac{-1}{\sigma\sqrt{2}}\right)^n H_n\left(\frac{x}{\sigma\sqrt{2}}\right) g(x; \sigma)$.
- $H_n$ has parity $(-1)^n$ (even for even $n$, odd for odd $n$).[^2]
- They are orthogonal with respect to the weight $e^{-x^2}$: $\int_{-\infty}^{\infty} H_n(x) H_m(x) e^{-x^2} \, dx = \sqrt{\pi} \, 2^n n! \, \delta_{nm}$.[^2]
- $H_n'(x) = 2nH_{n-1}(x)$.[^2]
- They are the [[Eigenfunction|eigenfunctions]] (times $e^{-x^2/2}$) of the quantum harmonic oscillator in the [[Schrödinger Equation]].[^2]

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
[^2]: Added from general knowledge.
