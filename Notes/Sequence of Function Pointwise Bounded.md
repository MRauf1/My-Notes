---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 ([[Sequence of Function]] Pointwise Bounded)[^1]
> Let $\{f_n\}$ be a [[Sequence of Function]] defined on a [[Set]] $E$. $\{f_n\}$ is pointwise bounded on $E$ if the sequence $\{f_n(x)\}$ is [[Bounded Sequence|bounded]] for every $x \in E$, that is, if there exists a finite-valued function $\phi$ defined on $E$ such that
> $$
> \begin{align}
> |f_n(x)| < \phi(x) \quad (x \in E, \; n = 1, 2, 3, \dots)
> \end{align}
> $$

The bound $\phi(x)$ may depend on $x$; contrast [[Sequence of Function Uniformly Bounded]], where one bound works for all $x$.

# Properties
- If $\{f_n\}$ is pointwise bounded on $E$ and $E_1 \subseteq E$ is [[Countable Set|countable]], some [[Subsequence]] converges pointwise on $E_1$ ([[Pointwise Bounded Sequence Countable Set Subsequence Theorem]]).[^1]
- Pointwise bounded and [[Equicontinuity|equicontinuous]] on a [[Compact Metric Space|compact]] set implies [[Sequence of Function Uniformly Bounded|uniformly bounded]] ([[Arzelà-Ascoli Theorem]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=164&annotation=M9RGQGB2)
