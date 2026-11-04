---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Boole's Inequality (Union Bound)[^1]
> Let $\{C_n\}$ be an arbitrary sequence of [[Event|events]]. Then
> $$
> \begin{align}
> P\left(\bigcup_{n=1}^\infty C_n\right) \leq \sum_{n=1}^\infty P(C_n)
> \end{align}
> $$

Equality holds when the events are [[Mutually Exclusive Events|mutually exclusive]] (countable additivity of [[Probability]]); overlaps are counted more than once on the right-hand side.

# Properties
- Also called countable subadditivity; the finite case follows from the [[Probability of Set Union]] by induction, the countable case from the [[Continuity Theorem of Probability]].
- It is the first of the Bonferroni bounds from the [[Probability of Set Union|inclusion-exclusion formula]]; applied to complements it gives [[Bonferroni's Inequality]].
- Turns guarantees for each fixed object into simultaneous guarantees: if each of $K$ bad events has probability at most $\delta/K$, none occurs with probability at least $1 - \delta$. Combined with [[Hoeffding's Inequality]], this gives the [[Uniform Sampling Simple Regret Bound]] and the [[Finite Hypothesis Class Generalization Bound]] (via a [[Uniform Deviation Bound]]).[^2]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=35)
[^2]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 3](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=3)
