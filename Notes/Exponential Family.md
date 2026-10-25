---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Exponential Family)
> Parametric [[Set]] of [[Probability Distribution]] of the form
> $$
> \begin{align}
> f_X(x | \theta) &= h(x) \exp[\eta(\theta) \cdot T(x) - A(\theta)] \\
> &= h(x) g(\theta) \exp[\eta(\theta) \cdot T(x)] \\
> &= \exp[\eta(\theta) \cdot T(x) - A(\theta) + B(x)]
> \end{align}
> $$
> where $g(\theta) = e^{-A(\theta)}, h(x) = e^{B(x)}$.
> $\eta(\theta)$ is the natural parameter.

# Types
- [[Natural Exponential Family]]
- [[Regular Exponential Class]]: Hogg's form $\exp[p(\theta)K(x) + H(x) + q(\theta)]$ with support free of $\theta$, for which $\sum_i T(X_i)$ is a complete [[Sufficient Statistic]]

# Examples
- [[Normal Distribution]]
- [[Exponential Distribution]]
- [[Gamma Distribution]]
- [[Chi-Squared Distribution]]
- [[Beta Distribution]]
- [[Poisson Distribution]]
- [[Bernoulli Distribution]]
- [[Binomial Distribution]] with fixed $n$ (number of trials)
- [[Multinomial Distribution]] with fixed $n$ (number of trials)
- [[Negative Binomial Distribution]] with fixed $r$ (number of successes)
- [[Geometric Distribution]]
- [[Dirichlet Distribution]]
- [[Categorical Distribution]]
- [[Wishart Distribution]]
- [[Inverse Wishart Distribution]]

# Properties
- The negative log-likelihood of a regular exponential family equals a [[Bregman Divergence]] between the observation and the mean parameter, up to parameter-independent terms (Banerjee et al., 2005).[^1]
- Every exponential family has a natural [[Conjugate Prior]] $p(\theta) \propto g(\theta)^\eta e^{\eta(\theta) \cdot \nu}$, and apart from irregular cases, exponential families are the only families with natural conjugate priors (they alone have a fixed number of sufficient statistics for all $n$).[^2]
- For an iid sample, the likelihood depends on the data only through the [[Sufficient Statistic]] $\sum_i T(x_i)$.[^3]

[^1]: Supplementary notes provided by the creator.
[^2]: [Gelman et al., p. 37](zotero://open-pdf/library/items/HDF44SF4?page=47&annotation=8GLB5FJU)
[^3]: [Gelman et al., p. 36](zotero://open-pdf/library/items/HDF44SF4?page=46&annotation=FD5QVM9I)
