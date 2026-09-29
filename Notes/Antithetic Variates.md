---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Antithetic Variates[^1]
> Draw samples in negatively correlated pairs — e.g. $U$ and $1 - U$ for $U \sim \mathcal{U}[0,1]$, or more generally $X$ and a reflected $X'$ with the same marginal distribution — and average each pair:
> $$
> \begin{align}
> \langle I \rangle_{\mathrm{AV}} = \frac{1}{2}\big(F(X) + F(X')\big), \qquad \mathrm{Var}[\langle I \rangle_{\mathrm{AV}}] = \frac{\sigma^2}{2}\,(1 + \rho)
> \end{align}
> $$
> where $\sigma^2 = \mathrm{Var}[F(X)]$ and $\rho$ is the [[Correlation]] between $F(X)$ and $F(X')$.

Compared with two independent samples (variance $\sigma^2/2$), the pair's fluctuations partially cancel when $\rho < 0$.

# Properties
- Unbiased, since $X'$ has the same marginal as $X$.
- Reduces variance iff $\rho < 0$; guaranteed when $F$ is monotone in $U$ and the pair is $(U, 1-U)$, and harmful when $\rho > 0$ (e.g. $F$ symmetric about $1/2$).
- A variance-reduction technique of the [[Monte Carlo Method]], alongside [[Control Variates]] and [[Stratified Sampling]].

[^1]: Monte Carlo Methods — Q&A Overview
