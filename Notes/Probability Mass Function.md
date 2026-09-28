---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Probability Function|Probability]] Mass Function)[^1][^3]
> For a [[Discrete Random Variable|discrete RV]] $X$ with space $\mathcal{D}$, the pmf of $X$ is
> $$
> \begin{align}
> p_X(x) = P[X = x], \quad x \in \mathcal{D}
> \end{align}
> $$
> also denoted $f(x)$ or $f_X$.

# Properties
- [[Probability Mass Function Definitional Properties]]: $0 \leq p_X(x) \leq 1$ for $x \in \mathcal{D}$ and $\sum_{x \in \mathcal{D}} p_X(x) = 1$.
- Determines the induced distribution $P_X(D) = \sum_{x \in D} p_X(x)$ for $D \subseteq \mathcal{D}$.
- Its positive points form the [[Random Variable Support|support]] $\mathcal{S}$; for $x \in \mathcal{S}$, $p_X(x) = F_X(x) - F_X(x^-)$ is the size of the jump of the [[Cumulative Distribution Function|cdf]] at $x$, and for $x \notin \mathcal{S}$, $F_X$ is continuous at $x$.
- A pmf over $K$ classes is a $K$-dimensional vector with elements in $[0,1]$ that sum to $1$, i.e., a point on the $(K-1)$-[[Simplex]] $\Delta^{K-1}$.[^2]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=52)
[^2]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=62)
