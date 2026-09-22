---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Path Tracing (Recursive Estimator)[^1]
> Estimate $L(x,\omega)$ with one sample and recurse: draw $\omega_i \sim p$, set $y = \mathrm{rayTrace}(x,\omega_i)$, and return the one-sample estimate
> $$
> \begin{align}
> L_e(x,\omega) + \langle L(y,-\omega_i) \rangle\, \frac{f_s(x,\omega_i\to\omega)\,|\cos\theta_i|}{p(\omega_i)}
> \end{align}
> $$

Unbiased by induction: the same $f/p$ cancellation of a [[Monte Carlo Estimator]], applied once per recursion level. This is a random walk — a particle enters at the detector, scatters, scatters again, and is eventually absorbed; each step is one draw from $p$, so choosing $p$ is importance sampling. It converges because every bounce sends on a fraction $\rho < 1$ of what reached it, so the depth-$N$ contribution decays like $\rho^N$ — a finite total over an unbounded walk.

# Properties
- Nothing in the two recursive steps tells it when to stop; truncating at a fixed depth $D$ is biased in exactly the way a [[Monte Carlo Estimator]] is biased by [[Zero-Density Bias (Importance Sampling)|zero density]] — walks longer than $D$ get density zero wherever the integrand is not. [[Russian Roulette]] removes this bias by terminating with probability one instead.
- Walking backward from the sensor, as here, is one instance of [[Local Path Sampling]]; walking forward from a source instead is particle tracing.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
