---
tags:
  - mathematics
  - measure_theory
  - topology
---

# Definition
> [!info] Well-Ordered Set[^1]
> A [[Set]] $X$ is well ordered by $\leq$ if $\leq$ is a [[Total Order|linear (total) order]] on $X$ and every nonempty [[Subset]] of $X$ has a (necessarily unique) minimal element. The relation $\leq$ is then called a well ordering on $X$.

Since the order is linear, the minimal element of a subset is in fact its smallest element. $\mathbb{N}$ with its natural ordering is well ordered (see [[Well Ordering Principle]]), whereas $\mathbb{Z}$, $\mathbb{Q}$, and $[0, 1]$ with their usual orderings are not.

> [!info] Well-Ordered Set (Strict Order Form)[^2]
> A set $A$ with an order relation $<$ (a [[Strict Total Order]]) is well-ordered if every nonempty subset of $A$ has a smallest element.

# Properties
- If $A$ is well-ordered, any subset of $A$ is well-ordered in the restricted order relation.[^3]
- If $A$ and $B$ are well-ordered, then $A \times B$ is well-ordered in the [[Dictionary Order]].[^4]

> [!abstract] Theorem 10.1 (Finite Ordered Sets)[^5]
> Every nonempty finite ordered set has the order type ([[Order Isomorphism|order isomorphic]]) of a section $\{1, \dots, n\}$ of $\mathbb{Z}^+$, so it is well-ordered.

- Every nonempty set admits a well ordering: [[Well Ordering Principle (Set Theory)]].
- Each element $x$ determines an [[Initial Segment]] $I_x = \{y : y < x\}$.
- Proofs over well-ordered sets proceed by [[Principle of Transfinite Induction|transfinite induction]].
- Any two well-ordered sets are comparable: [[Well-Ordered Set Comparability Theorem]].
- The [[Set of Countable Ordinals]] is the canonical uncountable well-ordered set all of whose initial segments are countable.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=18&annotation=8TF8Y9PF)
[^2]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=65&annotation=HBD79LE9)
[^3]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=65&annotation=A2VGA6D9)
[^4]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=66&annotation=IU4FE3CL)
[^5]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=66&annotation=S5N8YXJQ)
