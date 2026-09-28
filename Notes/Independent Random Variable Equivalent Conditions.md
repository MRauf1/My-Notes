---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Theorem 1 (CDF Criterion)[^1]
> Let $(X_1, X_2)$ have [[Joint Cumulative Distribution Function|joint cdf]] $F(x_1, x_2)$ and marginal cdfs $F_1, F_2$. Then $X_1, X_2$ are [[Independent Random Variable|independent]] if and only if
> $$
> \begin{align}
> F(x_1, x_2) = F_1(x_1) F_2(x_2) \quad \text{for all } (x_1, x_2) \in \mathbb{R}^2
> \end{align}
> $$

> [!abstract] Theorem 2 (Rectangle Criterion)[^1]
> $X_1, X_2$ are independent if and only if
> $$
> \begin{align}
> P(a < X_1 \leq b, c < X_2 \leq d) = P(a < X_1 \leq b)\,P(c < X_2 \leq d)
> \end{align}
> $$
> for every $a < b$ and $c < d$.

> [!abstract] Theorem 3 (MGF Criterion)[^2]
> Suppose the joint mgf $M(t_1, t_2)$ of $X_1, X_2$ exists. Then $X_1, X_2$ are independent if and only if
> $$
> \begin{align}
> M(t_1, t_2) \equiv M(t_1, 0)\,M(0, t_2)
> \end{align}
> $$
> i.e. the joint mgf is the product of the marginal mgfs ([[Moment Generating Function of Random Vector]]).

Theorems 1 and 2 are equivalent because rectangle probabilities are corner differences of the cdf, and a product cdf gives product differences. Unlike the pdf or pmf definition, they apply to every random vector, with or without a density. Theorem 3 uses uniqueness of the mgf: the product $M_1(t_1) M_2(t_2)$ is the mgf of an independent pair with the same marginals.

# Properties
- General (measure-theoretic) definition: $X_1, X_2$ are independent iff $P(X_1 \in A, X_2 \in B) = P(X_1 \in A) P(X_2 \in B)$ for all (Borel) sets $A, B$, i.e. every event determined by $X_1$ is an [[Independent Events|independent event]] from every event determined by $X_2$; rectangles suffice because they generate all such sets.
- Consequently $u(X_1)$ and $v(X_2)$ are independent for any (measurable) functions $u, v$.
- The [[Characteristic Function (Probability)|characteristic function]] version, $\varphi(t_1, t_2) = \varphi_1(t_1) \varphi_2(t_2)$, works even when no mgf exists.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=137)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=138)
