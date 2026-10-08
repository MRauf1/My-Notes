---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Superposition Principle (Linear Equations)[^1]
> If $u_1, \dots, u_n$ are solutions of a [[Homogeneous Linear Partial Differential Equation]] $\mathcal{L}u = 0$, then so is every [[Linear Combination]]
> $$
> \begin{align}
> c_1 u_1(\mathbf{x}) + \cdots + c_n u_n(\mathbf{x}) = \sum_{j=1}^n c_j u_j(\mathbf{x}), \qquad c_j \text{ constants}.
> \end{align}
> $$
> Equivalently, the solution set of $\mathcal{L}u = 0$ is the [[Kernel Vector Subspace|kernel]] of the [[Linear Partial Differential Operator]] $\mathcal{L}$ and hence a [[Vector Space]].

# Properties
- Follows directly from the linearity $\mathcal{L}(u+v) = \mathcal{L}u + \mathcal{L}v$, $\mathcal{L}(cu) = c\mathcal{L}u$.
- Fails for nonlinear equations.
- The physical [[Superposition Principle]] of fields is an instance: it holds exactly because the governing field equations are linear.
- Adding a homogeneous solution to a solution of the [[Inhomogeneous Linear Partial Differential Equation]] gives another inhomogeneous solution.
- Basis of [[Separation of Variables]], which superposes separated solutions $X_n(x)T_n(t)$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=15&annotation=B4BVPKE6)
