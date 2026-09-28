---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Theorem 1 (First-Derivative Test)[^1]
> If $f$ is differentiable on $(a, b)$, then
> - $f$ is [[Convex Function]] if and only if $f'(x) \leq f'(y)$ for all $a < x < y < b$ ($f'$ nondecreasing)
> - $f$ is strictly convex if and only if $f'(x) < f'(y)$ for all $a < x < y < b$ ($f'$ strictly increasing)

> [!abstract] Theorem 2 (Second-Derivative Test)[^1]
> If $f$ is twice differentiable on $(a, b)$, then
> - $f$ is [[Convex Function]] if and only if $f''(x) \geq 0$ for all $a < x < b$
> - $f$ is strictly convex if $f''(x) > 0$ for all $a < x < b$

The strict second-derivative condition is only sufficient, not necessary: $f(x) = x^4$ is strictly convex on $\mathbb{R}$, yet $f''(0) = 0$.

# Properties
- These tests are the usual way to verify the hypothesis of [[Jensen's Inequality]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=97)
