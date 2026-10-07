---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Diffusion Equation Well-Posedness[^1][^2]
> **Uniqueness.** The Dirichlet problem
> $$
> \begin{align}
> u_t - k u_{xx} = f(x, t) \ (0 < x < l,\ t > 0), \quad u(x, 0) = \phi(x), \quad u(0, t) = g(t), \quad u(l, t) = h(t)
> \end{align}
> $$
> has at most one solution: any solution is determined completely by its initial and boundary data.
>
> **Stability.** If $u_1, u_2$ solve it with the same $f, g, h$ and initial data $\phi_1, \phi_2$, then for all $t \ge 0$
> $$
> \begin{align}
> \int_0^l |u_1 - u_2|^2(x, t)\, dx &\le \int_0^l |\phi_1 - \phi_2|^2\, dx && \text{(square-integral sense)} \\
> \max_{x} |u_1 - u_2|(x, t) &\le \max_{x} |\phi_1 - \phi_2| && \text{(uniform sense)}
> \end{align}
> $$
> If we start nearby, we stay nearby. The same holds in $\mathbb{R}^n$ (bounded domain, $u_t = k\Delta u$).

Together with existence, these make the forward diffusion problem a [[Well-Posed Problem]]; the two stabilities are the same idea measured with two different notions of nearness ($L^2$ vs. sup norm).[^3]

**Backward in time it is ill-posed: diffusion is irreversible.**[^4] Running the equation for $t < 0$ means un-smoothing. A Fourier mode $e^{i\xi x}$ decays like $e^{-k\xi^2 t}$ forward, so backward it grows like $e^{k\xi^2 |t|}$: arbitrarily small high-frequency perturbations of the data blow up arbitrarily fast, so there is no continuous dependence, and for generic data no solution at all. Physically, heat flow and [[Brownian Motion]] are irreversible processes (cf. the second law of thermodynamics and [[Entropy]]); going backward leads to chaos.

# Properties
- Uniqueness via the [[Maximum Principle (Diffusion Equation)|maximum principle]]: $w = u_1 - u_2$ has zero data, so $\max w \le 0$ and $\min w \ge 0$.
- Uniqueness via energy: $\frac{d}{dt}\int \tfrac12 w^2\, dx = -k\int w_x^2\, dx \le 0$ (boundary terms vanish), so $\int w^2$ is non-increasing from $0$. This also gives the $L^2$ stability.
- Uniform stability follows from the maximum and minimum principles applied to $u_1 - u_2$.
- On the whole line, uniqueness requires a growth restriction (e.g. bounded solutions); without it there are nonzero solutions with zero initial data (Tychonoff).
- Contrast: the [[Wave Equation]] is well-posed in both time directions ([[Wave and Diffusion Equation Comparison]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=56&annotation=85JUNIL6)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=57&annotation=GG632HRF); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=57&annotation=LIDJTA4L)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=57&annotation=52EACZ9N); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=57&annotation=APAZ8X7X)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=67&annotation=NWLNLRCD)
