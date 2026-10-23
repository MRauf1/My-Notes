---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Principle of Transfinite Induction[^1]
> Let $X$ be a [[Well-Ordered Set|well ordered set]]. If $A \subseteq X$ is such that $x \in A$ whenever $I_x \subseteq A$ (where $I_x$ is the [[Initial Segment]] of $x$), then $A = X$.

The general case of [[Proof by Strong Induction]]: taking $X = \mathbb{N}$, "$I_n \subseteq A \implies n \in A$" is exactly the strong induction step, and no separate base case is needed since $I_{\min X} = \emptyset$.

# Properties
- Proof: if $A \neq X$, the [[Well-Ordered Set|well ordering]] gives a minimal $x \in X \setminus A$; then $I_x \subseteq A$, so $x \in A$, a contradiction.
- Combined with the [[Well Ordering Principle (Set Theory)|well ordering principle]], it allows inductive constructions over arbitrary sets.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=22&annotation=KMRMP3Z9)
