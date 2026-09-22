---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Expected Squared-Error Loss of a Noisy Monte Carlo Estimator[^1]
> When a loss is evaluated on a noisy Monte Carlo simulation $\langle I \rangle$ rather than on the true (unknown) $I = \mathbb{E}[\langle I \rangle]$, the expected squared-error loss $\ell_2$ decomposes as
> $$
> \begin{align}
> \mathbb{E}[\ell_2(\langle I \rangle)] = \ell_2\big(\mathbb{E}[\langle I \rangle]\big) + \mathrm{Var}[\langle I \rangle]
> \end{align}
> $$

You may not be optimizing the loss you think you are: estimator noise is inside the objective, not merely blurring it. Minimizing $\mathbb{E}[\ell_2(\langle I \rangle)]$ is not the same as minimizing $\ell_2(I)$, because the [[Variance|variance]] of the estimator contributes an unavoidable additive term. This is a special case of the [[Bias-Variance-MSE Decomposition of an Estimator|bias-variance-MSE decomposition]], where the quantity being scored by $\ell_2$ is itself a random estimator rather than a comparison against a fixed ground truth.

# Properties
- Whether this variance-inflation of the objective is undesirable depends on what is being optimized; it is not always a problem.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
