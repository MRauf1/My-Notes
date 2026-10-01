---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Bounded [[Set]])[^1]
> A set $S$ is bounded if it's [[Set Upper Bound|bounded above]] and [[Set Lower Bound|bounded below]].
> In other words, $S$ is bounded if there exist [[Real Number]] $m, M$ such that $S \subseteq [m, M]$

> [!info] Definition 2 (Bounded [[Set]] in High Dimension)[^2]
> A [[Set]] $S$ in $\mathbb{R}^k$ is bounded if there exists $M > 0$ such that $\max\{|x_j| : j = 1, \dots, k\} \leq M$ for all $\mathbf{x} = (x_1, \dots, x_k) \in S$.

> [!info] Definition 3 (Bounded Set in a General [[Metric Space]])[^3]
> Let $(X, d)$ be a [[Metric Space]] and $E \subseteq X$. $E$ is bounded if there exists a real number $M$ and a point $q \in X$ such that $d(q, p) \leq M$ for all $p \in E$.
> $E$ is unbounded if no such $M$ and $q$ exist.

My interpretation: it is the set $E$ itself that has finite size, while the surrounding space $X$ can be unbounded. If $E$ can be "trapped" inside a ball of finite radius $M$ around just one vantage point $q \in X$, then $E$ does not escape to infinity. An unbounded set is one whose points spread out so far that no finite ball, centered anywhere in $X$, contains all of them — for example, $\mathbb{N} \subseteq \mathbb{R}$ is unbounded (see the [[Archimedean Property]]).

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=33)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=98)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=41)