---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Dirichlet Distribution[^1]
> Random variables $Y_1, \dots, Y_k$ have a Dirichlet distribution with parameters $\alpha_1, \dots, \alpha_{k+1} > 0$ if their joint pdf is
> $$
> \begin{align}
> g(y_1, \dots, y_k) = \frac{\Gamma(\alpha_1 + \dots + \alpha_{k+1})}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_{k+1})} y_1^{\alpha_1 - 1}\cdots y_k^{\alpha_k - 1}(1 - y_1 - \dots - y_k)^{\alpha_{k+1} - 1}
> \end{align}
> $$
> for $y_i > 0$ and $y_1 + \dots + y_k < 1$, and zero elsewhere.

**Construction.** If $X_1, \dots, X_{k+1}$ are independent with $X_i \sim \Gamma(\alpha_i, 1)$, then $Y_i = X_i / \sum_{j=1}^{k+1} X_j$ for $i = 1, \dots, k$ are Dirichlet, and $Y_{k+1} = \sum_j X_j \sim \Gamma(\sum_j \alpha_j, 1)$ is independent of $(Y_1, \dots, Y_k)$ (by the $n$-dimensional [[Random Vector Transformation]]). The normalized proportions forget the total.

Writing $y_{k+1} = 1 - \sum_{i \leq k} y_i$, the vector $(y_1, \dots, y_{k+1})$ lies on the probability simplex, so the Dirichlet is a distribution over probability vectors, i.e. over pmfs on $k + 1$ categories.

# Properties
- $k = 1$ gives the [[Beta Distribution]] $\text{Beta}(\alpha_1, \alpha_2)$; each marginal $Y_i$ is $\text{Beta}(\alpha_i, \alpha_0 - \alpha_i)$ with $\alpha_0 = \sum_j \alpha_j$.
- $E(Y_i) = \alpha_i / \alpha_0$; larger $\alpha_0$ concentrates the distribution around its mean, while all $\alpha_i = 1$ gives the uniform distribution on the simplex.
- It is the [[Conjugate Prior]] of the [[Multinomial Distribution]] probabilities, generalizing the beta-binomial pair.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=197)
