---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Equicontinuous Family)[^1]
> A family $\mathscr{F}$ of complex [[Function|functions]] $f$ defined on a [[Set]] $E$ in a [[Metric Space]] $(X, d)$ is equicontinuous on $E$ if for every $\epsilon > 0$ there exists a $\delta > 0$ such that
> $$
> \begin{align}
> |f(x) - f(y)| < \epsilon
> \end{align}
> $$
> whenever $d(x, y) < \delta$, $x \in E$, $y \in E$, and $f \in \mathscr{F}$.

A single $\delta$ works for all points *and* all members of the family; equicontinuity is to [[Uniformly Continuous Function|uniform continuity]] what uniform convergence is to pointwise convergence.

# Properties
- Every member of an equicontinuous family is [[Uniformly Continuous Function|uniformly continuous]].[^1]
- If $K$ is a [[Compact Metric Space]], $f_n \in \mathcal{C}(K)$ ([[Space of Bounded Continuous Functions]]), and $\{f_n\}$ [[Sequence of Function Uniform Convergence|converges uniformly]] on $K$, then $\{f_n\}$ is equicontinuous on $K$.[^2]
- Conversely, pointwise bounded + equicontinuous on compact $K$ gives a uniformly convergent subsequence ([[Arzelà-Ascoli Theorem]]).
- If $\{f_n\}$ is an equicontinuous sequence on a [[Compact Set]] $K$ and converges pointwise on $K$, then $\{f_n\}$ converges uniformly on $K$.[^3]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=165&annotation=Y63ACNRH)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=166&annotation=224VGWCX)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=177&annotation=R99N94IB)
