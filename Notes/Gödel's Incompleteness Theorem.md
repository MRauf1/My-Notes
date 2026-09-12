---
tags:
  - computer_science
  - theoretical_computer_science
---

# Definition
> [!info] Gödel's (First) Incompleteness Theorem[^1]
> For any consistent formal theory $T$ at least as expressive as Peano arithmetic, there exists a sentence $G$ in the language of $T$ such that neither $G$ nor $\neg G$ is provable in $T$:
> $$
> T \nvdash G \quad \text{and} \quad T \nvdash \neg G.
> $$
> That is, there exist statements which are true but have no proof within $T$.

# Types
- Second Incompleteness Theorem - a consistent theory $T$ (as above) cannot prove its own consistency.

# Properties
- Implies that some functions on the integers cannot be represented by any algorithm, i.e., cannot be computed, motivating the study of [[Computability]].

[^1]: [Russell and Norvig, 2022, p. 27](zotero://open-pdf/library/items/JZXT5DZQ?page=27&annotation=9XJRVKBE)
