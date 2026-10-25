---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Weierstrass M-Test)[^1]
> Let $(M_k)$ be a [[Sequence]] of non-negative [[Real Number]] where $\sum M_k < \infty$, and let $\sum_{k=0}^{\infty} g_k$ be a [[Infinite Series of Functions]] defined on $S \subseteq \mathbb{R}$. If $|g_k(x)| \leq M_k$ for all $x \in S$ and for all $k \in \mathbb{N}$, then $\sum g_k$ [[Sequence of Function Uniform Convergence|converges uniformly]] on $S$.

> [!abstract] Theorem 2 (General Version)[^2]
> Suppose $\{f_n\}$ is a [[Sequence of Function]] defined on a [[Set]] $E$, and suppose
> $$
> \begin{align}
> |f_n(x)| \leq M_n \quad (x \in E, \; n = 1, 2, 3, \dots)
> \end{align}
> $$
> Then $\sum f_n$ converges uniformly on $E$ if $\sum M_n$ converges.

The converse is not true.[^2] The M-test also yields [[Absolutely Convergent Infinite Series|absolute convergence]] at each point, but uniform convergence in general does not imply absolute convergence.

# Properties
- Consequence of the [[Cauchy Criterion for Uniform Convergence Theorem]].
- Used to construct a [[Continuous Nowhere Differentiable Function Theorem|continuous nowhere differentiable function]].
- For series that do not converge absolutely, the uniform [[Dirichlet Test]] can be used instead.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=215)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=157&annotation=IL2W76J3)
