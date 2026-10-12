---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Eigenfunction Expansion Method for Inhomogeneous Boundary Conditions[^1][^2]
> When the boundary data are inhomogeneous, a separated solution $X(x)T(t)$ cannot fit the boundary conditions. Instead, expand the unknown solution in the eigenfunctions $X_n$ of the corresponding homogeneous problem,
> $$
> \begin{align}
> u(x, t) = \sum_n u_n(t)\, X_n(x), \qquad u_n(t) = \frac{(u(\cdot, t), X_n)}{(X_n, X_n)},
> \end{align}
> $$
> and derive an [[Ordinary Differential Equation]] for each $u_n(t)$ by differentiating the coefficient formula in $t$, using the PDE, and moving the $x$-derivatives onto $X_n$ with [[Green's Second Identity]]. The boundary data enter as forcing terms.
>
> **Diffusion.** For $u_t = k u_{xx}$ on $0 < x < l$, $u(0, t) = h(t)$, $u(l, t) = j(t)$, $u(x, 0) = 0$, with $X_n = \sin(n\pi x/l)$, $\lambda_n = (n\pi/l)^2$:
> $$
> \begin{align}
> \frac{du_n}{dt} + \lambda_n k\, u_n = -2n\pi l^{-2} k\left[(-1)^n j(t) - h(t)\right], \qquad u_n(0) = 0,
> \end{align}
> $$
> $$
> \begin{align}
> u_n(t) = -2n\pi l^{-2} k \int_0^t e^{-\lambda_n k (t - s)}\left[(-1)^n j(s) - h(s)\right] ds.
> \end{align}
> $$
>
> **Waves.** For $u_{tt} - c^2 u_{xx} = f(x, t)$, $u(0, t) = h(t)$, $u(l, t) = k(t)$, $u(x, 0) = \phi(x)$, $u_t(x, 0) = \psi(x)$:[^3]
> $$
> \begin{align}
> \frac{d^2 u_n}{dt^2} + c^2 \lambda_n u_n = -2n\pi l^{-2} c^2\left[(-1)^n k(t) - h(t)\right] + f_n(t), \qquad u_n(0) = \phi_n, \quad u_n'(0) = \psi_n,
> \end{align}
> $$
> where $f_n, \phi_n, \psi_n$ are the sine coefficients of $f, \phi, \psi$.

The detour through Green's identity is necessary because term-by-term differentiation of a Fourier series is not always valid: the series for $u$ consists of sines that vanish at $x = 0, l$ while $u$ does not, so it cannot be differentiated twice term by term and checked directly.[^4] Each mode ODE is solved by variation of parameters ([[Duhamel's Principle]] for a single mode).

# Properties
- Alternative to the [[Boundary Condition Subtraction Device]], which first makes the boundary conditions homogeneous by subtracting a known function; both shift the boundary data into the interior as a source.[^5]
- Applies to the [[Inhomogeneous Diffusion Equation]] and [[Inhomogeneous Wave Equation]] on a finite interval, and to any [[Symmetric Boundary Condition]] with the appropriate [[Eigenfunction Expansion]].
- The sine series for $u$ converges to $u$ inside $(0, l)$ but not uniformly up to the endpoints when $h, j \neq 0$ ([[Gibbs Phenomenon]] of the [[Odd Extension]]).[^6]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=159&annotation=SI9RCAN8)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=160&annotation=D8HYLFWV)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=161&annotation=A3KJXN7F); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=161&annotation=TBZAZ73Z) (the factor $c^2$ on the boundary term follows from $u_{tt} = c^2 u_{xx} + f$ and is restored here)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=156&annotation=PJ6CUDY7)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=161&annotation=2PUHR5U6)
[^6]: Added from general knowledge.
