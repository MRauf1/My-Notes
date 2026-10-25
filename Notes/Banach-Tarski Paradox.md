---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!abstract] Banach-Tarski Paradox[^1]
> Let $U$ and $V$ be arbitrary bounded [[Open Set|open sets]] in $\mathbb{R}^n$, $n \geq 3$. There exist $k \in \mathbb{N}$ and subsets $E_1, \dots, E_k, F_1, \dots, F_k$ of $\mathbb{R}^n$ such that
> - the $E_j$ are disjoint and $\bigcup_j E_j = U$,
> - the $F_j$ are disjoint and $\bigcup_j F_j = V$,
> - $E_j$ is congruent to $F_j$ for $j = 1, \dots, k$.

Thus a ball the size of a pea can be cut into finitely many pieces and rearranged into a ball the size of the earth. The pieces cannot be visualized and their construction depends on the [[Axiom of Choice]]. Proved by Banach and Tarski in 1924.

**The measure problem.** Ideally one would like $\mu : \mathcal{P}(\mathbb{R}^n) \to [0, \infty]$ such that[^2]
1. $\mu(E_1 \cup E_2 \cup \cdots) = \mu(E_1) + \mu(E_2) + \cdots$ for disjoint $E_j$ (finite or countable),
2. $\mu(E) = \mu(F)$ whenever $E$ is congruent to $F$ (related by translations, rotations, reflections),
3. $\mu(Q) = 1$ for the unit cube $Q = \{x : 0 \leq x_j < 1,\ j = 1, \dots, n\}$.

These conditions are mutually inconsistent (already for $n = 1$, via the [[Vitali Set]]).[^3] Banach–Tarski says more: for $n \geq 3$ there is no $\mu$ on $\mathcal{P}(\mathbb{R}^n)$ that is positive and finite on bounded open sets and satisfies (1) for *finite* sequences together with (2).[^1]

The remedy is to give up defining $\mu$ on all subsets and settle for a [[Sigma-Field|$\sigma$-algebra]] containing every set one meets in practice ([[Borel Sigma-Algebra]], Lebesgue measurable sets).[^4]

# Properties
- Motivates restricting [[Measure (Measure Theory)|measures]] to $\sigma$-algebras rather than the full [[Power Set]].
- Relies on the [[Axiom of Choice]]; without choice, such non-measurable decompositions need not exist.
- Only uncountable spaces are affected: on a countable $X$ every subset can be measured consistently ([[Counting Measure]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=33&annotation=MTI85C9G)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=32&annotation=NJDWDFER)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=33&annotation=KX4LGJQY)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=34&annotation=VWLRVIAA)
