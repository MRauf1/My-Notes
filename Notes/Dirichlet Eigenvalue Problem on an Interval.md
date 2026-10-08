---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Dirichlet Eigenvalue Problem on an Interval[^1][^2]
> The [[Eigenfunction|eigenvalue problem]]
> $$
> \begin{align}
> -X'' = \lambda X, \qquad X(0) = X(l) = 0
> \end{align}
> $$
> has exactly the eigenvalues and eigenfunctions
> $$
> \begin{align}
> \lambda_n = \left(\frac{n\pi}{l}\right)^2, \qquad X_n(x) = \sin\frac{n\pi x}{l}, \qquad n = 1, 2, 3, \dots
> \end{align}
> $$
> All eigenvalues are real and strictly positive.

**Proof that there are no others.**[^2]
- $\lambda = 0$: $X = C + Dx$, and $X(0) = X(l) = 0$ forces $C = D = 0$.
- $\lambda = -\gamma^2 < 0$: $X = C\cosh\gamma x + D\sinh\gamma x$ ([[Hyperbolic Function]]); $X(0) = 0$ gives $C = 0$, and $X(l) = D\sinh\gamma l = 0$ with $\sinh\gamma l \neq 0$ gives $D = 0$.
- $\lambda \in \mathbb{C}$ arbitrary: with $\gamma$ a square root of $-\lambda$, $X = Ce^{\gamma x} + De^{-\gamma x}$; the conditions give $C + D = 0$ and $Ce^{\gamma l} + De^{-\gamma l} = 0$, hence $e^{2\gamma l} = 1$, so $\operatorname{Re}\gamma = 0$ and $2l\operatorname{Im}\gamma = 2\pi n$. Thus $\gamma = n\pi i / l$ and $\lambda = -\gamma^2 = n^2\pi^2/l^2$.

**Spectral reading.**[^3] Positivity is immediate from the [[Dirichlet Energy]]: multiplying by $\bar X$ and integrating by parts (boundary terms vanish),
$$
\begin{align}
\lambda \int_0^l |X|^2\, dx = \int_0^l |X'|^2\, dx > 0,
\end{align}
$$
since $X' \equiv 0$ with $X(0) = 0$ would force $X \equiv 0$. So $-d^2/dx^2$ with Dirichlet conditions is a positive definite self-adjoint operator on $L^2(0, l)$, the infinite-dimensional analogue of a [[Positive Definite Matrix]]. Its lowest eigenvalue is the sharp Poincaré (Wirtinger) constant: $\int_0^l |X|^2 \le (l/\pi)^2 \int_0^l |X'|^2$ for $X(0) = X(l) = 0$. Its finite-difference discretization is the tridiagonal matrix $\frac{1}{h^2}\operatorname{tridiag}(-1, 2, -1)$, whose eigenvectors are exactly sampled sines (the DST basis) and whose eigenvalues $\frac{4}{h^2}\sin^2\frac{n\pi h}{2l}$ converge to $(n\pi/l)^2$.

# Properties
- Eigenfunctions are mutually orthogonal: $\int_0^l \sin\frac{n\pi x}{l}\sin\frac{m\pi x}{l}\,dx = \frac{l}{2}\delta_{nm}$ ([[Kronecker Delta]]); expansion in them is the [[Fourier Sine Series]].
- Used by [[Separation of Variables]] for the wave and diffusion equations with a [[Dirichlet Boundary Condition]] at both ends ([[Wave Equation on a Finite Interval]], [[Diffusion Equation on a Finite Interval]]).
- Upper bracket for every other interval problem: $\lambda_n^{\text{Neumann}} \le \lambda_n^{\text{Robin}, a \ge 0} \le \lambda_n^{\text{Dirichlet}}$, all indexed from $n = 0$ ([[Robin Eigenvalue Problem on an Interval]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=100&annotation=7BSX5QNZ)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=100&annotation=TD8LIRAT)
[^3]: Spectral-theory connections added from general knowledge.
