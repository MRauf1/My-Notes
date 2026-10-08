---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Neumann Eigenvalue Problem on an Interval[^1][^2][^3]
> The [[Eigenfunction|eigenvalue problem]]
> $$
> \begin{align}
> -X'' = \lambda X, \qquad X'(0) = X'(l) = 0
> \end{align}
> $$
> has exactly the eigenvalues and eigenfunctions
> $$
> \begin{align}
> \lambda_n = \left(\frac{n\pi}{l}\right)^2, \qquad X_n(x) = \cos\frac{n\pi x}{l}, \qquad n = 0, 1, 2, \dots
> \end{align}
> $$
> Note that $n = 0$ is included: $\lambda_0 = 0$ is an eigenvalue whose eigenfunctions are the constants.[^4]

**Zero eigenvalue.** For $\lambda = 0$, $X = C + Dx$ and $X' \equiv D$; both Neumann conditions hold iff $D = 0$, with $C$ arbitrary. Negative or nonreal $\lambda$ give no eigenfunction (directly, as in the [[Dirichlet Eigenvalue Problem on an Interval|Dirichlet case]], or by symmetry).[^3]

**Spectral reading.**[^5] Integrating by parts, $\lambda\int_0^l |X|^2 = \int_0^l |X'|^2 \ge 0$ ([[Dirichlet Energy]]), with equality iff $X$ is constant. So the operator is positive *semi*definite with a one-dimensional kernel, the constants, exactly like the [[Graph Laplacian Matrix]] of a connected graph, whose kernel is spanned by $\mathbf 1$ (indeed the Neumann finite-difference Laplacian *is* the path-graph Laplacian). The first nonzero eigenvalue $\lambda_1 = (\pi/l)^2$ is the spectral gap (the continuous Fiedler value) and gives the sharp Poincaré–Wirtinger inequality
$$
\begin{align}
\int_0^l |X - \bar X|^2\, dx \le \left(\frac{l}{\pi}\right)^2 \int_0^l |X'|^2\, dx, \qquad \bar X = \frac{1}{l}\int_0^l X\, dx.
\end{align}
$$
It controls the rate at which insulated diffusion equilibrates ([[Diffusion Equation on a Finite Interval]]).

# Properties
- Expansion in the eigenfunctions is the [[Fourier Cosine Series]] $\phi = \tfrac12 A_0 + \sum_{n \ge 1} A_n \cos\frac{n\pi x}{l}$; the factor $\tfrac12$ lets the single formula $A_n = \frac{2}{l}\int_0^l \phi \cos\frac{n\pi x}{l}\,dx$ cover $n = 0$ too (since $\|1\|^2 = l$ while $\|\cos\|^2 = l/2$), so $\tfrac12 A_0$ is the mean of $\phi$.[^5]
- Eigenvalues coincide with the Dirichlet ones shifted by one index: $\lambda_n^N = \lambda_{n}^D$ for $n \ge 1$, plus the extra $\lambda_0^N = 0$.
- The $a_0 = a_l = 0$ case of the [[Robin Eigenvalue Problem on an Interval]].
- Used by [[Separation of Variables]] with a [[Neumann Boundary Condition]] at both ends; the zero mode produces the steady state $\tfrac12 A_0$ for diffusion and the drift $\tfrac12 A_0 + \tfrac12 B_0 t$ for waves ([[Wave Equation on a Finite Interval]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=101&annotation=YN7442UL)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=102&annotation=JD4WYYWM)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=102&annotation=ZEUSLNG2)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=102&annotation=C5B5WLJW)
[^5]: Spectral-theory connections added from general knowledge.
