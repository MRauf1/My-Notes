---
tags:
  - mathematics
  - real_analysis
---

# Definition

Let $E$ be a [[Subset]] of [[Metric Space]] $(S, d)$.[^1]
- $E$ is [[Closed Set]] if and only if $E = E^-$
- An element is in $E^-$ if and only if it is the [[Limit of Sequence]] of some [[Sequence]] of [[Point]] in $E$

> [!abstract] Theorem (Characterizations of Closure)[^3]
> If $X$ is a [[Metric Space]], $E \subseteq X$, and $x \in X$, the following are equivalent:
> a. $x \in E^-$.
> b. $B(r, x) \cap E \neq \emptyset$ for all $r > 0$.
> c. There is a [[Sequence]] $\{x_n\}$ in $E$ that converges to $x$.

Consequently, with $\rho(x, E) = \inf\{\rho(x, y) : y \in E\}$, one has $\rho(x, E) = 0$ if and only if $x \in E^-$.[^4]

> [!abstract] Theorem (Supremum Lies in the Closure)[^2]
> Let $E$ be a nonempty [[Subset]] of $\mathbb{R}$ that is [[Set Upper Bound|bounded above]], and let $y = \sup E$. Then $y \in E^-$. Hence $y \in E$ if $E$ is [[Closed Set|closed]].

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=100)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=44)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=27&annotation=725ZCV53)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=28&annotation=PAIB9MKZ)
