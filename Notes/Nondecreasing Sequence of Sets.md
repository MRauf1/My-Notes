---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Nondecreasing [[Sequence]] of [[Set]])[^1]
> [[Sequence]] of [[Set]] $(A_n)$ is nondecreasing (nested upward) if $A_n \subseteq A_{n+1}$ for $n \in \mathbb{N}$. Its limit is
> $$
> \begin{align}
> \lim_{n \to \infty} A_n = \bigcup_{n=1}^\infty A_n
> \end{align}
> $$

# Properties
- Counterpart of the [[Nonincreasing Sequence of Sets]]; together they are the monotone sequences of sets, the set analogue of a [[Monotone Sequence]].
- [[Continuity Theorem of Probability]]: $\lim_n P(A_n) = P\left(\bigcup_n A_n\right)$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=23)