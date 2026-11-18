---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Nor)[^1]
> $P \downarrow Q$ means "neither $P$ nor $Q$":
> $$
> \begin{align}
> P \downarrow Q \equiv \neg(P \lor Q) \equiv \neg P \land \neg Q
> \end{align}
> $$

# Properties
- Functionally complete: $\neg P \equiv P \downarrow P$, $P \lor Q \equiv (P \downarrow Q) \downarrow (P \downarrow Q)$, $P \land Q \equiv (P \downarrow P) \downarrow (Q \downarrow Q)$.
- Dual of [[Nand]]; the second form is [[DeMorgan's Laws]].

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=38)
