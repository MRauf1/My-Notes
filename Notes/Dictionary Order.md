---
tags:
  - mathematics
  - topology
---

# Definition
> [!info] Dictionary Order[^1]
> Let $A$ and $B$ be [[Set|sets]] with [[Strict Total Order|order relations]] $<_A$ and $<_B$. The dictionary (lexicographic) order relation $<$ on the [[Cartesian Product]] $A \times B$ is defined by
> $$
> \begin{align}
> a_1 \times b_1 < a_2 \times b_2 \iff a_1 <_A a_2, \quad \text{or} \quad a_1 = a_2 \text{ and } b_1 <_B b_2.
> \end{align}
> $$

Pairs are compared by their first coordinate, and the second coordinate is only consulted to break ties, exactly as words are ordered in a dictionary.

# Properties
- If $<_A$ and $<_B$ are order relations ([[Strict Total Order|strict total orders]]), so is the dictionary order on $A \times B$.
- If $A$ and $B$ are [[Well-Ordered Set|well-ordered]], then $A \times B$ is well-ordered in the dictionary order.[^2]
- $\mathbb{R} \times \mathbb{R}$ in the dictionary order is not a [[Linear Continuum]] (it fails the least upper bound property), but $[0, 1] \times [0, 1]$ (the ordered square) is.

[^1]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=28&annotation=E9PQ5IQA)
[^2]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=66&annotation=IU4FE3CL)
