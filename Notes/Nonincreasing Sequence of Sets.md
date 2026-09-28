---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Nonincreasing [[Sequence]] of [[Set]])[^1]
> [[Sequence]] of [[Set]] $(A_n)$ is nonincreasing (nested downward) if $A_n \supseteq A_{n+1}$ for $n \in \mathbb{N}$. Its limit is
> $$
> \begin{align}
> \lim_{n \to \infty} A_n = \bigcap_{n=1}^\infty A_n
> \end{align}
> $$

# Properties
- Counterpart of the [[Nondecreasing Sequence of Sets]]; complements of a nonincreasing sequence form a nondecreasing one.
- [[Continuity Theorem of Probability]]: $\lim_n P(A_n) = P\left(\bigcap_n A_n\right)$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=23)