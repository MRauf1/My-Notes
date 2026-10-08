---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Eigenfunction[^1]
> Let $A$ be a linear differential operator acting on functions that satisfy given homogeneous [[Boundary Condition|boundary conditions]] (e.g. $A = -d^2/dx^2$ on functions with $X(0) = X(l) = 0$). An **eigenfunction** of $A$ is a solution $X \not\equiv 0$ of
> $$
> \begin{align}
> A X = \lambda X,
> \end{align}
> $$
> and an **eigenvalue** is a number $\lambda$ for which such a nonzero solution exists. For $A = -d^2/dx^2$ this is a two-point boundary value problem for an [[Ordinary Differential Equation]].

**Infinite-dimensional linear algebra.** This is the same notion as an [[Eigenvector]] and [[Eigenvalue]] of an $N \times N$ matrix, with the [[Function Space]] in place of $\mathbb{F}^N$ ([[Infinite-Dimensional Linear Operator]]). The difference: a matrix has at most $N$ eigenvalues, while $-d^2/dx^2$ with Dirichlet conditions has infinitely many, $\pi^2/l^2, 4\pi^2/l^2, 9\pi^2/l^2, \dots$[^2]

**Normal modes.** In physics and engineering eigenfunctions are called normal modes: they are the natural shapes of solutions that persist for all time, only their amplitude changing (decaying, oscillating, or growing) under the evolution.[^3]

**Spectral theory.**[^4] The finite-dimensional [[Spectral Theorem]] carries over, with care:
- *Symmetry.* For $-d^2/dx^2$ with Dirichlet, Neumann, mixed, Robin, or periodic conditions, [[Integration by Parts]] gives $\langle AX, Y \rangle = \langle X, AY \rangle$ on $L^2(0, l)$, where the boundary terms $[X'\bar Y - X \bar Y']_0^l$ vanish. Hence (as for a [[Self-Adjoint Linear Map]]) all eigenvalues are real and eigenfunctions of distinct eigenvalues are orthogonal. This is why no complex eigenvalues occur in any of the interval problems.
- *Quadratic form.* $\langle AX, X \rangle = \int |X'|^2 \, dx + (\text{boundary terms})$, the [[Dirichlet Energy]]; so the sign of the eigenvalues is decided by the energy and the boundary terms, exactly as a [[Positive Definite Matrix]] has positive eigenvalues. The eigenvalues are minima/min–max values of the Rayleigh quotient $\langle AX, X\rangle / \|X\|^2$.
- *Completeness.* $A$ is unbounded, but its inverse (an integral operator with the Green's function as kernel) is compact and self-adjoint, so by the spectral theorem for compact self-adjoint operators the normalized eigenfunctions form an [[Orthonormal Basis]] of $L^2(0, l)$, the eigenvalues are discrete with finite multiplicity, and $\lambda_n \to \infty$. This is the abstract reason that "practically any" function has a [[Fourier Sine Series]] or [[Fourier Cosine Series]].
- *Functional calculus.* Evolutions are functions of the operator: $e^{-ktA}$ (diffusion), $\cos(ct\sqrt A)$ (waves), $e^{-itA}$ (Schrödinger); see [[Separation of Variables]].
- *Weyl asymptotics.* For all these boundary conditions $\lambda_n \sim (n\pi/l)^2$; the boundary condition only affects lower-order terms. In $d$ dimensions, $\#\{\lambda_n \le \Lambda\} \sim \frac{\omega_d\, |\Omega|}{(2\pi)^d} \Lambda^{d/2}$ (Weyl's law), so the spectrum "hears" the volume.

# Types
- [[Dirichlet Eigenvalue Problem on an Interval]]
- [[Neumann Eigenvalue Problem on an Interval]]
- [[Mixed Eigenvalue Problem on an Interval]]
- [[Robin Eigenvalue Problem on an Interval]]

# Properties
- The building blocks of [[Separation of Variables]]; an expansion in eigenfunctions diagonalizes the PDE.
- Eigenfunctions of the [[Laplacian Operator]] are the continuous counterpart of eigenvectors of the [[Graph Laplacian Matrix]].
- With an orthogonal eigenbasis, [[Parseval's Theorem]] holds: $\|f\|^2 = \sum_n |\langle f, X_n\rangle|^2 / \|X_n\|^2$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=100&annotation=7BSX5QNZ)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=100&annotation=PSI8758E)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=100&annotation=Y7KGWXS9)
[^4]: Spectral-theory connections added from general knowledge (cf. Strauss §5.3 for symmetric boundary conditions).
