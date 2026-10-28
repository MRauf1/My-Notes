---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Sequential Inversion[^1]
> Factor the density of a [[Random Vector]] $\mathbf{X} \in \mathbb{R}^d$ by the [[Conditional Probability Multiplication Rule|chain rule]],
> $$
> \begin{align}
> f(\mathbf{x}) = \prod_{j=1}^d f_{j \mid 1:(j-1)}(x_j \mid \mathbf{x}_{1:(j-1)})
> \end{align}
> $$
> where the $j = 1$ factor is the [[Marginal Distribution|marginal]] of $X_1$. Sample $\mathbf{U} = (U_1, \dots, U_d) \sim \mathcal{U}(0,1)^d$ and set
> $$
> \begin{align}
> x_1 = F_{1 \mid \emptyset}^{-1}(u_1), \qquad x_j = F_{j \mid 1:(j-1)}^{-1}(u_j \mid \mathbf{x}_{1:(j-1)}), \quad j = 2, \dots, d
> \end{align}
> $$
> where $F_{1 \mid \emptyset}$ is the marginal CDF of $X_1$ and $F_{j \mid 1:(j-1)}$ is the [[Conditional Distribution|conditional]] CDF of $X_j$ given the previous components. Then $\mathbf{X} \sim f$.

This is the $d$-dimensional generalization of [[Inverse Transform Sampling]]: each component is drawn by one-dimensional inversion of its conditional CDF given the components already drawn. The components may be taken in any order whose conditional CDFs are tractable.[^1]

**Sequential conditional sampling.**[^3] The same factorization justifies drawing each $X_j \mid \mathbf{X}_{1:(j-1)} = \mathbf{x}_{1:(j-1)}$ by *any* one-dimensional method of [[Non-Uniform Random Variate Generation]], mixing inversion for some components, special transformations for others and [[Rejection Sampling|acceptance-rejection]] for the rest. Conditional acceptance-rejection methods are analysed with the variance reduction tools of [[Sequential Monte Carlo]].

# Properties
- Like one-dimensional inversion, it gives very good control over the simulation ($\mathbf{X}$ is a deterministic function of $\mathbf{U}$), and suits balanced sampling methods such as [[Stratified Sampling]].[^2]
- Practical only when the many conditional distributions that arise can be handled well: outside simple settings $F_{j \mid 1:(j-1)}$ may be hard to invert, and if inverting for $X_j$ needs an expensive setup for each $\mathbf{x}_{1:(j-1)} \in \mathbb{R}^{j-1}$ that cannot be reused, sampling is very slow.[^2]
- The [[Multivariate Normal Distribution]] is a notable case where all conditionals stay in the family ([[Multivariate Normal Distribution Conditional Distribution]]).
- The same sequential scheme along a directed graph is [[Ancestral Sampling]].
- The [[Copula-Marginal Sampling|copula-marginal method]] is another multivariate generalization of inversion.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=4&annotation=PPKC68E3); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=4&annotation=RE7SXVVZ)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=5&annotation=6SDQ2BXV)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=5&annotation=82YY3JXZ)
