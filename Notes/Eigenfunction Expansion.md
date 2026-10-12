---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Eigenfunction Expansion (Generalized Fourier Series)[^1]
> Let $\{X_n\}$ be the [[Eigenfunction|eigenfunctions]] of $X'' + \lambda X = 0$ on $(a, b)$ with a [[Symmetric Boundary Condition]]. For any function $f$ on $(a, b)$, its **Fourier coefficients** are
> $$
> \begin{align}
> A_n = \frac{(f, X_n)}{(X_n, X_n)} = \frac{\int_a^b f(x)\, \overline{X_n(x)}\, dx}{\int_a^b |X_n(x)|^2\, dx},
> \end{align}
> $$
> and its **Fourier series** is $\sum_n A_n X_n(x)$.

The coefficient formula is forced by orthogonality ([[Symmetric Boundary Condition Orthogonality Theorem]]): if $f = \sum A_n X_n$, taking the [[L2 Inner Product]] with $X_m$ kills every term but one. In vector language, $A_n X_n$ is the [[Orthogonal Projection]] of $f$ onto the line spanned by $X_n$, and the series is an expansion in an orthogonal basis.

# Types
- [[Fourier Sine Series]]: Dirichlet conditions on $(0, l)$.
- [[Fourier Cosine Series]]: Neumann conditions on $(0, l)$.
- Full [[Fourier Series]]: [[Periodic Boundary Condition|periodic conditions]] on $(-l, l)$.
- The sine, cosine, and full series are the **classical** Fourier series.[^2]

# Properties
- Whether the series actually converges to $f$ depends on the mode of convergence and on the regularity of $f$: [[Fourier Series Uniform Convergence Theorem]], [[Fourier Series L2 Convergence Theorem]], [[Fourier Series Pointwise Convergence Theorem]].
- The partial sums are the best $L^2$ approximation from the span of $X_1, \dots, X_N$ ([[Best Approximation Theorem]]), and the coefficients satisfy [[Bessel's Inequality]], with equality ([[Parseval's Theorem]]) because the eigenfunctions form a [[Complete Orthogonal Set]].
- Term-by-term differentiation of the series is not always valid, so solutions of PDEs with inhomogeneous boundary data are handled by computing coefficients of derivatives through [[Green's Second Identity]] ([[Eigenfunction Expansion Method for Inhomogeneous Boundary Conditions]]).[^3]
- The engine of [[Separation of Variables]]: expanding in eigenfunctions diagonalizes the spatial operator.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=137&annotation=IJ6E4JY5)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=125&annotation=2A6XSSFJ)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=156&annotation=PJ6CUDY7)
