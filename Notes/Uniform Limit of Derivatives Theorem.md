---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Sequence of Function Uniform Convergence|Uniform Convergence]] and [[Derivative|Differentiation]] Theorem)[^1]
> Suppose $\{f_n\}$ is a [[Sequence of Function]], [[Differentiable Function|differentiable]] on $[a, b]$, and such that $\{f_n(x_0)\}$ converges for some point $x_0$ on $[a, b]$. If $\{f_n'\}$ converges uniformly on $[a, b]$, then $\{f_n\}$ converges uniformly on $[a, b]$ to a function $f$, and
> $$
> \begin{align}
> f'(x) = \lim_{n \rightarrow \infty} f_n'(x) \quad (a \leq x \leq b)
> \end{align}
> $$

Uniform convergence of $\{f_n\}$ alone is not enough: the hypothesis is placed on the derivatives $\{f_n'\}$, not on $\{f_n\}$. Indeed, a uniform limit of differentiable functions may be nowhere differentiable ([[Continuous Nowhere Differentiable Function Theorem]]).

If the continuity of the $f_n'$ is assumed in addition, a much shorter proof follows from the [[Uniform Limit of Integrals Theorem]] and the [[Fundamental Theorem of Calculus]].[^2]

# Properties
- [[Derivative of Power Series]] (term-by-term differentiation of [[Power Series]])
- [[Uniform Convergence Interchange of Limits Theorem]]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=161&annotation=A4ED8RYG)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=162&annotation=NPV6928P)
