---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Hamiltonian Monte Carlo[^1]
> Augment the state $x$ with an auxiliary momentum $p \sim \mathcal{N}(0, M)$ and define the Hamiltonian, i.e. [[Potential Energy|potential]] plus [[Kinetic Energy|kinetic energy]],
> $$
> \begin{align}
> H(x, p) = U(x) + \tfrac{1}{2}\,p^\top M^{-1} p, \qquad U(x) = -\log \pi(x)
> \end{align}
> $$
> Each iteration resamples $p$, simulates Hamilton's equations $\dot{x} = M^{-1}p$, $\dot{p} = -\nabla U(x)$ for $L$ leapfrog steps of size $\epsilon$ to reach $(x', p')$, and accepts with probability $\min\big(1, \exp(H(x,p) - H(x',p'))\big)$.

The trajectory glides frictionlessly along level sets of the energy landscape, so proposals can be far from $x$ yet still have high acceptance probability.

# Properties
- The joint density $\propto e^{-H(x,p)}$ has marginal $\pi(x)$, so discarding $p$ yields samples of $\pi$.
- Exact Hamiltonian flow conserves $H$ ([[Conservation of Mechanical Energy]]); the leapfrog integrator is volume-preserving and reversible, so only its small energy error needs the [[Metropolis-Hastings Algorithm|Metropolis–Hastings]] correction.
- Makes long, non-diffusive moves, scaling as $\epsilon \propto d^{-1/4}$ versus $d^{-1/2}$ for random walk proposals.
- The No-U-Turn Sampler (NUTS) chooses $L$ adaptively by extending the trajectory until it starts to double back.
- A [[Markov Chain Monte Carlo]] method; with $L = 1$ it reduces to the [[Metropolis-Adjusted Langevin Algorithm]].

[^1]: Monte Carlo Methods — Q&A Overview
