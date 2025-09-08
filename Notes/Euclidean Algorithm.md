---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Euclidean Algorithm)
> [[Function]] $F: \mathbb{Z}^2 \rightarrow \mathbb{Z}^2$ defined as
> $$
> \begin{align}
> F(m, n) = \begin{cases}
> (n, r),\ \text{where}\ r = rem_n(m) & \text{if}\ n \neq 0 \\
> (|m|, 0) & \text{if}\ n = 0
> \end{cases}
> \end{align}
> $$

The algorithm is to iterate $F$ until stable. The algorithm is guaranteed to halt.

After first iteration, the second value of the ordered pair always becomes non-negative.

> [!example]- Examples 2 (Euclidean Algorithm)
> > [!example]- Example 2.1
> ![[Screenshot 2025-06-24 164953.png]]

[^1]: [Algebra - Abstract and Concrete](zotero://open-pdf/library/items/IQ3GJ7PV?page=15)