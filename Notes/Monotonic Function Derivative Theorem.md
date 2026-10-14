---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Monotonicity from the Sign of the Derivative)[^1]
> Suppose $f$ is differentiable in $(a, b)$.
> - If $f'(x) \geq 0$ for all $x \in (a, b)$, then $f$ is monotonically increasing.
> - If $f'(x) = 0$ for all $x \in (a, b)$, then $f$ is constant.
> - If $f'(x) \leq 0$ for all $x \in (a, b)$, then $f$ is monotonically decreasing.

"Monotonically increasing" is in the non-strict sense of [[Monotonic Function]]. Strict signs $f' > 0$ ($f' < 0$) give strictly [[Increasing Function|increasing]] ([[Decreasing Function|decreasing]]) functions.

# Properties
- Follows from the [[Mean Value Theorem]]: $f(x_2) - f(x_1) = (x_2 - x_1) f'(x)$ for some $x \in (x_1, x_2)$.
- The middle case is the [[Zero Derivative Implies Constant Function Theorem]].
- Applied to $f'$, it gives the derivative tests for [[Convex Function Basic Properties|convexity]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=117&annotation=6ZVETPYS)
