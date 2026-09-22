---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Estimator Efficiency[^1]
> Variance alone is not a fair comparison between estimators, since an estimator with cheaper samples can simply draw more of them. The honest currency is efficiency:
> $$
> \begin{align}
> \varepsilon = \frac{1}{\mathrm{Var}[\langle I \rangle] \cdot \mathrm{cost}(\langle I \rangle)}
> \end{align}
> $$

A technique earns its place only when it raises $\varepsilon$ — by cutting [[Monte Carlo Estimator Variance|variance]] at fixed cost, or by cutting cost faster than it raises variance. Estimators should therefore be compared at equal time rather than at equal sample count.

# Properties
- The correct lens for judging whether [[Stratified Sampling|stratification]], [[Control Variates]], or a change of $p$ is actually worthwhile.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
