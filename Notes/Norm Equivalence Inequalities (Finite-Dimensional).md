---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 ($\infty$-Norm and 2-Norm)[^1]
> If $x \in \mathbb{C}^n$, then
> $$
> \lVert x \rVert_\infty \leq \lVert x \rVert_2 \leq \sqrt{n} \lVert x \rVert_\infty
> $$

> [!abstract] Theorem 2 (2-Norm and 1-Norm)[^1]
> If $x \in \mathbb{C}^n$, then
> $$
> \lVert x \rVert_2 \leq \lVert x \rVert_1 \leq \sqrt{n} \lVert x \rVert_2
> $$

> [!abstract] Theorem 3 ($\infty$-Norm and 1-Norm)[^2]
> If $x \in \mathbb{C}^n$, then
> $$
> \lVert x \rVert_\infty \leq \lVert x \rVert_1 \leq n \lVert x \rVert_\infty
> $$

These inequalities show that the [[Infinity Norm]], [[Vector Norm|2-norm]], and [[1-Norm]] are all equivalent on the finite-dimensional space $\mathbb{C}^n$: for a given $n$, any two differ by at most a constant, so if one is small, all are proportionally small. Indeed, all [[p-Norm|p-norms]] are equivalent in this sense.[^2]

# Properties
- [[p-Norm]]
- [[Operator Norm and Frobenius Norm Inequality]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=295)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=74)
