---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 ([[Sequence of Function]] Uniformly Bounded)[^1]
> Let $\{f_n\}$ be a [[Sequence of Function]] defined on a [[Set]] $E$. $\{f_n\}$ is uniformly bounded on $E$ if there exists a number $M$ such that
> $$
> \begin{align}
> |f_n(x)| < M \quad (x \in E, \; n = 1, 2, 3, \dots)
> \end{align}
> $$

Uniform boundedness implies [[Sequence of Function Pointwise Bounded|pointwise boundedness]].

# Properties
- Even a uniformly bounded sequence of [[Continuous Function|continuous functions]] on a [[Compact Set]] need not have a [[Subsequence]] which converges pointwise on that set (unlike [[Bolzano-Weierstrass Theorem]] for numbers).[^1]
- Even if a uniformly bounded sequence converges pointwise on a compact set, it need not contain a uniformly convergent subsequence.[^2]
- A sequence of [[Bounded Function|bounded functions]] may converge pointwise without being uniformly bounded, but every [[Sequence of Function Uniform Convergence|uniformly convergent]] sequence of bounded functions is uniformly bounded.[^2][^3]
- [[Equicontinuity]] is the missing ingredient: see [[Arzelà-Ascoli Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=164&annotation=M9RGQGB2)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=165&annotation=AITLFHVE)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=174&annotation=T3HJZSH7)
