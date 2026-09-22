---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Bias and Consistency of an Estimator (Four Quadrants)[^1]
> [[Bias|Bias]] and consistency are independent properties of an estimator, giving four combinations:
> - Unbiased and consistent: the nice case — the plain [[Monte Carlo Estimator]], [[Stratified Sampling|stratification]], [[Control Variates]].
> - Unbiased and not consistent: rare; needs pathology.
> - Biased and consistent: kernel estimates with shrinking bandwidth, a solver with shrinking step size, [[Stochastic Gradient Descent]] — fine, as long as the bias is acknowledged.
> - Biased and not consistent: clamping outliers, denoising the output, naive automatic differentiation of a discontinuous integrand.

# Properties
- A biased-but-consistent estimator is often an acceptable engineering tradeoff, since its bias vanishes as $N \to \infty$; a biased-and-inconsistent estimator never self-corrects with more samples.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
