---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Discontinuity)[^1]
> If $x$ is a point in the [[Domain]] of $f$ at which $f$ is not [[Continuous Function|continuous]], then $f$ is discontinuous at $x$, or $f$ has a discontinuity at $x$.

For $f$ defined on an interval or segment, discontinuities are classified by whether the [[One-Sided Limit of Function|one-sided limits]] $f(x^+), f(x^-)$ exist.

# Types
- [[Simple Discontinuity]] (discontinuity of the first kind): both $f(x^+)$ and $f(x^-)$ exist.
	- [[Jump Discontinuity]]: $f(x^+) \neq f(x^-)$.
	- Removable discontinuity: $f(x^+) = f(x^-) \neq f(x)$.
- [[Discontinuity of the Second Kind]]: at least one of $f(x^+), f(x^-)$ does not exist.

# Properties
- A [[Monotonic Function]] has only simple discontinuities ([[Monotonic Function One-Sided Limit Theorem]]), and at most countably many of them ([[Monotonic Function Discontinuity Countable Theorem]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=103)
