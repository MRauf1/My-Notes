---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Neyman Factorization Theorem[^1]
> Let $X_1, \dots, X_n$ be a random sample from a distribution with pdf or pmf $f(x; \theta)$, $\theta \in \Omega$. The statistic $Y_1 = u_1(X_1, \dots, X_n)$ is a [[Sufficient Statistic]] for $\theta$ if and only if there are two nonnegative functions $k_1$ and $k_2$ such that
> $$
> \begin{align}
> f(x_1; \theta)f(x_2; \theta)\cdots f(x_n; \theta) = k_1[u_1(x_1, \dots, x_n); \theta]\,k_2(x_1, \dots, x_n)
> \end{align}
> $$
> where $k_2(x_1, \dots, x_n)$ does not depend on $\theta$.

> [!abstract] Joint Version[^2]
> The vector of statistics $\mathbf{Y} = (Y_1, \dots, Y_m)^T$ is jointly sufficient for $\boldsymbol{\theta} \in \Omega$ if and only if there are nonnegative $k_1, k_2$ with
> $$
> \begin{align}
> \prod_{i=1}^n f(x_i; \boldsymbol{\theta}) = k_1(\mathbf{y}; \boldsymbol{\theta})\,k_2(x_1, \dots, x_n) \quad \text{for all } x_i \in S
> \end{align}
> $$
> where $k_2$ does not depend on $\boldsymbol{\theta}$ and $S$ is the support of $X$.

The [[Likelihood Function|likelihood]] depends on the data only through $Y_1$, up to a factor that is free of $\theta$. So every likelihood-based inference about $\theta$ uses the sample only through $Y_1$. The theorem is easier to use than the definition of sufficiency because it does not require the distribution of $Y_1$.

# Properties
- The support must be handled with indicator functions. For example, a support depending on $\theta$ enters $k_1$ through the order statistics.
- It also holds for non-iid samples, with $\prod_i f(x_i; \theta)$ replaced by the joint pdf $f(x_1, \dots, x_n; \theta)$.
- Applied to the [[Regular Exponential Class]], it shows immediately that $\sum_i K(X_i)$ is sufficient.
- Not to be confused with the group-theoretic [[Factorization Theorem]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=438&annotation=5DGU3WPZ)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=463&annotation=XWGENHQM)
