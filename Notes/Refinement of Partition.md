---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Refinement of [[Partition]])[^1]
> A [[Partition]] $P^*$ of $[a, b]$ is a refinement of $P$ if $P^* \supseteq P$ (every point of $P$ is a point of $P^*$). Given two partitions $P_1, P_2$, their common refinement is $P^* = P_1 \cup P_2$.

# Properties
- Refining increases lower sums and decreases upper sums: $L(P, f, \alpha) \leq L(P^*, f, \alpha)$ and $U(P^*, f, \alpha) \leq U(P, f, \alpha)$ ([[Darboux Sums of 2 Partitions Lemma]]).
- Common refinements are the standard tool for comparing sums over two unrelated partitions, e.g. proving $\underline{\int} f\,d\alpha \leq \overline{\int} f\,d\alpha$ in the [[Riemann-Stieltjes Integral]].
- A refinement satisfies $\text{mesh}(P^*) \leq \text{mesh}(P)$ ([[Mesh of Partition]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=132&annotation=NV3V4IQL)
