---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Totally Bounded Metric Space)[^1]
> A [[Metric Space]] $(X, d)$ is totally bounded if, for every $\epsilon > 0$, $X$ can be covered by finitely many [[Epsilon Neighborhood|balls]] of radius $\epsilon$.

> [!info] Definition 2 (Totally Bounded Subset)[^1]
> A subset $E$ of a [[Metric Space]] $X$ is totally bounded if, for every $\epsilon > 0$, $E$ can be covered by finitely many balls of radius $\epsilon$, i.e. $E \subseteq \bigcup_{j=1}^n B(\epsilon, z_j)$. (A family $\{V_\alpha\}_{\alpha \in A}$ with $E \subseteq \bigcup_\alpha V_\alpha$ is called a cover of $E$; see [[Open Cover]].)

My interpretation: this is a stronger requirement than merely being [[Bounded Set|bounded]] — a bounded space can still contain infinitely many points spread out in a way that no fixed finite number of small balls can cover (e.g. an infinite-dimensional space), whereas total boundedness demands the space can be covered by finitely many arbitrarily small balls.

# Properties
- Totally bounded $\implies$ [[Bounded Set|bounded]] (but not conversely, in general metric spaces).
- If $x \in B(\epsilon, z_1)$ and $y \in B(\epsilon, z_2)$, then $\rho(x, y) < 2\epsilon + \max_{j,k} \rho(z_j, z_k)$, which proves totally bounded $\implies$ bounded.[^1]
- If $E$ is totally bounded, so is its [[Closure Set|closure]] $E^-$: $E \subseteq \bigcup_1^n B(\epsilon, z_j)$ implies $E^- \subseteq \bigcup_1^n B(2\epsilon, z_j)$.[^1]
- [[Compact Metric Space|Compactness Equivalence Theorem]]: a metric space is compact if and only if it is both [[Complete Metric Space|complete]] and totally bounded.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=28&annotation=7J4RNEJG)
