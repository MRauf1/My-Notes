---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Sequential Monte Carlo[^1]
> Sequential Monte Carlo approximates a sequence of distributions $\pi_0, \pi_1, \dots, \pi_T$ by a population of weighted particles $\{(x^{(i)}, w^{(i)})\}_{i=1}^N$, $\pi_t \approx \sum_i w^{(i)} \delta_{x^{(i)}}$. At each step $t$ it
> 1. **propagates** each particle through a transition kernel $x_t^{(i)} \sim q_t(\cdot \mid x_{t-1}^{(i)})$,
> 2. **reweights** by the incremental importance weight $w_t^{(i)} \propto w_{t-1}^{(i)}\,\dfrac{\pi_t(x_{0:t}^{(i)})}{\pi_{t-1}(x_{0:t-1}^{(i)})\,q_t(x_t^{(i)} \mid x_{t-1}^{(i)})}$, and
> 3. **resamples** particles in proportion to their weights, duplicating heavy particles and discarding light ones.

# Types
- **Particle filter**: $\pi_t$ is the filtering posterior $p(x_t \mid y_{1:t})$ of a state-space model as observations $y_t$ arrive; the bootstrap filter propagates by the dynamics $p(x_t \mid x_{t-1})$ and weights by the likelihood $p(y_t \mid x_t)$.
- **SMC samplers**: $\pi_t$ is an artificial bridge from an easy distribution to a hard static target, as in [[Annealed Importance Sampling]] with added resampling.

# Properties
- Resampling combats weight degeneracy (all weight concentrating on one particle), at the cost of losing particle diversity; it is typically triggered when the effective sample size $1/\sum_i (w^{(i)})^2$ falls below a threshold.
- Handles multimodal targets better than a single [[Markov Chain Monte Carlo]] chain, since particles can occupy several modes simultaneously.
- Built on the importance-weighting construction of the [[Monte Carlo Estimator]].

[^1]: Monte Carlo Methods — Q&A Overview
