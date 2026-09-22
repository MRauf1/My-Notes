---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Bias-Variance-MSE Decomposition of an Estimator[^1]
> For an estimator $\langle I \rangle_N$ of a fixed, deterministic quantity $I$,
> $$
> \begin{align}
> \underbrace{\mathbb{E}\big[(\langle I \rangle_N - I)^2\big]}_{\text{MSE}} = \underbrace{\big(\mathbb{E}[\langle I \rangle_N] - I\big)^2}_{\text{bias}^2} + \underbrace{\mathrm{Var}[\langle I \rangle_N]}_{\text{variance}}
> \end{align}
> $$

[[Variance|Variance]] is visible — it appears as noise across runs. [[Bias|Bias]] is not visible — a biased estimator can look exactly like a converged answer. Consequently, an estimator with ten times the variance and no bias is often a more useful research tool than one with a small, unknown bias, because variance can be measured (e.g. by re-running) while a hidden bias cannot.

# Properties
- Reduces to the model-fitting [[Bias-Variance Tradeoff]] when the fixed target $I$ is replaced by a randomly observed $y_0$ with irreducible noise, which contributes a further $\mathrm{Var}[\epsilon]$ term.
- Specializes to the [[Expected Squared-Error Loss of a Noisy Monte Carlo Estimator|expected squared-error loss of a noisy estimator]] when the quantity being scored is a loss evaluated at the random estimator itself rather than the estimator compared against $I$.
- Applies to any [[Monte Carlo Estimator]] of a fixed integral $I$.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
