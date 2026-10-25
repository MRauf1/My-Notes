---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Arzelà-Ascoli Theorem)[^1]
> If $K$ is [[Compact Metric Space|compact]], $f_n \in \mathcal{C}(K)$ for $n = 1, 2, 3, \dots$ ([[Space of Bounded Continuous Functions]]), and $\{f_n\}$ is [[Sequence of Function Pointwise Bounded|pointwise bounded]] and [[Equicontinuity|equicontinuous]] on $K$, then
> (a) $\{f_n\}$ is [[Sequence of Function Uniformly Bounded|uniformly bounded]] on $K$,
> (b) $\{f_n\}$ contains a [[Sequence of Function Uniform Convergence|uniformly convergent]] [[Subsequence]].

> [!abstract] Theorem 2 (Compactness in $\mathcal{C}(K)$)[^2]
> Let $K$ be a [[Compact Metric Space]] and $S \subseteq \mathcal{C}(K)$. Then $S$ is [[Compact Set|compact]] (with respect to the [[Supremum Norm]] metric) if and only if $S$ is uniformly closed, pointwise bounded, and equicontinuous.

Theorem 2 is the general form: it is the [[Heine-Borel Theorem]] for $\mathcal{C}(K)$, where "closed and bounded" must be strengthened by equicontinuity. If $S$ is not equicontinuous, then $S$ contains a sequence with no equicontinuous subsequence, hence no subsequence converging uniformly on $K$.[^2]

Theorem 1 is the function-space analogue of the [[Bolzano-Weierstrass Theorem]].

# Properties
- Proof uses the diagonal process of [[Pointwise Bounded Sequence Countable Set Subsequence Theorem]] on a countable [[Dense Subset]] of $K$ ([[Separable Metric Space|compact metric spaces are separable]]).
- Partial converse: a uniformly convergent sequence in $\mathcal{C}(K)$ is equicontinuous (see [[Equicontinuity]]).
- If $\{f_n\}$ is a uniformly bounded sequence of [[Riemann-Stieltjes Integral|Riemann-integrable]] functions on $[a, b]$ and $F_n(x) = \int_a^x f_n(t)\,dt$, then $\{F_n\}$ has a uniformly convergent subsequence on $[a, b]$ (the $F_n$ are uniformly [[Lipschitz Continuity|Lipschitz]], hence equicontinuous).[^3]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=167&annotation=RZILQ7RG)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=177&annotation=6RBPYHA8)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=177&annotation=84L6KVDU)
