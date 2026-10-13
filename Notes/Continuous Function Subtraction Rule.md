---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 ([[Continuous Function]] [[Subtraction]] Rule)[^1]
> If [[Function]] $f, g$ are [[Continuous Function]] at $a$, then $f - g$ is also continuous at $a$.

> [!abstract] Theorem 2 (On [[Metric Space]])
> Let $f, g$ be [[Complex-Valued Function|complex]] continuous functions on a [[Metric Space]] $X$. Then $f - g$ is continuous on $X$.

Rudin's statement lists only $f + g$, $fg$, $f/g$,[^2] but $f - g$ follows: $f - g = f + (-1) \cdot g$, where the [[Constant Function]] $-1$ is continuous, so apply [[Continuous Function Product Rule]] then [[Continuous Function Addition Rule]]. Directly, $|(f - g)(x) - (f - g)(p)| \leq |f(x) - f(p)| + |g(x) - g(p)|$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=149)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=96)
