---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Markov Chain Monte Carlo[^1]
> To sample from $\pi(x) = \tilde{\pi}(x)/Z$ when only $\tilde{\pi}$ can be evaluated and the normalizing constant $Z = \int \tilde{\pi}(x)\,dx$ is intractable, construct a Markov chain $X_0, X_1, \dots$ with transition kernel $K$ whose stationary distribution is $\pi$:
> $$
> \begin{align}
> \int \pi(x)\,K(x' \mid x)\,dx = \pi(x')
> \end{align}
> $$
> and estimate expectations by ergodic averages $\frac{1}{N}\sum_{t=1}^N f(X_t) \to \mathbb{E}_\pi[f]$.

# Types
- [[Metropolis-Hastings Algorithm]]
- [[Gibbs Sampling]]
- [[Metropolis-Adjusted Langevin Algorithm]]
- [[Hamiltonian Monte Carlo]]

# Properties
- Stationarity is usually ensured by detailed balance, $\pi(x)K(x' \mid x) = \pi(x')K(x \mid x')$.
- Samples are correlated, so the effective sample size is smaller than $N$ and early samples (burn-in) are biased by the initialization.
- Only ratios $\tilde{\pi}(x')/\tilde{\pi}(x)$ are needed, so $Z$ cancels — the standard tool for sampling posteriors in [[Bayesian Inference]].
- Can get stuck in one of several separated modes; [[Sequential Monte Carlo]] and [[Annealed Importance Sampling]] address this.
- A family of the [[Monte Carlo Method]].

[^1]: Monte Carlo Methods — Q&A Overview
