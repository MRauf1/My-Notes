---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Convergence Rate[^1]
> The root-mean-square error of a [[Monte Carlo Estimator]] shrinks as $O(1/\sqrt{N})$, with a constant given by the standard deviation $\sigma$ of the integrand $f/p$, regardless of the dimension $d$ of the domain of integration.

Bad: halving the error costs $4\times$ the samples — quadrature on a smooth 1D integrand converges much faster than this.

Good: the rate does not depend on $d$. Trapezoidal quadrature in $d$ dimensions converges only as $O(N^{-2/d})$, degrading with dimension, while Monte Carlo does not care about $d$. The crossover between the two rates is around $d = 4$; Monte Carlo integrals routinely run to dozens of dimensions or more, over integrands with no smoothness to exploit, which is why Monte Carlo dominates in that regime.

Since the rate $O(1/\sqrt{N})$ is fixed regardless of the technique used, the constant $\sigma$ — reduced via [[Optimal Importance Sampling Distribution|importance sampling]], [[Stratified Sampling|stratification]], or [[Control Variates]] — is the entire game.

**Owen's account.**[^2] For [[Simple Monte Carlo]], $E((\hat{\mu}_n - \mu)^2) = \sigma^2/n$ gives the exact rate of exchange between variance and sample size, $\mathrm{RMSE} = \sigma/\sqrt{n} = O(n^{-1/2})$.
- **Cost of precision:** one more decimal digit (RMSE $\div 10$) needs $100\times$ the computation; three more digits need $10^6\times$. Simple Monte Carlo is poorly suited to high-precision answers.
- **Variance–time exchange:**[^3] halving $\sigma^2$ (same $\mu$) gains as much as doubling $n$, which is the same gain as making $f$ twice as fast to evaluate. In reverse, since raising $n$ buys little accuracy, slower code that offers another benefit (e.g. faster programming) may be worth it ([[Monte Carlo Estimator Efficiency]]).
- **Versus quadrature:**[^4] in $d = 1$, [[Simpson's Rule]] has error $O(n^{-4})$ for integrands with a continuous fourth derivative, so $n$ Simpson points match about $An^8$ Monte Carlo points.
- **Strengths — neither dimension nor smoothness appears in $\sigma/\sqrt{n}$:**[^5] $d$ may be $2$ or $1000$ with the same RMSE, while product Simpson degrades to $O(n^{-4/d})$; and quadrature rates require bounded derivatives, whereas Monte Carlo only needs $\sigma^2 < \infty$. Monte Carlo is most competitive in **high-dimensional, non-smooth problems without closed forms**.
- The rate is lost when $\sigma^2 = \infty$ ([[Infinite Moments in Monte Carlo]]).

# Properties
- Contrasts with quadrature methods (e.g. the trapezoidal rule), whose $O(N^{-2/d})$ rate depends on dimension.
- Follows from the [[Central Limit Theorem]]; improved to nearly $O(N^{-1})$ for smooth integrands by [[Quasi-Monte Carlo]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=5XNJZUY2); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=BY5SIPV3)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=EDH7LDCP)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=HJT5NJQU)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=IA2TVW8I); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=LEXAWK3Q); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=18&annotation=X5WTL5AE)
