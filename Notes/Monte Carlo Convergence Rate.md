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

# Properties
- Contrasts with quadrature methods (e.g. the trapezoidal rule), whose $O(N^{-2/d})$ rate depends on dimension.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
