---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Gaussian Derivative[^1]
> The derivatives of the [[Gaussian Filter|Gaussian kernel]] $g(x, y; \sigma)$, used as kernels to compute smoothed image derivatives. Since [[Convolution|convolution]] and differentiation commute,
> $$
> \begin{align}
> \frac{\partial \ell(x, y)}{\partial x} \circ g(x, y) = \ell(x, y) \circ \frac{\partial g(x, y)}{\partial x}
> \end{align}
> $$
> The first and second order derivatives are
> $$
> \begin{align}
> g_x(x, y; \sigma) &= \frac{\partial g(x, y; \sigma)}{\partial x} = \frac{-x}{2\pi\sigma^4} \exp\left(-\frac{x^2 + y^2}{2\sigma^2}\right) = \frac{-x}{\sigma^2} g(x, y; \sigma) \\
> g_{x^2}(x, y; \sigma) &= \frac{x^2 - \sigma^2}{\sigma^4} g(x, y; \sigma)
> \end{align}
> $$
> In general, the $n$-th order derivative is a polynomial of degree $n$ (a [[Hermite Polynomial]]) times the Gaussian:
> $$
> \begin{align}
> g_{x^n}(x; \sigma) = \frac{\partial^n g(x; \sigma)}{\partial x^n} = \left(\frac{-1}{\sigma\sqrt{2}}\right)^n H_n\left(\frac{x}{\sigma\sqrt{2}}\right) g(x; \sigma)
> \end{align}
> $$
> and since the Gaussian is [[Separable Filter|separable]], in 2D
> $$
> \begin{align}
> g_{x^n, y^m}(x, y; \sigma) = \frac{\partial^{n+m} g(x, y)}{\partial x^n \partial y^m} = \left(\frac{-1}{\sigma\sqrt{2}}\right)^{n+m} H_n\left(\frac{x}{\sigma\sqrt{2}}\right) H_m\left(\frac{y}{\sigma\sqrt{2}}\right) g(x, y; \sigma)
> \end{align}
> $$

# Properties
- Commutativity is easy to prove in the Fourier domain: both sides equal $jw_x \mathscr{L}(w_x, w_y) G(w_x, w_y)$ ([[Convolution Theorem]]).
- Even where $\partial \ell / \partial x$ is undefined (e.g. at step boundaries), $\ell \circ g_x$ is always defined, since $g$ is infinitely differentiable.
- Smoothing the derivative reduces output noise at the cost of spatial resolution, addressing the noise sensitivity of the [[Discrete Image Derivative]]; $\sigma$ controls this trade-off.
- **Closed under convolution**: the convolution of Gaussian derivatives of orders $n$ and $m$ with variances $\sigma_1^2$ and $\sigma_2^2$ is a Gaussian derivative of order $n + m$ and variance $\sigma_1^2 + \sigma_2^2$ (trivial in the Fourier domain, where an order-$n$ derivative is $(jw)^n G(w; \sigma)$), generalizing the closure of the [[Gaussian Filter]].
- **Discrete approximations**: besides sampling the continuous functions, a common choice convolves [[Binomial Filter|binomial filters]] with $d_0 = [1, -1]$, $d_n = b_n \circ d_0$:
$$
\begin{align}
d_0 = [1, -1], \; d_1 = [1, 0, -1], \; d_2 = [1, 1, -1, -1], \; d_3 = [1, 2, 0, -2, -1], \; \dots
\end{align}
$$
  The 2D separable version with $d_1$ and $b_2$ is the [[Sobel Operator]].
- The Gaussian gradient and directional derivatives are covered in [[Image Gradient]]; the Laplacian of the Gaussian in [[Laplacian Filter]].

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
