---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Piecewise [[Continuous Function]])[^1]
> [[Function]] $f$ on $[a, b]$ is piecewise continuous function if there is a [[Partition]] $P$ of $[a, b]$ such that $f$ is [[Uniformly Continuous Function]] on each interval $[t_{k-1}, t_k]$.

> [!info] Definition 2 (Piecewise Continuous Function on $\mathbb{R}$)[^2]
> A function $\phi$ on $\mathbb{R}$ is piecewise continuous if in each finite interval it has only finitely many [[Jump Discontinuity|jumps]] and it is continuous at all other points.

Definition 2 is the local version of Definition 1, adapted to unbounded domains: restricted to any $[a, b]$, each piece extends continuously to its closed subinterval because the one-sided limits at the jumps exist.

# Properties
- Bounded piecewise continuous initial data still give a $C^\infty$ solution of the [[Diffusion Equation]] for $t > 0$, converging to the average of the one-sided limits at each jump ([[Diffusion Equation Smoothing Theorem]]).

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=295)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=94&annotation=5ZJF86GY)
