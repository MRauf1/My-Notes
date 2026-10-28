---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Complete [[Metric Space]])[^1]
> [[Metric Space]] $(S, d)$ is complete if every [[Cauchy Sequence]] in $S$ converges to some element $s \in S$.

Equivalently, in a complete metric space a sequence is a [[Cauchy Sequence]] if and only if it is a [[Convergent Sequence]] (convergent $\implies$ Cauchy holds in every metric space, see [[Convergent Sequence is Cauchy Sequence]]). In an incomplete space, a Cauchy sequence may fail to converge because the point it approaches is missing from the space.

Related to [[Completeness Axiom]] and ensures that the space is complete (has no gaps).

# Properties
- Every metric space is isometric to a [[Dense Subset]] of a complete metric space ([[Completion of Metric Space]]).
- The [[Space of Bounded Continuous Functions]] $\mathscr{C}(X)$ is complete under the [[Supremum Norm]].
- [[Complete Metric Space Theorem]]
- [[Baire Category Theorem]]
- [[Compact Metric Space|Compact metric spaces]] are complete.[^2]
- $\mathbb{R}$, [[Set of Complex Numbers|$\mathbb{C}$]], and $\mathbb{R}^k$ (any [[Euclidean n-Space|Euclidean space]]) are complete — this is the Cauchy criterion for convergence in $\mathbb{R}^k$.[^2]
- Every [[Closed Set|closed]] subset $E$ of a complete metric space $X$ is itself complete: any [[Cauchy Sequence]] in $E$ is a Cauchy sequence in $X$, hence converges to some $p \in X$, and $p \in E$ since $E$ is closed.[^2]
- Conversely, a complete subset of an arbitrary metric space is [[Closed Set|closed]]: if $x_n \to x$ with $x_n \in E$, then $\{x_n\}$ is Cauchy, so its limit lies in $E$.[^3]
- The [[Set of Rational Numbers|rationals]] $\mathbb{Q}$, with $d(x,y) = |x - y|$, are NOT complete: a sequence of rationals converging (in $\mathbb{R}$) to an irrational number, such as $\sqrt{2}$, is Cauchy in $\mathbb{Q}$ but has no limit in $\mathbb{Q}$.[^2]
- Open intervals such as $(0, 1)$, with the usual metric, are NOT complete: $(1/n)$ is Cauchy but its limit $0 \notin (0, 1)$. This is consistent with $(0,1)$ not being [[Closed Set|closed]] in $\mathbb{R}$.
- Completeness does not imply [[Compact Metric Space|compactness]]: $\mathbb{R}$ is complete but not compact, since it is unbounded (hence not [[Totally Bounded|totally bounded]]). See [[Compact Metric Space]] for the full compact $\iff$ complete + totally bounded equivalence.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=97)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=62)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=27&annotation=FV8NNTV6)
