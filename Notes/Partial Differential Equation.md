---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition

[[Differential Equation]] with [[Partial Derivative]].[^1] Has more than 1 [[Independent Variable]] and 1 [[Dependent Variable]].

> [!info] Partial Differential Equation[^2]
> Given independent variables $x, y, \dots$ (more than one) and an unknown dependent variable $u(x, y, \dots)$, a PDE is an identity relating the independent variables, $u$, and the partial derivatives of $u$ (written $u_x = \partial u / \partial x$, etc.). The most general first-order PDE in two variables is
> $$
> \begin{align}
> F(x, y, u, u_x, u_y) = 0.
> \end{align}
> $$
> A solution is a function $u(x, y, \dots)$ satisfying the equation identically, at least in some region of the independent variables.[^3]

# Order
- Highest order of [[Derivative]] that appears ([[Differential Equation Order]]).

# Types
- [[General Order Partial Differential Equation]]
- [[First Order Partial Differential Equation]]
- [[Second Order Partial Differential Equation]]
	- [[Second Order Linear Partial Differential Equation]] (elliptic / hyperbolic / parabolic / ultrahyperbolic)
- [[Homogeneous Linear Partial Differential Equation]] and [[Inhomogeneous Linear Partial Differential Equation]]

## Fundamental Equations
- [[Transport Equation]]
- [[Wave Equation]]
	- [[Damped Wave Equation]], [[Klein-Gordon Equation]], [[Inhomogeneous Wave Equation]], [[Linearized Acoustic Equations]]
- [[Diffusion Equation]]
	- [[Heat Equation]]
- [[Laplace Equation]]
- [[Schrödinger Equation]]

# Techniques
- [[Geometric Method]]
- [[Coordinate Change Method]]

# Properties
- Unlike for an [[Ordinary Differential Equation]], whose roles of dependent and independent variable are sometimes swapped (e.g. for separable ODEs), the distinction between the independent variables and the unknown is always maintained.[^3]
- Solutions generally depend on arbitrary functions rather than arbitrary constants (an ODE of order $m$ has $m$ arbitrary constants); e.g. $u_x = 0$ has solution $u = f(y)$. These arbitrary functions of fewer variables combine into a solution that is only partly arbitrary, since a function of two variables carries immensely more information than one of a single variable.[^4]
- Hence auxiliary conditions — [[Initial Condition|initial conditions]] and [[Boundary Condition|boundary conditions]] — are needed to single out a unique solution, ideally giving a [[Well-Posed Problem]].[^5]
- Linear PDEs obey the [[Superposition Principle (Partial Differential Equations)|superposition principle]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=620)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=13&annotation=ARYQM7IC)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=13&annotation=55KALYYC)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=16&annotation=D3RM86RN)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=21&annotation=EGJH7SN4)
