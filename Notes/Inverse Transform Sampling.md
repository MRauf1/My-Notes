---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!abstract] Theorem 1 (Inverse Transform Sampling, Continuous)[^1]
> Given the [[Cumulative Distribution Function]] $F(a) := \mathbb{P}[X \leq a]$, draw $\xi \sim \mathcal{U}[0,1]$ and return $F^{-1}(\xi)$.
> Proof: $F$ is non-decreasing, so for any $a$,
> $$
> \begin{align}
> F^{-1}(\xi) \leq a \iff F\big(F^{-1}(\xi)\big) \leq F(a) \iff \xi \leq F(a)
> \end{align}
> $$
> hence $\mathbb{P}[X \leq a] = \mathbb{P}[\xi \leq F(a)] = F(a)$.

> [!abstract] Theorem 2 (Inverse Transform Sampling, Discrete)[^1]
> Given a cumulative mass function $F$, draw $\xi \sim \mathcal{U}[0,1]$ and return $\min\{x \in \mathbb{Z} : F(x) \geq \xi\}$, which can be computed by binary search in $O(\log N)$.

One uniform random number in, one sample out, with no wasted draws — this is the method to use whenever $F$ can be inverted. As one instance, the [[Exponential Distribution|exponential distribution]] $p(x;\lambda) = \lambda e^{-\lambda x}$ has CDF $F(x) = 1 - e^{-\lambda x}$, so inversion gives the closed form $x = -\log(1-\xi)/\lambda$ — the waiting time between events in a random walk (e.g. how far a photon travels before an interaction).

The discrete version is used to pick which sampling strategy to apply, which term of a series to estimate, which stratum to land in, or which kind of event happens next — any discrete choice weighted by probabilities.

# Properties
- Related to the general [[Cumulative Distribution Function Transformation Technique]] for transforming a random variable's density, of which inversion is the special case where the transformation is the CDF itself and the input variable is $\mathcal{U}[0,1]$.
- When $F^{-1}$ has no closed form (e.g. the normal distribution requires $\mathrm{erf}^{-1}$), a dedicated transform such as the [[Box-Muller Transform]] or [[Rejection Sampling]] is used instead.
- Used to sample a [[Free-Flight Distance Sampling|free-flight distance]] in a homogeneous medium, and the cosine-weighted case underlying [[BSDF Importance Sampling]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
