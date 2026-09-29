---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Annealed Importance Sampling[^1]
> Bridge an easy distribution $\pi_0$ to the (unnormalized) target $\tilde{\pi}_T$ through the geometric path
> $$
> \begin{align}
> \tilde{\pi}_t(x) = \pi_0(x)^{1-\beta_t}\,\tilde{\pi}_T(x)^{\beta_t}, \qquad 0 = \beta_0 < \beta_1 < \dots < \beta_T = 1
> \end{align}
> $$
> Draw $x_0 \sim \pi_0$, and for $t = 1, \dots, T-1$ move $x_t \sim K_t(\cdot \mid x_{t-1})$ with a [[Markov Chain Monte Carlo]] kernel leaving $\pi_t$ invariant. The final sample $x_{T-1}$ carries the importance weight
> $$
> \begin{align}
> w = \prod_{t=1}^{T} \frac{\tilde{\pi}_t(x_{t-1})}{\tilde{\pi}_{t-1}(x_{t-1})}
> \end{align}
> $$

The inverse temperature $\beta_t$ slowly "cools" the easy distribution into the complex target landscape.

# Properties
- $\mathbb{E}[w] = Z_T / Z_0$, so AIS gives an unbiased estimate of the normalizing constant (e.g. the marginal likelihood in [[Bayesian Inference]]).
- Weighted samples estimate $\mathbb{E}_{\pi_T}[f]$ as in the [[Monte Carlo Estimator]], without requiring the MCMC kernels to mix.
- Adding resampling between steps turns it into a [[Sequential Monte Carlo]] sampler.

[^1]: Monte Carlo Methods — Q&A Overview
