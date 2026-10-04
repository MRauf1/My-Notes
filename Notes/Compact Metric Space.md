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

> [!abstract] Theorem 3 (Compactness Equivalence Theorem)
> A [[Metric Space]] $(S, d)$ is compact if and only if it is both [[Complete Metric Space|complete]] and [[Totally Bounded|totally bounded]].

My interpretation: compactness always implies completeness (Theorem 2 above means every Cauchy sequence, having a convergent subsequence, must itself converge), but the converse fails — completeness alone says nothing about boundedness. For example, $\mathbb{R}$ (with the standard metric) is complete, but not compact, since it is unbounded (hence not totally bounded).

# Properties
- Every [[Compact Metric Space|compact metric space]] is [[Complete Metric Space|complete]], but not conversely.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=102)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=60)