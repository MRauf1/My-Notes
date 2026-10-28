---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Copula-Marginal Sampling[^1]
> To sample $\mathbf{X} \in \mathbb{R}^d$ with [[Copula]] $C$ and marginal CDFs $F_1, \dots, F_d$:
> $$
> \begin{align}
> \mathbf{U} \sim C, \qquad X_j = F_j^{-1}(U_j), \quad j = 1, \dots, d
> \end{align}
> $$
> with $F_j^{-1}$ the generalized inverse ([[Quantile Function]]).

> [!info] Copula-Marginal Sampling from a Donor Distribution[^2]
> Let $\mathbf{Y} \sim G$ be a continuous distribution on $\mathbb{R}^d$ that can be sampled, with marginal CDFs $G_1, \dots, G_d$, and let $F_1, \dots, F_d$ be given continuous marginals. Then
> $$
> \begin{align}
> X_j = F_j^{-1}\big(G_j(Y_j)\big), \quad j = 1, \dots, d
> \end{align}
> $$
> gives a random vector $\mathbf{X}$ with marginals $F_j$ and the same copula as $G$.

The second form applies a [[QQ Transformation]] to each component, combining the dependence structure of one family (e.g. the [[Multivariate Normal Distribution]]) with the marginals of another. It generalizes [[Inverse Transform Sampling]] and reduces to the QQ transformation when $d = 1$, but $d > 1$ adds enough complexity to count as a fourth generic method of multivariate [[Non-Uniform Random Variate Generation]], alongside [[Sequential Inversion|inversion]], [[Rejection Sampling|acceptance-rejection]] and [[Mixture Distribution|mixtures]].[^3]

# Properties
- Fully general by [[Sklar's Theorem]]: for every $F$ some copula $C$ makes the procedure deliver $\mathbf{X} \sim F$.[^4]
- It does not make sampling easier by itself: the marginals are $d$ one-dimensional curves, but the copula is inherently $d$-dimensional, so the method just pushes the difficulty into sampling $\mathbf{U} \sim C$.[^5]
- Mixing a copula from one family with margins from another may destroy the convenient properties of either family, such as closure under sums or minima, which is an aesthetic objection; but the property most wanted may be incompatible with every standard multivariate family anyway.[^6]

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=E5AXZHYA)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=GVJ27Y7V)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=3&annotation=BLY9P3UL); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=19&annotation=L8KL37FJ)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=PJL59BR4)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=7SENZZDX)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=21&annotation=34E6NTGE)
