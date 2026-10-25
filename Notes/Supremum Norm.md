---
tags:
  - mathematics
  - linear_algebra
  - real_analysis
---

# Definition
> [!info] Definition 1 (Supremum Norm)[^1]
> The supremum norm on $C([0,1])$ is defined by
> $$
> \lVert f \rVert_\infty := \max_{0 \leq x \leq 1} |f(x)|
> $$

This is the functional analog of the [[Infinity Norm]] on $\mathbb{R}^n$/$\mathbb{C}^n$.

> [!info] Definition 2 (Supremum Norm on $\mathscr{C}(X)$)[^2]
> For a [[Metric Space]] $X$ and $f \in \mathscr{C}(X)$ ([[Space of Bounded Continuous Functions]]),
> $$
> \begin{align}
> \lVert f \rVert = \sup_{x \in X} |f(x)|
> \end{align}
> $$
> Since $f$ is bounded, $\lVert f \rVert < \infty$; $\lVert f \rVert = 0$ only if $f = 0$; and $\lVert f + g \rVert \leq \lVert f \rVert + \lVert g \rVert$.

When the domain is compact (e.g. $[0, 1]$), the supremum is attained and equals the maximum of Definition 1.

# Properties
- [[Normed Space]]
- Convergence in the supremum norm is [[Sequence of Function Uniform Convergence|uniform convergence]].
- $\mathscr{C}(X)$ is complete under this norm, hence a [[Banach Space]] ([[Space of Bounded Continuous Functions]]).
- [[L1 Norm]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=288)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=159&annotation=ZDDY4MLQ)
