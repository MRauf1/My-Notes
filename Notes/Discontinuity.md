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
	- [[Removable Discontinuity]]: $f(x^+) = f(x^-) \neq f(x)$.
- [[Discontinuity of the Second Kind]] (essential discontinuity): at least one of $f(x^+), f(x^-)$ does not exist (including being $\pm\infty$, an infinite discontinuity).

# Properties
- The set of discontinuities of a function may be discrete, dense, or even the entire domain.[^2]
- Bounded $f$ is Riemann integrable iff its discontinuity set has measure zero; for the [[Riemann-Stieltjes Integral]], $f$ and $\alpha$ must not share discontinuities ([[Functions that are Riemann-Stieltjes Integrable Theorem]]).
- A [[Monotonic Function]] has only simple discontinuities ([[Monotonic Function One-Sided Limit Theorem]]), and at most countably many of them ([[Monotonic Function Discontinuity Countable Theorem]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=103)
[^2]: [Classification of discontinuities — Wikipedia](https://en.wikipedia.org/wiki/Classification_of_discontinuities)
