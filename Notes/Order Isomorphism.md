---
tags:
  - mathematics
  - measure_theory
  - topology
---

# Definition
> [!info] Order Isomorphism[^1]
> Two [[Partial Order|partially ordered sets]] $X$ and $Y$ are order isomorphic if there is a [[Bijective Function|bijection]] $f: X \to Y$ such that
> $$
> \begin{align}
> x_1 \leq x_2 \iff f(x_1) \leq f(x_2).
> \end{align}
> $$

An order isomorphism is an isomorphism in the category of partially ordered sets: it preserves and reflects the ordering, so $X$ and $Y$ are indistinguishable as ordered sets.

> [!info] Same Order Type[^2]
> Sets $A$ and $B$ with order relations $<_A$ and $<_B$ ([[Strict Total Order|strict total orders]]) have the same order type if there exists a [[Bijective Function|bijection]] $f: A \to B$ such that
> $$
> \begin{align}
> a_1 <_A a_2 \implies f(a_1) <_B f(a_2).
> \end{align}
> $$

For total orders, preserving the order already implies reflecting it (by trichotomy), so "same order type" is exactly order isomorphism.

# Properties
- Order isomorphism is an [[Equivalence Relation]] on partially ordered sets.
- Any two [[Well-Ordered Set|well ordered sets]] are comparable up to order isomorphism: see [[Well-Ordered Set Comparability Theorem]].
- The [[Set of Countable Ordinals]] is unique up to order isomorphism.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=18&annotation=SAT5CLVJ)
[^2]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=27&annotation=U4KSZ6E5)
