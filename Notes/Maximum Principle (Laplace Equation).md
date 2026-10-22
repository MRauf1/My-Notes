---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Maximum Principle (Laplace Equation)[^1]
> Let $D \subset \mathbb{R}^n$ ($n = 2, 3$ in the source; the statement holds for every $n$) be a connected bounded open set, and let $u$ be a [[Harmonic Function]] in $D$ that is continuous on $\bar D = D \cup \partial D$. Then the maximum and the minimum values of $u$ are attained on $\partial D$ and nowhere inside, unless $u \equiv$ constant:
> $$
> \begin{align}
> \min_{\partial D} u \le u(\mathbf{x}) \le \max_{\partial D} u \qquad \text{for all } \mathbf{x} \in \bar D.
> \end{align}
> $$

A harmonic function is biggest somewhere on the boundary and smallest somewhere else on the boundary; no interior point has either property (unless $u$ is constant), while several boundary points may.[^2]

# Properties
- **Weak form** (extremes attained on $\partial D$) vs **strong form** (never attained inside unless constant); the strong form follows from the [[Mean Value Property (Harmonic Function)]].[^3]
- Time-independent case of the [[Maximum Principle (Diffusion Equation)]].
- Implies uniqueness and uniform stability of the Dirichlet problem: [[Laplace Equation Dirichlet Problem Uniqueness]].
- Holds one-sidedly for subharmonic ($\Delta u \ge 0$: max on $\partial D$) and superharmonic ($\Delta u \le 0$: min on $\partial D$) functions.[^3]
- Fails on unbounded domains without growth conditions, e.g. on the exterior of a circle one must impose boundedness at infinity ([[Laplace Equation in the Exterior of a Circle]]).[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=166&annotation=CK4QKFJT)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=166&annotation=X3FA493S); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=167&annotation=LRNN54X5)
[^3]: Added from general knowledge.
