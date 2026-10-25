---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Sequence of Function Uniform Convergence]] of [[Continuous Function]] Theorem)[^1]
> Let $(f_n)$ be [[Sequence of Function]] on a [[Set]] $S \subseteq \mathbb{R}$, suppose $f_n \rightarrow f$ [[Sequence of Function Uniform Convergence|uniformly]] on $S$, and suppose $S = Domain(f)$. If each $f_n$ is [[Continuous Function]] on $S$, then $f$ is [[Continuous Function]] on $S$.

This does not necessarily hold when the sequence converges pointwise.

> [!abstract] Theorem 2 ([[Infinite Series]] Version)[^2]
> Let $\sum_{k=0}^{\infty} g_k$ be [[Infinite Series of Functions]] on a [[Set]] $S \subseteq \mathbb{R}$. Suppose each $g_k$ is [[Continuous Function]] on $S$ and the [[Infinite Series]] [[Sequence of Function Uniform Convergence|converges uniformly]] on $S$. Then the [[Infinite Series]] $\sum_{k=0}^{\infty} g_k$ represents a [[Continuous Function]] on $S$.

> [!abstract] Theorem 3 ([[Metric Space]] Version)[^3]
> If $\{f_n\}$ is a [[Sequence of Function|sequence]] of [[Continuous Function|continuous functions]] on a set $E$ in a [[Metric Space]], and if $f_n \rightarrow f$ uniformly on $E$, then $f$ is continuous on $E$.

The converse is not true: a sequence of continuous functions may converge to a continuous function although the convergence is not uniform.[^4]

# Properties
- Corollary of the [[Uniform Convergence Interchange of Limits Theorem]].[^4]
- Partial converse: [[Dini's Theorem]].
- Equivalently, $\mathscr{C}(X)$ is uniformly closed in the bounded functions; see [[Space of Bounded Continuous Functions]].

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=206)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=214)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=159&annotation=VCDR48BF)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=159&annotation=RXICR9DG)
