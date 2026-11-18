---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!info] Definition 1 (Geometric Sequence)[^1]
> A [[Sequence]] $\{a_n\}_{n=k}^{\infty}$ is geometric if there is a number $r$, the common ratio, such that
> $$
> \begin{align}
> a_{n+1} = r\, a_n \quad \text{for all } n \geq k
> \end{align}
> $$

> [!abstract] Theorem 2 (Explicit Formula)[^2]
> A geometric sequence with first term $a$ and common ratio $r \neq 0$ is
> $$
> \begin{align}
> a_n = a r^{n-1}, \quad n \geq 1
> \end{align}
> $$

# Properties
- The explicit formula follows from the recursion by [[Proof by Induction]].
- For $r > 0$, $a_n = \tfrac{a}{r} r^{n}$ is the restriction to $\mathbb{N}$ of an [[Exponential Function]] with base $r$: constant ratio of consecutive terms.
- Sum of the terms: [[Geometric Series]] (finite sum for $r \neq 1$, infinite sum for $|r| < 1$).
- Counterpart: [[Arithmetic Sequence]] (constant difference instead of constant ratio).

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=666)
[^2]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=668)
