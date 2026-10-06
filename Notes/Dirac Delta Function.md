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
- It is the derivative of the [[Heaviside Function|Heaviside step function]] in the distributional sense.[^2]

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
