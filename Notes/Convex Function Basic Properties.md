---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Theorem 1 (First-Derivative Test)[^1][^3]
> If $f$ is differentiable on $(a, b)$, then
> - $f$ is [[Convex Function]] if and only if $f'(x) \leq f'(y)$ for all $a < x < y < b$ ($f'$ nondecreasing)
> - $f$ is strictly convex if and only if $f'(x) < f'(y)$ for all $a < x < y < b$ ($f'$ strictly increasing)

> [!abstract] Theorem 2 (Second-Derivative Test)[^1][^3]
> If $f$ is twice differentiable on $(a, b)$, then
> - $f$ is [[Convex Function]] if and only if $f''(x) \geq 0$ for all $a < x < b$
> - $f$ is strictly convex if $f''(x) > 0$ for all $a < x < b$

The strict second-derivative condition is only sufficient, not necessary: $f(x) = x^4$ is strictly convex on $\mathbb{R}$, yet $f''(0) = 0$.

> [!abstract] Theorem 3 (Continuity)[^2]
> Every [[Convex Function]] on an open interval $(a, b)$ is [[Continuous Function|continuous]].

> [!abstract] Theorem 4 (Composition)[^2]
> If $f$ is convex and $g$ is increasing and convex, then $g \circ f$ is convex.

# Properties
- Theorem 2 follows from Theorem 1 via [[Monotonic Function Derivative Theorem]] applied to $f'$.
- These tests are the usual way to verify the hypothesis of [[Jensen's Inequality]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=97)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=110)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=124&annotation=Z2Q4JR3F)
