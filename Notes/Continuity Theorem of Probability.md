---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Continuity Theorem of Probability[^1]
> Let $\{C_n\}$ be a [[Nondecreasing Sequence of Sets|nondecreasing sequence]] of [[Event|events]]. Then
> $$
> \begin{align}
> \lim_{n\to\infty} P(C_n) = P\left(\lim_{n\to\infty} C_n\right) = P\left(\bigcup_{n=1}^\infty C_n\right)
> \end{align}
> $$
> Let $\{C_n\}$ be a [[Nonincreasing Sequence of Sets|nonincreasing sequence]] of events. Then
> $$
> \begin{align}
> \lim_{n\to\infty} P(C_n) = P\left(\lim_{n\to\infty} C_n\right) = P\left(\bigcap_{n=1}^\infty C_n\right)
> \end{align}
> $$

The limit and $P$ can be interchanged, i.e. $P$ is continuous along monotone sequences of events. It follows from countable additivity of [[Probability]] by writing $\bigcup_n C_n$ as the [[Disjoint Set Union]] of the rings $C_1, C_2 \cap C_1^c, C_3 \cap C_2^c, \dots$; the nonincreasing case follows by taking [[Set Complement|complements]].

# Properties
- Used to prove [[Boole's Inequality]] and the right-continuity in [[Cumulative Distribution Function Basic Properties]].
- The measure-theoretic analogue is continuity from below/above of a [[Measure (Measure Theory)|measure]]; continuity from above requires finite measure, which holds automatically since $P(\mathcal{C}) = 1$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=35)
