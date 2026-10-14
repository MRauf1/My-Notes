---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Darboux's Theorem)[^1]
> Suppose $f$ is a real [[Differentiable Function]] on $[a, b]$ and suppose $f'(a) < \lambda < f'(b)$. Then there is a point $x \in (a, b)$ such that $f'(x) = \lambda$. A similar result holds if $f'(a) > f'(b)$.

A [[Derivative]] that exists at every point of an interval need not be continuous, but it still has the intermediate value property shared by continuous functions ([[Intermediate Value Theorem]]). Consequently, not every function is a derivative.[^2]

> [!abstract] Corollary 2 (No Simple Discontinuities)[^3]
> If $f$ is differentiable on $[a, b]$, then $f'$ cannot have any [[Simple Discontinuity|simple discontinuities]] on $[a, b]$. However, $f'$ may have [[Discontinuity of the Second Kind|discontinuities of the second kind]].

# Properties
- Intermediate value theorem for derivatives; compare Theorem 3 of [[Intermediate Value Theorem]].
- Proved via [[Extreme Value Theorem]] and [[Fermat's Theorem]] applied to $g(t) = f(t) - \lambda t$.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=117&annotation=T7TNH3WT)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=117&annotation=URUMJ35M)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=118&annotation=J2TELJAV)
