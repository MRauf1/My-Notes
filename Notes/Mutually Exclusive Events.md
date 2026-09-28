---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition
> [!info] Mutually Exclusive Events[^1][^2]
> A (finite or [[Countable Set|countable]]) collection of [[Event|events]] $A_1, A_2, \dots$ is mutually exclusive if its members are pairwise [[Disjoint Sets|disjoint]]: $A_m \cap A_n = \emptyset$ for all $m \neq n$. Its union is then a [[Disjoint Set Union|disjoint union]].

# Properties
- The third axiom of [[Probability]]: $P\left(\bigcup_n A_n\right) = \sum_n P(A_n)$ for mutually exclusive events.
- A mutually exclusive collection that is also [[Exhaustive Events|exhaustive]] forms a [[Partition]] of the [[Sample Space]].
- Mutually exclusive events with positive probabilities are never [[Independent Events|independent]], since $P(A \cap B) = 0 \neq P(A)P(B)$.

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=12)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=28)
