---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Independent Random Variable Factorization Theorem[^1]
> Let $X_1, X_2$ have [[Random Variable Support|supports]] $\mathcal{S}_1, \mathcal{S}_2$ and joint pdf $f(x_1, x_2)$. Then $X_1$ and $X_2$ are [[Independent Random Variable|independent]] if and only if
> $$
> \begin{align}
> f(x_1, x_2) \equiv g(x_1) h(x_2)
> \end{align}
> $$
> where $g(x_1) > 0$ for $x_1 \in \mathcal{S}_1$ and zero elsewhere, and $h(x_2) > 0$ for $x_2 \in \mathcal{S}_2$ and zero elsewhere. The same holds for a joint pmf.

The point is that $g$ and $h$ need not be the [[Marginal Distribution|marginals]]; any nonnegative factorization suffices. Proof of sufficiency: integrating gives $f_1(x_1) = c_1 g(x_1)$ with $c_1 = \int h$, and $f_2(x_2) = c_2 h(x_2)$ with $c_2 = \int g$, and $c_1 c_2 = \iint f = 1$, so $f = g h = f_1 f_2$.

**The support must be a product space.** The conditions on $g$ and $h$ make $g(x_1) h(x_2)$ positive exactly on $\mathcal{S}_1 \times \mathcal{S}_2$, so the theorem only applies when the joint support is (up to a set of zero area) the product space $\mathcal{S}_1 \times \mathcal{S}_2$. A formula that looks factorable is not enough, because the support restriction is part of the function: $f(x_1, x_2) = 8 x_1 x_2$ on $0 < x_1 < x_2 < 1$ is really $8 x_1 x_2 \cdot \mathbb{1}\{x_1 < x_2\}$, and the indicator does not factor. Such $X_1, X_2$ are dependent.

# Properties
- Corollary: if the joint support is not a product set, e.g. it is bounded by a curve that is neither a horizontal nor a vertical line, then $X_1, X_2$ are dependent, whatever the formula for $f$ on the support.
- Extends to $n$ variables: $X_1, \dots, X_n$ are mutually independent iff $f(x_1, \dots, x_n) \equiv \prod_i g_i(x_i)$ on a product support.
- Not to be confused with the Fisher-Neyman factorization theorem for sufficient statistics, which factors a likelihood in the parameter rather than a density in the coordinates.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=135)
