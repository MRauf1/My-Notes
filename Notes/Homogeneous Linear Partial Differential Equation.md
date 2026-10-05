---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition

> [!info] Definition 1 (Homogeneous Linear [[Partial Differential Equation]])[^1]
> Of the form $\mathcal{L}u = 0$, where $\mathcal{L}$ is some [[Linear Partial Differential Operator]], i.e. for all functions $u, v$ and constants $c$,
> $$
> \begin{align}
> \mathcal{L}(u + v) &= \mathcal{L}u + \mathcal{L}v \\
> \mathcal{L}(cu) &= c\,\mathcal{L}u.
> \end{align}
> $$

Can be of any order.

Two solutions can be combined to produce new solutions - $u + v, cu$, any [[Linear Combination]] ([[Superposition Principle (Partial Differential Equations)|Superposition Principle]]).

# Properties
- The solution set is the [[Kernel Vector Subspace|kernel]] of $\mathcal{L}$, a [[Vector Space]].
- Adding a solution of $\mathcal{L}u = 0$ to a solution of the [[Inhomogeneous Linear Partial Differential Equation]] $\mathcal{L}u = g$ gives another solution of $\mathcal{L}u = g$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=14&annotation=WFHSAPYJ)
