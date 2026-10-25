---
tags:
  - statistics
  - bayesian_statistics
---

# Definition

> [!info] Definition 1 (Conjugate Prior)
> If $\mathcal{F}$ is the family of [[Probability Distribution]] of data then a family $\mathcal{P}$ of distributions of $\theta$ are conjugate for $\mathcal{F}$ if using a prior from $\mathcal{P}$ always produces a posterior from $\mathcal{P}$.[^1] 
> As a result, the subsequent update only impacts the parameters of the posterior distribution.
> Conjugate priors are not unique.

> [!info] Definition 2 (Conjugacy, Gelman)[^2]
> If $\mathcal{F}$ is a class of sampling distributions $p(y \mid \theta)$ and $\mathcal{P}$ a class of priors for $\theta$, then $\mathcal{P}$ is conjugate for $\mathcal{F}$ if
> $$
> \begin{align}
> p(\theta \mid y) \in \mathcal{P} \quad \text{for all } p(\cdot \mid \theta) \in \mathcal{F} \text{ and } p(\cdot) \in \mathcal{P}
> \end{align}
> $$
> This is formally vague: the class of all distributions is always conjugate. The useful notion is the **natural conjugate prior family**, obtained by taking $\mathcal{P}$ to be the set of all densities with the same functional form (in $\theta$) as the likelihood.[^3]

> [!abstract] Exponential Family Conjugacy[^4][^5]
> If $p(y_i \mid \theta) = f(y_i)\, g(\theta)\, e^{\phi(\theta)^T u(y_i)}$ is an [[Exponential Family]], the iid likelihood is $p(y \mid \theta) \propto g(\theta)^n e^{\phi(\theta)^T t(y)}$ with [[Sufficient Statistic]] $t(y) = \sum_{i=1}^n u(y_i)$. The prior
> $$
> \begin{align}
> p(\theta) \propto g(\theta)^{\eta}\, e^{\phi(\theta)^T \nu}
> \end{align}
> $$
> is natural conjugate, with posterior $p(\theta \mid y) \propto g(\theta)^{\eta + n}\, e^{\phi(\theta)^T (\nu + t(y))}$.
> Conversely, apart from certain irregular cases, exponential families are the only classes with natural conjugate priors, since they are the only distributions with a fixed number of sufficient statistics for all $n$.

**Conjugate vs natural conjugate.**[^8]
- A *conjugate* prior is any prior family closed under updating with a given likelihood; it is a broad category, and its hyperparameters need not have an intuitive meaning.
- A *natural conjugate* prior is the subset constructed from the algebraic form of the likelihood (mainly for exponential families), whose hyperparameters act as pseudo-sufficient statistics and an effective prior sample size.
- "Same functional form as the likelihood" means the prior **kernel in $\theta$** mirrors the likelihood viewed as a function of $\theta$. It does **not** mean the prior is the same distribution as the likelihood: the likelihood $p(x \mid \theta)$ is a distribution over data, the prior a distribution over parameters, indexed by hyperparameters. E.g. Beta prior with Binomial likelihood share no family name; in the Normal–Normal case both are Gaussian, but in different variables ($x$ vs $\mu$).
- In canonical form $p(x \mid \eta) = h(x)\exp(\eta^T T(x) - A(\eta))$, the natural conjugate prior is
$$
\begin{align}
p(\eta \mid \chi, \nu) = f(\chi, \nu)\exp\left(\eta^T\chi - \nu A(\eta)\right)
\end{align}
$$
  with $\chi$ mirroring the sufficient statistic $T(x)$ and $\nu$ mirroring the sample size multiplying the log-partition $A(\eta)$. Multiplying adds exponents: $p(\eta \mid x_{1:n}) \propto \exp\left(\eta^T\left(\chi + \sum_i T(x_i)\right) - (\nu + n)A(\eta)\right)$.

In Gelman's parameterization (Exponential Family Conjugacy box, where $\eta$ is a prior sample size rather than the natural parameter), the update $\eta \to \eta + n$, $\nu \to \nu + t(y)$ makes the "prior as additional data" reading literal: $\eta$ is a prior sample size and $\nu$ a prior total of the sufficient statistic.

# Properties
- **Interpretable as additional data** (pseudo-observations), besides being computationally convenient ([[Posterior Compromise Between Prior and Data]]).[^3]
- Justification mirrors that of standard likelihoods: results are easy to understand and often analytic, they are often good approximations, and they simplify computation. They also serve as building blocks for complex, high-dimensional models where full conjugacy is impossible.[^6]
- If available information contradicts the conjugate family, a more realistic nonconjugate prior should be used; [[Mixture Distribution|mixtures]] of conjugate families can help when a single conjugate prior is unreasonable.[^6][^7]
- Nonconjugate priors pose no new conceptual problems, only less transparent interpretation and harder computation.[^6]
- Conjugacy makes the [[Prior Predictive Distribution]] available in closed form via $p(y) = p(y \mid \theta)\,p(\theta)/p(\theta \mid y)$.
- Its parameters are [[Hyperparameter|hyperparameters]]; choosing a prior family for convenience is part of [[Prior Distribution Selection]].

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=55)
[^2]: [Gelman et al., p. 35](zotero://open-pdf/library/items/HDF44SF4?page=45&annotation=YEVQ2RSV)
[^3]: [Gelman et al., p. 36](zotero://open-pdf/library/items/HDF44SF4?page=46&annotation=5PQ5U4CD)
[^4]: [Gelman et al., p. 36](zotero://open-pdf/library/items/HDF44SF4?page=46&annotation=FD5QVM9I); [Gelman et al., p. 36](zotero://open-pdf/library/items/HDF44SF4?page=46&annotation=32SW5V9I)
[^5]: [Gelman et al., p. 37](zotero://open-pdf/library/items/HDF44SF4?page=47&annotation=8GLB5FJU)
[^6]: [Gelman et al., p. 36](zotero://open-pdf/library/items/HDF44SF4?page=46&annotation=AYQDM2TP)
[^7]: [Gelman et al., p. 35](zotero://open-pdf/library/items/HDF44SF4?page=45&annotation=LGAESXX3)
[^8]: Supplementary notes provided by the creator.
