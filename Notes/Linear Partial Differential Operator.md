---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Linear Partial Differential Operator[^1]
> An operator $\mathcal{L}$ built from [[Partial Derivative|partial derivatives]], taking a function $v$ to a new function $\mathcal{L}v$, which is a [[Linear Operator]]: for any functions $u, v$ and any constant $c$,
> $$
> \begin{align}
> \mathcal{L}(u + v) &= \mathcal{L}u + \mathcal{L}v \\
> \mathcal{L}(cu) &= c\,\mathcal{L}u.
> \end{align}
> $$
> The general linear partial differential operator of order $m$ in $n$ variables is
> $$
> \begin{align}
> \mathcal{L} = \sum_{|\alpha| \le m} a_\alpha(\mathbf{x}) \, \partial^\alpha, \qquad \partial^\alpha = \frac{\partial^{|\alpha|}}{\partial x_1^{\alpha_1} \cdots \partial x_n^{\alpha_n}},
> \end{align}
> $$
> with coefficients $a_\alpha$ depending only on the [[Independent Variable|independent variables]] (not on $u$). It has constant coefficients if every $a_\alpha$ is constant.

# Types
- [[Laplacian Operator]]

# Properties
- A [[Partial Differential Equation]] $\mathcal{L}u = g$ is linear iff $\mathcal{L}$ is linear; see [[Homogeneous Linear Partial Differential Equation]] and [[Inhomogeneous Linear Partial Differential Equation]].
- Linearity is what gives the [[Superposition Principle (Partial Differential Equations)|superposition principle]].
- $\partial/\partial x$ is the simplest example: it takes $v$ to $v_x$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=14&annotation=WFHSAPYJ)
