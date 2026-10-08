---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Diffusion Kernel (Partial Differential Equations)[^1][^2]
> The diffusion kernel (also called the heat kernel, source function, Green's function, fundamental solution, or propagator) of the [[Diffusion Equation]] $u_t = k\Delta u$ on $\mathbb{R}^n$ is, for $t > 0$,
> $$
> \begin{align}
> S(\mathbf{x}, t) = \frac{1}{(4\pi k t)^{n/2}} e^{-|\mathbf{x}|^2 / 4kt}, \qquad \text{in 1D: } S(x, t) = \frac{1}{\sqrt{4\pi k t}} e^{-x^2 / 4kt}.
> \end{align}
> $$
> The unique bounded solution of $u_t = k\Delta u$, $u(\mathbf{x}, 0) = \phi(\mathbf{x})$ is the [[Convolution]]
> $$
> \begin{align}
> u(\mathbf{x}, t) = \int_{\mathbb{R}^n} S(\mathbf{x} - \mathbf{y}, t)\, \phi(\mathbf{y})\, d\mathbf{y} = \frac{1}{(4\pi k t)^{n/2}} \int_{\mathbb{R}^n} e^{-|\mathbf{x} - \mathbf{y}|^2 / 4kt}\, \phi(\mathbf{y})\, d\mathbf{y}.
> \end{align}
> $$
> The formula makes no sense at $t = 0$; there $S(\cdot, t) \to \delta$.

![[Diffusion Kernel (Partial Differential Equations).png]]

**It is a Gaussian.** $S(\cdot, t)$ is exactly the density of the [[Normal Distribution]] $N(\mathbf{0}, 2kt\, I)$: mean $\mathbf{0}$, variance $\sigma^2 = 2kt$ per coordinate, so $\sigma = \sqrt{2kt}$. Hence solving the diffusion equation for time $t$ is the same as blurring the initial data with a Gaussian of standard deviation $\sqrt{2kt}$, and conversely Gaussian blurring with $\sigma$ is diffusion run to time $t = \sigma^2 / 2k$ (the basis of Gaussian scale-space in computer vision). Its properties are the Gaussian's properties:
- Positive, even ($S(-\mathbf{x}, t) = S(\mathbf{x}, t)$), with total mass $\int S\, d\mathbf{x} = 1$ for all $t$.
- Small $t$: a tall thin spike of height $(4\pi k t)^{-n/2}$, and $\max_{|\mathbf{x}| > \delta} S(\mathbf{x}, t) \to 0$ as $t \to 0$, i.e. $S \to$ [[Dirac Delta Function|$\delta$]]. Large $t$: very spread out and flat.[^3]
- **Semigroup**: $S(\cdot, t) * S(\cdot, s) = S(\cdot, t + s)$, since variances of independent Gaussians add ([[Normal Distribution Linear Combination]]).
- Separable: the $n$-D kernel is the product of $n$ 1D kernels.

**Interpretations.**[^4][^5]
- **Weighted average**: $u(x, t) \approx \sum_i S(x - y_i, t)\phi(y_i)\Delta y_i$ is a Gaussian-weighted average of the initial values around $x$; for small $t$ it weights values near $x$ heavily, and for any $t > 0$ the solution is a spread-out version of $\phi$.
- **Diffusion**: $S(x - y, t)$ is the concentration produced by a unit mass placed exactly at $y$ at time $0$ and spreading out; a general initial distribution is the superposition of such spreading point masses.
- **Heat**: $S(x - y, t)$ is a hot spot at $y$ cooling off and spreading its heat along the rod.
- **[[Brownian Motion]]**: the probability that a particle starting at $x$ is in $(a, b)$ at time $t$ is $\int_a^b S(x - y, t)\, dy$. If the initial probability density is $\phi$, the density at time $t$ is $u = S * \phi$, which satisfies the diffusion equation.

# Properties
- Constructed via the [[Diffusion Equation Invariance Properties]]: $S = \partial Q / \partial x$, where $Q(x, t) = \tfrac12 + \tfrac12 \operatorname{erf}\!\left(x / \sqrt{4kt}\right)$ solves the problem with step initial data, so particular solutions are often expressible through the [[Error Function]], though $u = S * \phi$ is generally not elementary.[^6]
- **Infinite speed of propagation**: $S > 0$ everywhere for every $t > 0$, so a disturbance at any point is felt everywhere instantly (though mostly negligibly far away).
- **Smoothing**: $u = S * \phi$ is $C^\infty$ in $(\mathbf{x}, t)$ for $t > 0$ even if $\phi$ is merely bounded and piecewise continuous, because all derivatives fall on the smooth kernel.
  See [[Diffusion Equation Smoothing Theorem]].
- Half-line Green's functions $S(x - y, t) \mp S(x + y, t)$ by the [[Method of Reflection]]; as the source operator it generates the solution with sources via [[Duhamel's Principle]].
- **Decay**: $|u(\mathbf{x}, t)| \le (4\pi k t)^{-n/2}\|\phi\|_{L^1} \to 0$ for integrable $\phi$, while $\int u\, d\mathbf{x} = \int \phi\, d\mathbf{x}$ is conserved (mass spreads, it is not lost).
- In Fourier space, $\hat{S}(\boldsymbol{\xi}, t) = e^{-k|\boldsymbol{\xi}|^2 t}$: high frequencies are damped fastest, which is the smoothing and the irreversibility ([[Diffusion Equation Well-Posedness]]).
- Distinct from, but related to, the [[Diffusion Kernel]] of [[Diffusion Model|diffusion models]]: that is a Gaussian transition with an added shrinkage of the mean toward $\mathbf{0}$, whose noise part is this heat kernel.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=58&annotation=CBIAQ2L7); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=61&annotation=N9C22GXL); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=61&annotation=IFVIMJLG)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=62&annotation=WEL7L3AC); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=62&annotation=P89X3ABX)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=62&annotation=WCH57VZ8)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=62&annotation=HRIZY3MR); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=63&annotation=3B3ZHRVA)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=63&annotation=HRCCI9HP); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=63&annotation=L44DXV7Z)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=63&annotation=9PA3BU9Y)
