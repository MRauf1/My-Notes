---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Dirac Delta Function[^1]
> The continuous **impulse** $\delta(t)$: zero everywhere except at the origin, where it is infinitely high, such that
> $$
> \begin{align}
> \int_{-\infty}^{\infty} \delta(t) \, dt = 1
> \end{align}
> $$
> It is the identity of continuous [[Convolution|convolution]]: $\ell(t) \circ \delta(t) = \ell(t)$.

It is not a function in the strict sense, and is also called the **impulse distribution**. Rigorously, it is the distribution (generalized function) defined by its action on test functions, $\langle \delta, \varphi \rangle = \varphi(0)$, or as the limit of increasingly narrow unit-area functions, e.g. Gaussians with variance $\to 0$.[^2]

# Properties
- **Scaling**: $\delta(at) = \delta(t)/|a|$.
- **Symmetry**: $\delta(-t) = \delta(t)$.
- **Sampling**: $\ell(t)\,\delta(t - a) = \ell(a)\,\delta(t - a)$ for a constant $a$; hence the sifting property
$$
\begin{align}
\int_{-\infty}^{\infty} \ell(t) \, \delta(t - a) \, dt = \ell(a)
\end{align}
$$
  which underlies the analysis of [[Sampling (Signal Processing)|sampling]].
- **Convolution identity**: $\ell(t) \circ \delta(t) = \ell(t)$; an LTI system's response to $\delta$ is its [[Impulse Response]].
- Its discrete analogue is the impulse $\delta[n]$, equal to $1$ at $n = 0$ and $0$ elsewhere, i.e. the [[Kronecker Delta]] $\delta_{n0}$, which is the identity of discrete convolution ([[Convolution Basic Properties]]).
- It is the derivative of the [[Heaviside Function|Heaviside step function]] in the distributional sense.[^2] Correspondingly, $\int f(x)\,\delta(x - s)\,dx$ is made rigorous by the [[Riemann-Stieltjes Integral]] $\int f\,dI(x - s) = f(s)$ ([[Riemann-Stieltjes Integral with Step Function Integrator Theorem]]).
- **Gaussian limit**: $\delta(x) = \lim_{a\to\infty} a\,e^{-\pi(ax)^2}$. Combined with the [[Fourier Transform of Gaussian]], this gives $\delta \to 1$ and $1 \to \delta$.[^sigft]
- **Shifts**: $g * \delta(x - b) = g(x - b)$, and convolution with a [[Dirac Comb]] makes periodic copies.
- **Cosine pair**: $\tfrac12\delta(x + 1) + \tfrac12\delta(x - 1) \to \tfrac12 e^{2\pi iu} + \tfrac12 e^{-2\pi iu} = \cos(2\pi u)$, by the shift theorem and Euler's formula: the sine terms cancel.

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
[^sigft]: [Sigworth, Fourier transform notes, p. 3](zotero://open-pdf/library/items/FEUF2XYA?page=3&annotation=WPND9LEZ)
