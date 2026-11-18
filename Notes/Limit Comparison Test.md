---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Limit Comparison Test)[^1]
> Suppose $\sum a_n$ and $\sum b_n$ have positive terms. If
> $$
> \begin{align}
> \lim_{n \to \infty} \frac{a_n}{b_n} = c, \qquad 0 < c < \infty
> \end{align}
> $$
> then either both series converge or both diverge.

# Properties
- Proof: for large $n$, $\frac{c}{2} b_n < a_n < \frac{3c}{2} b_n$, so the [[Infinite Series Comparison Test]] applies in both directions.
- Usually compared against a [[p-Series]] or [[Geometric Series]] with the same dominant terms.
- Edge cases: $c = 0$ with $\sum b_n$ convergent implies $\sum a_n$ converges; $c = \infty$ with $\sum b_n$ divergent implies $\sum a_n$ diverges.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=761)
