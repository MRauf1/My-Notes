---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Initial Segment[^1]
> Let $X$ be a [[Well-Ordered Set|well ordered set]]. The initial segment of $x \in X$ is
> $$
> \begin{align}
> I_x = \{y \in X : y < x\}.
> \end{align}
> $$
> The elements of $I_x$ are called the predecessors of $x$.

# Properties
> [!abstract] Proposition (Unions of Initial Segments)[^2]
> If $X$ is well ordered and $A \subseteq X$, then $\bigcup_{x \in A} I_x$ is either an initial segment or $X$ itself.

- Hypothesis "$I_x \subseteq A$" is the inductive hypothesis of the [[Principle of Transfinite Induction]].
- Used to compare well-ordered sets in the [[Well-Ordered Set Comparability Theorem]].
- The [[Set of Countable Ordinals]] is characterized as the uncountable well-ordered set all of whose initial segments are countable.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=22&annotation=AF4R99XH)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=22&annotation=78WQTLHE)
