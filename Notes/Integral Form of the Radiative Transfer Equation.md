---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Integral Form of the Radiative Transfer Equation[^1]
> Along the ray through $x$ in direction $\omega$, the [[Radiative Transfer Equation|RTE]] is a linear first-order ODE; solving it gives
> $$
> \begin{align}
> L(x,\omega) = \int_{\overline{x_\partial x}} \mathcal{T}(y\leftrightarrow x)\Big(\mu_s(y)L_{\mathrm{ins}}(y,\omega) + \mu_a(y)L_e(y,\omega)\Big)\,d\ell(y) + \mathcal{T}(x_\partial\leftrightarrow x)\,L(x_\partial,\omega)
> \end{align}
> $$
> where $x_\partial$ is where the ray enters the medium,
> $$
> \begin{align}
> \mathcal{T}(y\leftrightarrow x) := \exp\left(-\int_{\overline{xy}}\mu_t\,d\ell\right)
> \end{align}
> $$
> is the transmittance — the probability a particle crosses the gap without interacting — and
> $$
> \begin{align}
> L_{\mathrm{ins}}(y,\omega) := \int_{\mathbb{S}^2} L(y,\omega_i)\,f_p(y,\omega_i\to\omega)\,d\sigma(\omega_i)
> \end{align}
> $$
> is the in-scattered radiance, the RTE's in-scattering term with $\mu_s$ pulled out front.

# Properties
- Requires sampling a [[Free-Flight Distance Sampling|free-flight distance]] along the ray to draw the point $y$ on the segment.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
