---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Vitali Set[^1]
> Define the equivalence relation $x \sim y \iff x - y \in \mathbb{Q}$ on $[0, 1)$. Using the [[Axiom of Choice]], pick exactly one element from each equivalence class; the resulting set $N \subseteq [0, 1)$ is a Vitali set.

For $r \in \mathbb{Q} \cap [0, 1)$ let $N_r$ be the translate of $N$ by $r$ modulo $1$. The $N_r$ are disjoint and $[0, 1) = \bigcup_{r} N_r$ is a **countable** union. If $\mu$ were a countably additive, translation-invariant measure on all of $\mathcal{P}(\mathbb{R})$ with $\mu([0,1)) = 1$, then
$$
\begin{align}
1 = \mu([0,1)) = \sum_{r \in \mathbb{Q} \cap [0,1)} \mu(N_r) = \sum_{r \in \mathbb{Q} \cap [0,1)} \mu(N),
\end{align}
$$
a countable sum of one constant, which is $0$ if $\mu(N) = 0$ and $\infty$ if $\mu(N) > 0$. Contradiction: $N$ cannot be assigned a measure.

The difficulty is structural, not about size: $N$ is uncountable, but so is a co-countable set, which is perfectly measurable ([[Countable-Cocountable Sigma-Algebra]]). $N$ is non-constructive and scattered across $[0,1)$ so evenly that translation invariance and countable additivity clash.

# Properties
- Not Lebesgue measurable; it is the one-dimensional instance of the inconsistency of the measure problem ([[Banach-Tarski Paradox]]).
- Its existence depends on the [[Axiom of Choice]].
- Requires an uncountable ambient space: on a countable set every subset is measurable.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=33)
