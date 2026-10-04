---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Mertens' Theorem)[^1]
> Suppose $\sum_{n=0}^\infty a_n$ converges [[Absolutely Convergent Infinite Series|absolutely]] to $A$, and $\sum_{n=0}^\infty b_n$ converges to $B$. Let $\sum_{n=0}^\infty c_n$ be their [[Cauchy Product]], i.e. $c_n = \sum_{k=0}^n a_k b_{n-k}$. Then $\sum_{n=0}^\infty c_n$ converges to $AB$.

That is, the Cauchy product of two convergent series converges, and to the correct value $AB$, provided at least one of the two factors converges absolutely.

> [!abstract] Theorem 2 (Companion Result: Convergence of the Product Forces the Right Value)[^2]
> If $\sum a_n$, $\sum b_n$, and their [[Cauchy Product]] $\sum c_n$ all three converge, to $A$, $B$, and $C$ respectively (with no assumption of absolute convergence on either factor), then $C = AB$.

Theorem 2 has a weaker hypothesis on $\sum a_n, \sum b_n$ than Mertens' theorem (no absolute convergence required), but a stronger hypothesis overall, since it additionally assumes $\sum c_n$ converges rather than deriving it.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=83)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=84)
