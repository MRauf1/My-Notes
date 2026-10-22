---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation in a Rectangle[^1][^2]
> Solve $u_{xx} + u_{yy} = 0$ in $D = \{0 < x < a,\ 0 < y < b\}$ with a standard (Dirichlet, Neumann, or Robin) condition on each side, of which three are homogeneous and the remaining one is $u(x, b) = g(x)$. By [[Separation of Variables]], $u = X(x)Y(y)$:
> 1. $-X'' = \lambda X$ with the homogeneous conditions at $x = 0, a$: eigenpairs $(\lambda_n, X_n)$.
> 2. $Y'' = \lambda_n Y$ with the homogeneous condition at $y = 0$: for $\lambda_n = \beta_n^2 > 0$, $Y_n(y) = A\cosh\beta_n y + B\sinh\beta_n y$ with $A, B$ fixed (up to scale) by that condition.
> 3. Sum: $u(x, y) = \sum_n A_n X_n(x) Y_n(y)$ is harmonic in $D$ and satisfies the three homogeneous conditions.
> 4. Impose $u(x, b) = g(x)$, an eigenfunction expansion of $g$:
> $$
> \begin{align}
> g(x) = \sum_n A_n Y_n(b)\, X_n(x) \quad\Rightarrow\quad A_n = \frac{1}{Y_n(b)}\frac{\int_0^a g(x) X_n(x)\, dx}{\int_0^a X_n(x)^2\, dx}.
> \end{align}
> $$

The general case with several inhomogeneous sides is a sum of such problems ([[Superposition Principle (Partial Differential Equations)]]). Because the rectangle is bounded, the growing hyperbolic functions $\cosh, \sinh$ cause no trouble.[^2]

# Properties
- The $x$-problems are those of [[Dirichlet Eigenvalue Problem on an Interval]], [[Neumann Eigenvalue Problem on an Interval]], [[Mixed Eigenvalue Problem on an Interval]], [[Robin Eigenvalue Problem on an Interval]]; step 4 is a [[Fourier Sine Series]] or [[Fourier Cosine Series]] in those cases.
- Unlike the evolution equations, the "other" variable $y$ produces exponentials $e^{\pm\beta_n y}$ rather than decaying or oscillating time factors.
- 3D analogue: [[Laplace Equation in a Box]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=173&annotation=YGQIZN3J); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=174&annotation=R6ZHNJ3Y)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=175&annotation=NPV7R37D)
