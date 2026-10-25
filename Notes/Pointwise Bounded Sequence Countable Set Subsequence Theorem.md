---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Sequence of Function Pointwise Bounded|Pointwise Bounded]] Sequence on [[Countable Set]] Subsequence Theorem)[^1]
> If $\{f_n\}$ is a [[Sequence of Function Pointwise Bounded|pointwise bounded]] [[Sequence of Function|sequence]] of complex functions on a [[Countable Set]] $E$, then $\{f_n\}$ has a [[Subsequence]] $\{f_{n_k}\}$ such that $\{f_{n_k}(x)\}$ converges for every $x \in E$.

The subsequence [[Sequence of Function Pointwise Convergence|converges pointwise]] on $E$ (not necessarily uniformly). The proof is the Cantor diagonal process: enumerate $E = \{x_1, x_2, \dots\}$, use [[Bolzano-Weierstrass Theorem]] to extract nested subsequences converging at $x_1$, then $x_2$, etc., and take the diagonal.

The theorem uses no continuity; it is a pure selection process.[^2]

# Properties
- Key step in the proof of the [[Arzelà-Ascoli Theorem]] (applied to a countable [[Dense Subset]] of a compact space).
- Key step in [[Helly's Selection Theorem]] (applied to the rationals).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=165&annotation=PSLDSA72)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=165&annotation=Y63ACNRH)
