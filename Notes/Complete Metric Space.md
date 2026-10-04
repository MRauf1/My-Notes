---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Complete [[Metric Space]])[^1]
> [[Metric Space]] $(S, d)$ is complete if every [[Cauchy Sequence]] in $S$ converges to some element $s \in S$.

Related to [[Completeness Axiom]] and ensures that the space is complete (has no gaps).

# Properties
- [[Complete Metric Space Theorem]]
- [[Baire Category Theorem]]
- [[Compact Metric Space|Compact metric spaces]] are complete.[^2]
- $\mathbb{R}^k$ (any [[Euclidean n-Space|Euclidean space]]) is complete — this is the Cauchy criterion for convergence in $\mathbb{R}^k$.[^2]
- Every [[Closed Set|closed]] subset $E$ of a complete metric space $X$ is itself complete: any [[Cauchy Sequence]] in $E$ is a Cauchy sequence in $X$, hence converges to some $p \in X$, and $p \in E$ since $E$ is closed.[^2]
- The [[Set of Rational Numbers|rationals]] $\mathbb{Q}$, with $d(x,y) = |x - y|$, are NOT complete: a sequence of rationals converging (in $\mathbb{R}$) to an irrational number, such as $\sqrt{2}$, is Cauchy in $\mathbb{Q}$ but has no limit in $\mathbb{Q}$.[^2]
- Completeness does not imply [[Compact Metric Space|compactness]]: $\mathbb{R}$ is complete but not compact, since it is unbounded (hence not [[Totally Bounded|totally bounded]]). See [[Compact Metric Space]] for the full compact $\iff$ complete + totally bounded equivalence.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=97)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=62)