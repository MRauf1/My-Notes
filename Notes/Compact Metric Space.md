---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Compact [[Metric Space]])[^1]
> [[Metric Space]] $(S, d)$ is compact if every [[Open Cover]] of $S$ has a finite [[Subcover]].

Every compact metric space is [[Closed Set]] and [[Bounded Set]].

> [!abstract] Theorem 2 (Sequences in Compact Metric Spaces)[^2]
> Let $(S, d)$ be a [[Compact Metric Space]] and $\{p_n\}$ a [[Sequence]] in $S$. Then some [[Subsequence]] of $\{p_n\}$ converges to a point of $S$.

> [!abstract] Theorem 3 (Compactness Equivalence Theorem)[^3]
> If $E$ is a subset of the [[Metric Space]] $(X, \rho)$, the following are equivalent:
> a. $E$ is [[Complete Metric Space|complete]] and [[Totally Bounded|totally bounded]].
> b. (Bolzano–Weierstrass property) Every [[Sequence]] in $E$ has a [[Subsequence]] that converges to a point of $E$.
> c. (Heine–Borel property) If $\{V_\alpha\}_{\alpha \in A}$ is an [[Open Cover|open cover]] of $E$, there is a finite $F \subseteq A$ such that $\{V_\alpha\}_{\alpha \in F}$ covers $E$.
> A set with these properties is called compact.[^4]

Every compact set is closed (a complete subset is closed) and bounded; the converse fails in general but holds in $\mathbb{R}^n$ ([[Heine-Borel Theorem]]). The names (b) and (c) generalize the [[Bolzano-Weierstrass Theorem]] and the [[Heine-Borel Theorem]].[^4]

My interpretation: compactness always implies completeness (Theorem 2 above means every Cauchy sequence, having a convergent subsequence, must itself converge), but the converse fails — completeness alone says nothing about boundedness. For example, $\mathbb{R}$ (with the standard metric) is complete, but not compact, since it is unbounded (hence not totally bounded).

# Properties
- Every [[Compact Metric Space|compact metric space]] is [[Complete Metric Space|complete]], but not conversely.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=102)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=60)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=28&annotation=EV7GX4AU)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=29&annotation=VHH538YN)
