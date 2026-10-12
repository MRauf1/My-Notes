---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Green's Second Identity (One Dimension)[^1]
> For twice differentiable functions $X_1, X_2$ on $[a, b]$,
> $$
> \begin{align}
> \int_a^b \left(-X_1'' X_2 + X_1 X_2''\right) dx = \left(-X_1' X_2 + X_1 X_2'\right)\Big|_a^b.
> \end{align}
> $$

> [!info] Green's Second Identity (General)[^2]
> For $u, v \in C^2(\bar D)$ on a bounded domain $D \subset \mathbb{R}^n$ with piecewise smooth boundary and outward unit normal $\mathbf{n}$,
> $$
> \begin{align}
> \iiint_D \left(u\, \Delta v - v\, \Delta u\right) d\mathbf{x} = \iint_{\partial D} \left(u \frac{\partial v}{\partial n} - v \frac{\partial u}{\partial n}\right) dS.
> \end{align}
> $$

The one-dimensional version is two [[Integration by Parts|integrations by parts]]: the integrand is the exact derivative $(X_1 X_2' - X_1' X_2)'$. The general version follows from the divergence theorem applied to $u\nabla v - v\nabla u$; with $D = (a, b)$ and the [[Normal Derivative]] $\pm d/dx$ at the two ends it reduces to the 1D identity.

# Properties
- Says that $A = -d^2/dx^2$ (or $-\Delta$, the [[Laplacian Operator]]) is symmetric, $(Au, v) = (u, Av)$, exactly when the boundary term vanishes; this is the definition of a [[Symmetric Boundary Condition]].
- Implies the orthogonality of eigenfunctions with distinct eigenvalues ([[Symmetric Boundary Condition Orthogonality Theorem]]) and the reality of eigenvalues ([[Symmetric Boundary Condition Real Eigenvalue Theorem]]).
- Used to compute the expansion coefficients of solutions with inhomogeneous boundary data without differentiating a series term by term ([[Eigenfunction Expansion Method for Inhomogeneous Boundary Conditions]]).
- Higher-dimensional analogue of the [[Fundamental Theorem of Calculus]]; [[Green's Theorem]] is its planar circulation-flux cousin.[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=131&annotation=WRXK2M8Y)
[^2]: Added from general knowledge.
