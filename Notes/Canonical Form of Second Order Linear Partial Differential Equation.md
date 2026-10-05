---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!abstract] Theorem 1 (Two Variables)[^1]
> By a linear transformation of the independent variables, the [[Second Order Linear Partial Differential Equation]] $a_{11} u_{xx} + 2a_{12} u_{xy} + a_{22} u_{yy} + a_1 u_x + a_2 u_y + a_0 u = 0$ can be reduced to one of three forms ($\cdots$ denotes terms of order 1 or 0):
> 1. Elliptic, $a_{12}^2 < a_{11} a_{22}$: $\; u_{xx} + u_{yy} + \cdots = 0$.
> 2. Hyperbolic, $a_{12}^2 > a_{11} a_{22}$: $\; u_{xx} - u_{yy} + \cdots = 0$.
> 3. Parabolic, $a_{12}^2 = a_{11} a_{22}$ (and not $a_{11} = a_{12} = a_{22} = 0$): $\; u_{xx} + \cdots = 0$.

> [!abstract] Theorem 2 ($n$ Variables)[^2]
> For $\sum_{i,j} a_{ij} u_{x_i x_j} + \sum_i a_i u_{x_i} + a_0 u = 0$ with symmetric coefficient matrix $A$, a linear change of variables $\boldsymbol{\xi} = B\mathbf{x}$ transforms the coefficient matrix to $B A B^T$. Choosing $B = Q^T$ with $Q$ the [[Orthogonal Matrix]] of the [[Spectral Theorem|spectral decomposition]] $A = Q D Q^T$ gives the [[Diagonal Matrix|diagonal]] coefficient matrix $D = \operatorname{diag}(d_1, \dots, d_n)$ of [[Eigenvalue|eigenvalues]]:
> $$
> \begin{align}
> \sum_{i=1}^n d_i u_{\xi_i \xi_i} + \cdots = 0.
> \end{align}
> $$
> Further rescaling $\xi_i \mapsto \xi_i / \sqrt{|d_i|}$ (for $d_i \neq 0$) makes every second-order coefficient $+1$, $-1$, or $0$.

# Properties
- In 2D, the cases are the signs of $\det A = a_{11} a_{22} - a_{12}^2$: $> 0$ elliptic, $< 0$ hyperbolic, $= 0$ parabolic.
- The numbers of positive, negative, and zero coefficients are invariant under any invertible linear change of variables (Sylvester's law of inertia), so the type ([[Elliptic Partial Differential Equation|elliptic]], [[Hyperbolic Partial Differential Equation|hyperbolic]], [[Parabolic Partial Differential Equation|parabolic]], [[Ultrahyperbolic Partial Differential Equation|ultrahyperbolic]]) is well defined.
- The canonical principal parts are those of the [[Laplace Equation]], [[Wave Equation]], and [[Diffusion Equation]], making these three typical of all second-order linear PDEs.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=40&annotation=LNBGZ85H)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=42&annotation=XFT6IUJP)
