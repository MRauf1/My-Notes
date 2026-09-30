---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Complete Family[^1]
> Let the random variable $Z$, of the continuous or discrete type, have a pdf or pmf that is one member of the family $\{h(z; \theta) : \theta \in \Omega\}$. The family is complete if
> $$
> \begin{align}
> E_\theta[u(Z)] = 0 \ \text{ for every } \theta \in \Omega \implies u(z) = 0
> \end{align}
> $$
> except on a set of points that has probability zero for each $h(z; \theta)$, $\theta \in \Omega$.

> [!info] Vector Version[^2]
> Let $\{f(v_1, \dots, v_k; \boldsymbol{\theta}) : \boldsymbol{\theta} \in \Omega\}$ be a family of pdfs of $V_1, \dots, V_k$ depending on a $p$-dimensional parameter $\boldsymbol{\theta}$. Let $u(v_1, \dots, v_k)$ be a function that does not involve the parameters. The family is complete if $E[u(V_1, \dots, V_k)] = 0$ for all $\boldsymbol{\theta} \in \Omega$ implies $u = 0$ at all points, except on a set that has probability zero for every member of the family.

Remark 7.4.1:[^3] the existence of $E[u(Z)]$ means that the integral or sum converges absolutely. This absolute convergence is tacitly assumed in the definition, and it is needed to prove that certain families are complete.

**Terminology.**[^4] If $Y_1$ is a [[Sufficient Statistic]] for $\theta$ and $\{f_{Y_1}(y_1; \theta) : \theta \in \Omega\}$ is complete, $Y_1$ is called a complete sufficient statistic. The vector analogue is joint complete sufficient statistics.

The only unbiased estimator of $0$ based on $Z$ is the trivial one. The family is rich enough, as $\theta$ ranges over $\Omega$, that the expectations $E_\theta[u(Z)]$ determine $u$. The consequence is uniqueness: if $E[\varphi_1(Z)] = E[\varphi_2(Z)] = \theta$ for all $\theta$, then $E[\varphi_1(Z) - \varphi_2(Z)] = 0$ for all $\theta$, so $\varphi_1 = \varphi_2$ almost surely. There is at most one unbiased estimator of $\theta$ that is a function of a complete statistic.

For continuous families, completeness is often a uniqueness statement for an integral transform. For the [[Regular Exponential Class]], $E_\theta[u(Y_1)] = \int u(y_1)R(y_1)e^{p(\theta)y_1 + nq(\theta)}dy_1 = 0$ on an interval of $p(\theta)$ says that a Laplace transform vanishes, which forces $u(y_1)R(y_1) = 0$.

# Properties
- Gives uniqueness in the [[Lehmann-Scheffé Theorem]] and independence in [[Basu's Theorem]].
- The regular exponential class has complete sufficient statistics: $\sum K(X_i)$ in the one-parameter case, and $(\sum K_1(X_i), \dots, \sum K_m(X_i))$ when $n > m$.
- A complete sufficient statistic is minimal sufficient, provided a [[Minimal Sufficient Statistic]] exists (Bahadur). The converse is false.
- Completeness is a property of the family of distributions, not of one distribution. Shrinking $\Omega$ can destroy it.
- A nonconstant [[Ancillary Statistic]] that is a function of $Y_1$ would give $E_\theta[u(Y_1) - c] = 0$ for all $\theta$. So a complete statistic has no nontrivial ancillary functions of itself.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=447&annotation=8H55ZX46)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=464&annotation=M7PAR9D3)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=447&annotation=963VSQ9R)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=449&annotation=E5GKTAZA)
