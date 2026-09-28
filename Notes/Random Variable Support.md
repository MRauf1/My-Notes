---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Support of a Random Variable[^1][^2]
> For a [[Discrete Random Variable]] $X$ with space $\mathcal{D}$ and [[Probability Mass Function|pmf]] $p_X$, the support is the set of points with positive probability
> $$
> \begin{align}
> \mathcal{S}_X = \{x \in \mathcal{D} : p_X(x) > 0\}
> \end{align}
> $$
> For a [[Continuous Random Variable]] with [[Probability Density Function|pdf]] $f_X$, the support is
> $$
> \begin{align}
> \mathcal{S}_X = \{x : f_X(x) > 0\}
> \end{align}
> $$

This is the probabilistic counterpart of [[Function Support]], applied to the pmf or pdf.

# Properties
- $\mathcal{S}_X \subseteq \mathcal{D}$, possibly with equality.
- In the discrete case, $x \in \mathcal{S}_X$ if and only if the [[Cumulative Distribution Function|cdf]] $F_X$ jumps at $x$, with jump size $p_X(x)$; off the support $F_X$ is continuous.
- A pdf is determined only up to changes on sets of length zero, so the continuous-case support is defined only up to such sets; measure-theoretic treatments therefore define the support as the smallest closed set of probability $1$.
- Under a one-to-one transformation $Y = g(X)$, $\mathcal{S}_Y = \{g(x) : x \in \mathcal{S}_X\}$ (see [[Random Variable Transformation]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=62)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=66)
