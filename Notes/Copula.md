---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Copula[^1]
> Let $\mathbf{X} \sim F$ on $\mathbb{R}^d$ with continuous [[Marginal Distribution|marginal]] CDFs $F_1, \dots, F_d$. The random vector
> $$
> \begin{align}
> \mathbf{U} = \big(F_1(X_1), \dots, F_d(X_d)\big)
> \end{align}
> $$
> has a multivariate uniform distribution: each $U_j \sim \mathcal{U}(0,1)$ by the [[Probability Integral Transform]], though the $U_j$ are not independent in general. The distribution $C$ of $\mathbf{U}$ on $[0,1]^d$ is the copula of $F$.

The copula separates the dependence structure of $F$ from its marginals: the marginals are $d$ one-dimensional curves, while the copula carries all of the inherently $d$-dimensional information about how the components move together.[^2]

# Properties
- [[Sklar's Theorem]]: every $F$ is its marginals joined by some copula, uniquely when all $F_j$ are continuous.[^3]
- Invariant under strictly increasing transformations of the components: $Y_j = h_j(X_j)$ with increasing $h_j$ leaves the copula unchanged, so applying [[QQ Transformation|QQ transformations]] componentwise changes the marginals but keeps the dependence. This is the basis of [[Copula-Marginal Sampling]].[^4]
- The independence copula is $\mathcal{U}(0,1)^d$, i.e. $C(\mathbf{u}) = \prod_j u_j$ ([[Mutually Independent Random Variables]]).
- Classical copula families are catalogued in Nelsen (2006).[^4]

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=19&annotation=9YVPJ2QN); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=E5AXZHYA)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=7SENZZDX)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=PJL59BR4)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=GVJ27Y7V)
