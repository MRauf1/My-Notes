---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!abstract] Theorem 1 (LU Decomposition)[^1]
> 1) Reduce $A$ to an [[Upper Triangular Matrix]] using [[Row Operations]] R1 only. If this succeeds, call the result $U$. If it fails, then $A$ does not have an LU Decomposition.
> 2) Define $L$ as a [[Lower Triangular Matrix]] with 1s on the diagonal and $-c$ in the $(i, j)$th entry if, during the elimination process, $c$ times row $j$ was added to row $i$.
> 3) $A = LU$

Not every [[Matrix]] has an LU Decomposition.

This decomposition can be used to solve linear systems in a fast and stable (not as susceptible to round-off errors) manner.

# Types
- [[LUP Decomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=128)