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

The same definitions apply to a [[Random Vector]] $(X_1, X_2)$ with space $\mathcal{D}$: its support $\mathcal{S}$ is the set of points $(x_1, x_2)$ with $p(x_1, x_2) > 0$ (discrete) or $f(x_1, x_2) > 0$ (continuous), and $\mathcal{S} \subseteq \mathcal{D}$.[^3] For an $n$-dimensional vector, Hogg et al. describe the continuous support as the points of $\mathcal{D}$ "that can be embedded in an open set of positive probability".[^4] Read literally this is too weak (every point lies in $\mathbb{R}^n$, an open set of probability $1$); the intended meaning is that every open neighborhood of the point has positive probability, which is exactly the closed-support definition below.

# Properties
- $\mathcal{S}_X \subseteq \mathcal{D}$, possibly with equality.
- In the discrete case, $x \in \mathcal{S}_X$ if and only if the [[Cumulative Distribution Function|cdf]] $F_X$ jumps at $x$, with jump size $p_X(x)$; off the support $F_X$ is continuous.
- A pdf is determined only up to changes on sets of length zero, so the continuous-case support is defined only up to such sets; measure-theoretic treatments therefore define the support as the smallest closed set of probability $1$.
- Under a one-to-one transformation $Y = g(X)$, $\mathcal{S}_Y = \{g(x) : x \in \mathcal{S}_X\}$ (see [[Random Variable Transformation]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=62)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=66)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=103)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=151)
