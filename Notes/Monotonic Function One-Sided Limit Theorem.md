---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Monotonic Function]] [[One-Sided Limit of Function|One-Sided Limit]] Theorem)[^1]
> Let $f$ be monotonically increasing on $(a, b)$. Then $f(x^+)$ and $f(x^-)$ exist at every point $x \in (a, b)$, and
> $$
> \begin{align}
> \sup_{a < t < x} f(t) = f(x^-) \leq f(x) \leq f(x^+) = \inf_{x < t < b} f(t)
> \end{align}
> $$
> Furthermore, if $a < x < y < b$, then
> $$
> \begin{align}
> f(x^+) \leq f(y^-)
> \end{align}
> $$
> Analogous results hold for monotonically decreasing functions.

> [!abstract] Corollary 2[^1]
> Monotonic functions have no [[Discontinuity of the Second Kind|discontinuities of the second kind]].

The function analogue of the [[Bounded Monotone Sequence Convergence Theorem]]: monotonicity forces one-sided limits to exist as a [[Supremum]] and [[Infimum]], so every discontinuity of a monotonic function is a [[Jump Discontinuity]].

# Properties
- Implies [[Monotonic Function Discontinuity Countable Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=104)
