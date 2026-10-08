---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Wave Equation on a Finite Interval[^1][^2][^3]
> The guitar string with fixed ends,
> $$
> \begin{align}
> v_{tt} = c^2 v_{xx}, \quad v(x, 0) = \phi(x), \quad v_t(x, 0) = \psi(x) \ (0 < x < l), \quad v(0, t) = v(l, t) = 0,
> \end{align}
> $$
> is solved by the [[Method of Reflection]]: extend $\phi, \psi$ to be odd about both $x = 0$ and $x = l$, hence odd and $2l$-periodic on $\mathbb{R}$, and apply [[D'Alembert's Formula]] to the extensions:
> $$
> \begin{align}
> v(x, t) = \frac{1}{2}\left[\phi_{\text{ext}}(x + ct) + \phi_{\text{ext}}(x - ct)\right] + \frac{1}{2c}\int_{x - ct}^{x + ct} \psi_{\text{ext}}(s)\, ds.
> \end{align}
> $$

**Diamond-shaped regions.** Written back in terms of the original $\phi, \psi$ on $(0, l)$, the formula at $(x, t)$ depends on how many times each backward characteristic reflects off each end. The characteristics through the corners $(0, 0)$ and $(l, 0)$, bouncing between the walls, divide the strip $0 < x < l$, $t > 0$ into diamonds, and within each diamond the solution is given by a different explicit formula. Each reflection off a fixed end contributes a sign flip and a shift by a multiple of $2l$ in the argument of $\phi$ and in the limits of the $\psi$ integral.

**Inhomogeneous boundary data.**[^4] With $v(0, t) = h(t)$, $v(l, t) = k(t)$ (and zero initial data and forcing), the boundary signals are reflected back and forth indefinitely, giving the series
$$
\begin{align}
v(x, t) &= h\!\left(t - \tfrac{x}{c}\right) - h\!\left(t + \tfrac{x - 2l}{c}\right) + h\!\left(t - \tfrac{x + 2l}{c}\right) - \cdots \
&\quad + k\!\left(t + \tfrac{x - l}{c}\right) - k\!\left(t - \tfrac{x + l}{c}\right) + k\!\left(t + \tfrac{x - 3l}{c}\right) - \cdots,
\end{align}
$$
with $h, k$ taken to vanish for negative arguments, so for each $(x, t)$ only finitely many terms are nonzero.

# Properties
- Periodic in time with period $2l/c$, since the extended data are $2l$-periodic; the same fact appears as the harmonic series of separation of variables.
- Singularities of the data are reflected, not smoothed, bouncing between the ends forever ([[Wave and Diffusion Equation Comparison]]).
- Generalizes the single-wall [[Wave Equation on the Half-Line]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=75&annotation=AY6LSGST)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=77&annotation=IVHQUGGV)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=78&annotation=SLD9MLRR)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=90&annotation=9KANQNZK)
