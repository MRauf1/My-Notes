---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Gibbs Sampling[^1]
> To sample a joint distribution $\pi(x_1, \dots, x_d)$, cycle through the coordinates and resample each from its full conditional given the current values of the others:
> $$
> \begin{align}
> x_j^{(t+1)} \sim \pi\big(x_j \mid x_1^{(t+1)}, \dots, x_{j-1}^{(t+1)}, x_{j+1}^{(t)}, \dots, x_d^{(t)}\big), \qquad j = 1, \dots, d
> \end{align}
> $$
> e.g. for two variables, alternate $X_1 \sim \pi(x_1 \mid X_2)$ and $X_2 \sim \pi(x_2 \mid X_1)$.

# Properties
- A special case of the [[Metropolis-Hastings Algorithm]] whose proposal is the full conditional, so the acceptance probability is always $1$.
- Useful when the joint is intractable but each conditional is tractable (e.g. conjugate models in [[Bayesian Inference]]).
- Mixes slowly when coordinates are strongly correlated, since axis-aligned moves cannot travel along a narrow diagonal ridge.
- A [[Markov Chain Monte Carlo]] method.

[^1]: Monte Carlo Methods — Q&A Overview
