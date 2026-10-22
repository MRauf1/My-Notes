---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation Dirichlet Problem Uniqueness[^1]
> On a connected bounded open set $D$, the Dirichlet problem for the [[Poisson Equation]]
> $$
> \begin{align}
> \Delta u = f \ \text{in } D, \qquad u = h \ \text{on } \partial D
> \end{align}
> $$
> has at most one solution $u \in C^2(D) \cap C(\bar D)$.

**Proof.**[^2] If $u, v$ both solve it, $w = u - v$ satisfies $\Delta w = 0$ in $D$ and $w = 0$ on $\partial D$. By the [[Maximum Principle (Laplace Equation)]], $0 = w(\mathbf{x}_m) \le w(\mathbf{x}) \le w(\mathbf{x}_M) = 0$ for all $\mathbf{x} \in D$, where $\mathbf{x}_m, \mathbf{x}_M \in \partial D$ are the boundary points of minimum and maximum. Hence $w \equiv 0$, i.e. $u \equiv v$.

# Properties
- The same argument gives uniform stability: $\max_{\bar D}|u - v| \le \max_{\partial D}|h_1 - h_2|$ for two Dirichlet data $h_1, h_2$ ([[Well-Posed Problem]]).[^3]
- The Neumann problem is unique only up to an additive constant, and is solvable only if $\iint_{\partial D} h \, dS = \iiint_D f \, d\mathbf{x}$.[^3]
- Symmetry consequence: if $D$ and $h$ (and $f$) are invariant under a rigid motion $g$, then so is the solution, because $u \circ g$ solves the same problem ([[Laplacian Operator Rigid Motion Invariance]]).[^3]
- Parabolic analogue: [[Diffusion Equation Well-Posedness]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=167&annotation=8AP5BV5E)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=168&annotation=2VIVF76D)
[^3]: Added from general knowledge.
