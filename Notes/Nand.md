---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Nand)[^1]
> $P \mid Q$ means "$P$ and $Q$ are not both true":
> $$
> \begin{align}
> P \mid Q \equiv \neg(P \land Q) \equiv \neg P \lor \neg Q
> \end{align}
> $$

# Properties
- Functionally complete: $\neg P \equiv P \mid P$, $P \land Q \equiv (P \mid Q) \mid (P \mid Q)$, $P \lor Q \equiv (P \mid P) \mid (Q \mid Q)$. This is why nand gates suffice to build any digital circuit.
- Dual of [[Nor]].

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=38)
