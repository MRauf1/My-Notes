---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Convex [[Set]])[^1]
> Let $V$ be a vector space whose scalars contain $\mathbb{R}$ (most commonly $V = \mathbb{R}^n$ itself, but $V$ could equally be a complex or quaternionic space, viewed as a vector space over $\mathbb{R}$ by restricting scalars), and let $E \subseteq V$. $E$ is convex if, for real $t$,
> $$
> \begin{align}
> x, y \in E \land 0 < t < 1 \implies tx + (1 - t)y \in E
> \end{align}
> $$

Set is convex if whenever $E$ contains 2 points, it also contains the [[Line Segment]] connecting them. The interpolation parameter $t$ is always a *real* number between $0$ and $1$ — convexity only needs addition and REAL scalar multiplication, so it makes sense in any vector space that is, or contains, an $\mathbb{R}$-vector space: $\mathbb{R}^n$, $\mathbb{C}^n$, quaternionic space, infinite-dimensional function/[[Hilbert Space|Hilbert]]/[[Banach Space|Banach]] spaces, and so on (see [[Convex Set Path Connected Theorem]] for the general normed-space statement). What convexity cannot be defined over is a vector space whose scalar field admits no order at all, such as a finite field $\mathbb{F}_q$ — there, "$0 < t < 1$" is simply meaningless, since finite fields can never be ordered.

![[Pasted image 20251030164922.png]]

# Properties
## [[Path Connected Metric Space]]
- [[Convex Set Path Connected Theorem]]: every convex set is [[Path Connected Metric Space|path connected]], and hence [[Connected Metric Space|connected]].
- [[Strictly Convex Space]]

## Examples of Convex Sets
- Every [[Epsilon Neighborhood|ball]] (open or closed) in $\mathbb{R}^k$ is convex.[^2]
- Every [[k-Cell]] is convex.[^2]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=193)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=40)