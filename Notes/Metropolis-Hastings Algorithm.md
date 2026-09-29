---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Metropolis-Hastings Algorithm[^1]
> From the current state $x$, propose $x' \sim q(\cdot \mid x)$ and accept it with probability
> $$
> \begin{align}
> \alpha(x, x') = \min\!\left(1, \frac{\tilde{\pi}(x')\,q(x \mid x')}{\tilde{\pi}(x)\,q(x' \mid x)}\right)
> \end{align}
> $$
> otherwise stay at $x$. The resulting chain has stationary distribution $\pi = \tilde{\pi}/Z$.

# Types
- **Random walk Metropolis–Hastings**: a symmetric local proposal, e.g. $x' = x + \epsilon\,\xi$ with $\xi \sim \mathcal{N}(0, I)$, for which $q(x \mid x') = q(x' \mid x)$ and $\alpha = \min(1, \tilde{\pi}(x')/\tilde{\pi}(x))$ (the original Metropolis algorithm).
- [[Metropolis-Adjusted Langevin Algorithm]]: a gradient-informed proposal.
- [[Hamiltonian Monte Carlo]]: a proposal from simulated Hamiltonian dynamics.
- [[Gibbs Sampling]]: conditional proposals that are always accepted.

# Properties
- The acceptance ratio satisfies detailed balance, making it a valid [[Markov Chain Monte Carlo]] kernel.
- $Z$ cancels in the ratio, so only the unnormalized density $\tilde{\pi}$ is needed.
- Random walk proposals mix slowly (diffusively) in high dimensions: the step size must shrink with $d$ to keep acceptance reasonable.

[^1]: Monte Carlo Methods — Q&A Overview
