---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Metropolis-Adjusted Langevin Algorithm[^1]
> Propose by one Euler–Maruyama step of the Langevin diffusion $dX_t = \nabla \log \pi(X_t)\,dt + \sqrt{2}\,dW_t$, which drifts toward high-density regions:
> $$
> \begin{align}
> x' = x + \frac{\epsilon^2}{2}\,\nabla_x \log \pi(x) + \epsilon\,\xi, \qquad \xi \sim \mathcal{N}(0, I)
> \end{align}
> $$
> and accept or reject $x'$ with the [[Metropolis-Hastings Algorithm|Metropolis–Hastings]] ratio for the Gaussian proposal $q(x' \mid x) = \mathcal{N}\big(x + \tfrac{\epsilon^2}{2}\nabla\log\pi(x),\ \epsilon^2 I\big)$.

# Properties
- Needs only $\nabla \log \pi = \nabla \log \tilde{\pi}$, which is independent of the normalizing constant $Z$ (the [[Score Function|score]] of $\pi$).
- The Metropolis correction removes the discretization bias of the unadjusted Langevin step, making $\pi$ exactly stationary.
- Scales better with dimension than random walk proposals (step size $\epsilon \propto d^{-1/6}$ versus $d^{-1/2}$).
- A [[Markov Chain Monte Carlo]] method; [[Hamiltonian Monte Carlo]] with a single leapfrog step reduces to it.

[^1]: Monte Carlo Methods — Q&A Overview
