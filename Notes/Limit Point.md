---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Limit Point)[^1]
> Let $(X, d)$ be a [[Metric Space]] and $E \subseteq X$. A point $p \in X$ is a limit point of $E$ if every [[Epsilon Neighborhood|neighborhood]] of $p$ contains a point $q \neq p$ such that $q \in E$.

A limit point need not belong to $E$ itself — it only requires that every neighborhood of $p$, no matter how small, contains some *other* point of $E$. Contrast with an [[Isolated Point]], which must belong to $E$ by definition.

> [!abstract] Theorem 2 (Limit Point Has Infinitely Many Nearby Points)[^2]
> If $p$ is a limit point of $E$, then every neighborhood of $p$ contains infinitely many points of $E$.

> [!abstract] Corollary 3 (Finite Set Has No Limit Points)[^3]
> A finite [[Set|point set]] has no limit points.

My interpretation: because a [[Metric Space|metric space]] is continuous, having at least one other point of $E$ in *every* neighborhood of $p$ (however small) actually forces there to be infinitely many such points — no matter how far you zoom in on $p$, that microscopic neighborhood still contains a slice of $E$ packed with points. A limit point can lie inside $E$ or outside it (much like a boundary point).

# Properties
- Every [[Interior Point]] of $E$ in $\mathbb{R}$ or $\mathbb{R}^k$ (under the standard Euclidean metric) is a limit point of $E$ — see [[Interior Point]].
- [[Closed Set]]
- [[Closure Set]]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=41)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=41)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=42)
