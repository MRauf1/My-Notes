---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Derivative Limit Theorem)[^1]
> Let $f$ be continuous at $c$ and differentiable in a punctured neighborhood of $c$. If $\lim_{x \rightarrow c} f'(x) = L$, then $f'(c)$ exists and $f'(c) = L$.

Continuity at $c$ is essential. If the limit of $f'$ exists, then $f'$ is continuous at $c$. This agrees with [[Darboux's Theorem]]: a derivative cannot have a [[Simple Discontinuity|removable or jump discontinuity]].

# Properties
- Follows from the [[Mean Value Theorem]] applied on $[c, x]$.
- One-sided version: if $\lim_{x \rightarrow c^+} f'(x) = L$, then the right-hand derivative at $c$ is $L$.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=124&annotation=DP2EP7N9)
