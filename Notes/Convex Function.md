---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Convex]] [[Function]])[^1]
> Function $f$ defined on $(a, b)$, $- \infty \leq a < b \leq \infty$ is said to be convex if for all $x, y \in (a, b)$ and for all $\gamma \in (0, 1)$,
> $$
> \begin{align}
> f(\gamma x + (1 - \gamma) y) \leq \gamma f(x) + (1 - \gamma) f(y)
> \end{align}
> $$
> $f$ is [[Strictly Convex Function]] if the above [[Inequality]] is strict.

# Properties
- Geometrically, every chord between two points on the graph lies above the function. A twice-differentiable function is convex if its [[Hessian Matrix]] is positive semidefinite everywhere (a positive definite Hessian gives strict convexity); a convex loss has a single [[Global Minimum]], making training relatively easy.[^2]
- [[Convex Function Basic Properties]]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=97)
[^2]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
