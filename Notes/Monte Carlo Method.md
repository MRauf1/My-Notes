---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Method[^1]
> A Monte Carlo method is any numerical algorithm that solves a mathematical problem, which may be entirely deterministic (an integral, a PDE, an optimization problem), by
> 1. reformulating the answer as the [[Expectation|expected value]] of a random variable under a chosen probability law $p$,
> 2. generating independent or correlated samples $X_1, \dots, X_N$ from $p$, and
> 3. approximating the answer by the empirical [[Sample Mean|sample mean]].
>
> For an integral, the reformulation is the probabilistic identity
> $$
> \begin{align}
> \Phi = \int_\Omega g(x)\,dx = \mathbb{E}_{X\sim p}\!\left[\frac{g(X)}{p(X)}\right] \approx \hat{\Phi}_N = \frac{1}{N}\sum_{i=1}^N \frac{g(X_i)}{p(X_i)}
> \end{align}
> $$
> which is the [[Monte Carlo Estimator]].

Developed in the 1940s at Los Alamos by Stanislaw Ulam, John von Neumann, and Nicholas Metropolis (who named it after the Monte Carlo Casino in Monaco) to solve analytically intractable neutron diffusion problems.

Unifying view: all Monte Carlo methods are stochastic estimators of expectations. They differ only in which distribution they draw from (uniform, importance-weighted, or the stationary law of a Markov chain) and how they keep the variance from blowing up (importance sampling, control variates, stratification, coordinate warps, gradients).

# Types
The hundreds of named algorithms are specialized answers to a few computational bottlenecks:
- **Direct random variate generation** — how to turn uniform $[0,1]$ samples into samples of a simple target density: [[Inverse Transform Sampling]], [[Rejection Sampling]], [[Box-Muller Transform]], [[Ziggurat Algorithm]].
- **Variance reduction** — how to shrink the constant $\sigma$ in the $\sigma/\sqrt{N}$ error when $N$ cannot grow: importance sampling ([[Optimal Importance Sampling Distribution]], [[Multiple Importance Sampling]]), [[Control Variates]], [[Antithetic Variates]], [[Stratified Sampling]], [[Latin Hypercube Sampling]], and [[Quasi-Monte Carlo]] (which also improves the rate).
- **[[Markov Chain Monte Carlo]]** — how to sample a density known only up to its normalizing constant: [[Metropolis-Hastings Algorithm]], [[Gibbs Sampling]], [[Metropolis-Adjusted Langevin Algorithm]], [[Hamiltonian Monte Carlo]].
- **[[Sequential Monte Carlo]] and particle methods** — how to sample distributions that evolve over time or have separated modes: particle filters, [[Annealed Importance Sampling]].
- **Transport, path-space, and differentiable Monte Carlo** — how to estimate infinite-dimensional integrals and their gradients: [[Path Tracing (Recursive Estimator)|path tracing]] of the [[Light Transport Equation]] (a Fredholm integral equation of the second kind), [[Walk on Spheres]] for elliptic PDEs, and [[Differentiable Monte Carlo]].

# Properties
- Consistent by the [[Strong Law of Large Numbers]]: $\hat{\Phi}_N \xrightarrow{\text{a.s.}} \Phi$ as $N \to \infty$.
- Error quantified by the [[Central Limit Theorem]]: $\hat{\Phi}_N - \Phi \approx \mathcal{N}(0, \sigma^2/N)$, so the error is $O(\sigma/\sqrt{N})$ — the [[Monte Carlo Convergence Rate]].
- Dimension-independent: the $O(N^{-1/2})$ rate has no $d$ in the exponent, whereas a tensor-product quadrature rule of order $r$ with $k$ points per axis uses $N = k^d$ points and converges as $O(N^{-r/d})$ — the [[Curse of Dimensionality]]. Monte Carlo therefore wins in high (even infinite) dimensions, while quadrature wins for smooth low-dimensional integrands.

[^1]: Monte Carlo Methods — Q&A Overview
