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

**Separation of variables.**[^5][^6][^7] The same problem is solved by [[Separation of Variables]] with the [[Dirichlet Eigenvalue Problem on an Interval|Dirichlet eigenfunctions]]:
$$
\begin{align}
u(x, t) = \sum_{n=1}^\infty \left(A_n \cos\frac{n\pi c t}{l} + B_n \sin\frac{n\pi c t}{l}\right)\sin\frac{n\pi x}{l}, \qquad \phi = \sum_n A_n \sin\frac{n\pi x}{l}, \quad \psi = \sum_n \frac{n\pi c}{l} B_n \sin\frac{n\pi x}{l},
\end{align}
$$
valid whenever $\phi, \psi$ have [[Fourier Sine Series|Fourier sine expansions]] (practically always, as Fourier claimed; proved in the theory of [[Fourier Series]]). The coefficients $n\pi c/l = c\sqrt{\lambda_n}$ are the (angular) **frequencies**, integer multiples of the fundamental $\pi c/l$ (some texts call $nc/2l$ the frequency); each separated solution is a normal mode in [[Simple Harmonic Motion]].

**Neumann ends** ($u_x(0, t) = u_x(l, t) = 0$).[^8] The zero eigenvalue of the [[Neumann Eigenvalue Problem on an Interval]] gives $T'' = 0$, $T = A + Bt$, so
$$
\begin{align}
u(x, t) = \frac12 A_0 + \frac12 B_0 t + \sum_{n=1}^\infty \left(A_n \cos\frac{n\pi c t}{l} + B_n \sin\frac{n\pi c t}{l}\right)\cos\frac{n\pi x}{l},
\end{align}
$$
with $\phi = \tfrac12 A_0 + \sum A_n \cos\frac{n\pi x}{l}$ and $\psi = \tfrac12 B_0 + \sum \frac{n\pi c}{l} B_n \cos\frac{n\pi x}{l}$: a free string can drift rigidly at constant velocity while vibrating.

**Spectral reading.**[^9] $u(t) = \cos(ct\sqrt{A})\phi + \frac{\sin(ct\sqrt A)}{c\sqrt A}\psi$ with $A = -d^2/dx^2$; since every mode only oscillates, the energy $\tfrac12\sum_n (|\dot T_n|^2 + c^2\lambda_n |T_n|^2)\|X_n\|^2$ is conserved mode by mode ([[Wave Equation Energy Conservation]], [[Dirichlet Energy]]). The eigenvalues are the squared frequencies, so "hearing the shape of a drum" is the inverse spectral problem for the Laplacian.

# Properties
- Periodic in time with period $2l/c$, since the extended data are $2l$-periodic; the same fact appears as the harmonic series of separation of variables.
- Singularities of the data are reflected, not smoothed, bouncing between the ends forever ([[Wave and Diffusion Equation Comparison]]).
- Generalizes the single-wall [[Wave Equation on the Half-Line]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=75&annotation=AY6LSGST)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=77&annotation=IVHQUGGV)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=78&annotation=SLD9MLRR)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=90&annotation=9KANQNZK)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=96&annotation=AWTSVNCY)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=97&annotation=D2NDSQ4S)
[^7]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=98&annotation=JWZ6DINZ); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=98&annotation=3Y3IXXXE); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=99&annotation=DZXJXYTX)
[^8]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=103&annotation=MW3XQS2X)
[^9]: Spectral-theory connection added from general knowledge.
