---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Symmetric Boundary Condition[^1][^2]
> Consider a pair of homogeneous [[Boundary Condition|boundary conditions]] on $(a, b)$ with eight real constants,
> $$
> \begin{align}
> \alpha_1 X(a) + \beta_1 X(b) + \gamma_1 X'(a) + \delta_1 X'(b) &= 0, \\
> \alpha_2 X(a) + \beta_2 X(b) + \gamma_2 X'(a) + \delta_2 X'(b) &= 0.
> \end{align}
> $$
> They are **symmetric** if
> $$
> \begin{align}
> f'(x) g(x) - f(x) g'(x) \Big|_{x=a}^{x=b} = 0
> \end{align}
> $$
> for every pair of functions $f, g$ both satisfying the conditions. For complex-valued functions they are called **symmetric (hermitian)** if[^3]
> $$
> \begin{align}
> f'(x) \overline{g(x)} - f(x) \overline{g'(x)} \Big|_{a}^{b} = 0.
> \end{align}
> $$

**Linear-algebra reading.**[^4] Functions act as vectors and $A = -d^2/dx^2$ acts as a matrix (a [[Linear Operator]]). By [[Green's Second Identity]], symmetric boundary conditions are exactly what make $(Af, g) = (f, Ag)$ in the [[L2 Inner Product]], the analogue of a real symmetric matrix or [[Self-Adjoint Linear Map]]. Two differences from matrix theory: the vector space is infinite dimensional, and the boundary conditions are part of the definition of the operator (they fix its domain).

# Properties
- All the standard conditions are symmetric: [[Dirichlet Boundary Condition|Dirichlet]], [[Neumann Boundary Condition|Neumann]], [[Robin Boundary Condition|Robin]], and [[Periodic Boundary Condition|periodic]]; not every choice of the eight constants is.[^2]
- [[Symmetric Boundary Condition Orthogonality Theorem]]: eigenfunctions of distinct eigenvalues are orthogonal.
- [[Symmetric Boundary Condition Real Eigenvalue Theorem]]: eigenvalues are real and eigenfunctions can be chosen real.
- [[Symmetric Boundary Condition Nonnegative Eigenvalue Theorem]]: if additionally $f f'|_a^b \leq 0$, there are no negative eigenvalues.
- [[Symmetric Boundary Condition Infinite Eigenvalue Theorem]]: there are infinitely many eigenvalues, $\lambda_n \to +\infty$.
- The eigenfunctions are complete, so every $f$ with $\int_a^b |f|^2 < \infty$ has a convergent [[Eigenfunction Expansion]] ([[Fourier Series L2 Convergence Theorem]], [[Complete Orthogonal Set]]); together these are the infinite-dimensional [[Spectral Theorem]] for $-d^2/dx^2$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=131&annotation=JPM7R2IF)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=132&annotation=DQ67LX9Y)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=133&annotation=Z32Y62HQ)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=134&annotation=US72E29R)
