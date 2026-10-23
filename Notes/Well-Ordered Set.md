---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Well-Ordered Set[^1]
> A [[Set]] $X$ is well ordered by $\leq$ if $\leq$ is a [[Total Order|linear (total) order]] on $X$ and every nonempty [[Subset]] of $X$ has a (necessarily unique) minimal element. The relation $\leq$ is then called a well ordering on $X$.

Since the order is linear, the minimal element of a subset is in fact its smallest element. $\mathbb{N}$ with its natural ordering is well ordered (see [[Well Ordering Principle]]), whereas $\mathbb{Z}$, $\mathbb{Q}$, and $[0, 1]$ with their usual orderings are not.

# Properties
- Every nonempty set admits a well ordering: [[Well Ordering Principle (Set Theory)]].
- Each element $x$ determines an [[Initial Segment]] $I_x = \{y : y < x\}$.
- Proofs over well-ordered sets proceed by [[Principle of Transfinite Induction|transfinite induction]].
- Any two well-ordered sets are comparable: [[Well-Ordered Set Comparability Theorem]].
- The [[Set of Countable Ordinals]] is the canonical uncountable well-ordered set all of whose initial segments are countable.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=18&annotation=8TF8Y9PF)
