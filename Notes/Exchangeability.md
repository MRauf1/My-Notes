---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Exchangeability[^1]
> Random variables $y_1, \dots, y_n$ are exchangeable if their joint density is invariant to permutations of the indexes: for every [[Permutation]] $\pi$ of $\{1, \dots, n\}$,
> $$
> \begin{align}
> p(y_1, \dots, y_n) = p(y_{\pi(1)}, \dots, y_{\pi(n)})
> \end{align}
> $$

Exchangeability says the labels carry no information about the outcomes. A nonexchangeable model is appropriate if information relevant to the outcome is conveyed by the unit indexes rather than by [[Covariate|explanatory variables]].[^1]

# Properties
- The usual (often tacit) starting point of a [[Statistical Inference|statistical analysis]].[^1]
- Exchangeable data are commonly modeled as [[Independent and Identically Distributed|iid]] given an unknown parameter vector $\theta$ with [[Prior Distribution]] $p(\theta)$:[^2]
$$
\begin{align}
p(y_1, \dots, y_n) = \int \left[\prod_{i=1}^n p(y_i \mid \theta)\right] p(\theta)\, d\theta
\end{align}
$$
- General case: iid implies exchangeable, but not conversely; conditionally iid mixtures as above are exchangeable but the $y_i$ are marginally dependent. De Finetti's theorem gives the converse for infinite exchangeable sequences: every such sequence is a mixture of iid sequences, which justifies the parameter-plus-prior structure of [[Bayesian Inference]].
- With covariates $x$, exchangeability is assumed for the $y_i$ conditional on $x_i$ (or for the pairs $(x_i, y_i)$).
- In a [[Hierarchical Model]], exchangeability can be stated separately at each level of units.[^3]

[^1]: [Gelman et al., p. 5](zotero://open-pdf/library/items/HDF44SF4?page=15&annotation=9JQKUV7N)
[^2]: [Gelman et al., p. 5](zotero://open-pdf/library/items/HDF44SF4?page=15&annotation=A2JKB3D2)
[^3]: [Gelman et al., p. 5](zotero://open-pdf/library/items/HDF44SF4?page=15&annotation=HJL44P8P)
