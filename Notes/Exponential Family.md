---
tags: statistics, categorical_variable_prediction
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