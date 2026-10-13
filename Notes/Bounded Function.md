---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Bounded [[Function]] into $\mathbb{R}^k$)[^1]
> A mapping $f: E \rightarrow \mathbb{R}^k$ is bounded if there is a real number $M$ such that
> $$
> \begin{align}
> |f(x)| \leq M \quad \text{for all } x \in E
> \end{align}
> $$

> [!info] Definition 2 (Bounded [[Function]] into [[Metric Space]])[^2]
> A mapping $f: E \rightarrow Y$ into a [[Metric Space]] $(Y, d_Y)$ is bounded if its [[Image]] $f(E)$ is a [[Bounded Set]], i.e., there exist $q \in Y$ and $M \in \mathbb{R}$ such that $d_Y(f(x), q) \leq M$ for all $x \in E$.

Definition 1 is the special case of Definition 2 with $Y = \mathbb{R}^k$ and $q = \mathbf{0}$.

# Properties
- Every continuous function on a [[Compact Metric Space]] is bounded ([[Continuous Function Compact Metric Space Theorem]], [[Continuous Function Bounded Theorem]]).
- Compactness cannot be dropped: [[Noncompact Subset of Real Line Continuous Function Theorem]].
- The [[Supremum Norm]] $\|f\|_\infty = \sup_{x \in E} |f(x)|$ is finite exactly for bounded functions.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=98)
[^2]: [Bounded function - Wikipedia](https://en.wikipedia.org/wiki/Bounded_function)
