---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Bonferroni's Inequality[^1]
> For [[Event|events]] $C_1, C_2$,
> $$
> \begin{align}
> P(C_1 \cap C_2) \geq P(C_1) + P(C_2) - 1
> \end{align}
> $$
> More generally, for events $C_1, \dots, C_k$,
> $$
> \begin{align}
> P\left(\bigcap_{i=1}^k C_i\right) \geq \sum_{i=1}^k P(C_i) - (k-1)
> \end{align}
> $$

Proof: apply [[Boole's Inequality]] to the complements, $P\left(\bigcup_i C_i^c\right) \leq \sum_i \left(1 - P(C_i)\right)$, and use [[DeMorgan's Laws]].

# Properties
- Gives a lower bound on the probability that all events occur simultaneously; this is the basis of the Bonferroni correction for simultaneous [[Confidence Interval|confidence intervals]] (each at level $1 - \alpha/k$ gives joint coverage $\geq 1 - \alpha$).
- Belongs to the family of Bonferroni bounds obtained by truncating the [[Probability of Set Union|inclusion-exclusion formula]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=36)
