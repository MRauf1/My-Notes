---
tags:
  - mathematics
  - topology
---

# Definition
> [!info] Inductive Set[^1]
> A [[Subset]] $A \subseteq \mathbb{R}$ is inductive if
> 1. $1 \in A$, and
> 2. $x \in A \implies x + 1 \in A$.

> [!info] Set of Positive Integers[^1]
> Let $\mathcal{A}$ be the collection of all inductive subsets of $\mathbb{R}$. The [[Set of Natural Numbers|set of positive integers]] is
> $$
> \begin{align}
> \mathbb{Z}^+ = \bigcap_{A \in \mathcal{A}} A.
> \end{align}
> $$

$\mathbb{Z}^+$ is the smallest inductive set: it is itself inductive, and it is contained in every inductive set. This is what makes [[Proof by Induction]] valid: if a set $A \subseteq \mathbb{Z}^+$ is inductive, then $A = \mathbb{Z}^+$.

# Properties
- Gives a construction of $\mathbb{Z}^+$ inside $\mathbb{R}$, as opposed to the axiomatic approach of the [[Peano Axioms]].
- $\mathbb{Z}^+$ is [[Well-Ordered Set|well-ordered]] ([[Well Ordering Principle]]).
- Sections $S_n = \{1, \dots, n - 1\}$ of $\mathbb{Z}^+$ are its [[Initial Segment|initial segments]].

[^1]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=34&annotation=H6KH7F97)
