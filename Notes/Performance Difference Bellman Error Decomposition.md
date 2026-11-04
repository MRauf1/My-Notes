---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Performance Difference Bellman Error Decomposition[^1]
> For all policies $\pi, \hat{\pi}$ and all $f \in \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$, with $d^\pi$ the normalized discounted [[State-Action Occupancy|state-action occupancy]] from $d_0$ and $\mathcal{T}^{\hat{\pi}}$ the [[Bellman Evaluation Operator]],
> $$
> \begin{align}
> J(\pi) - J(\hat{\pi}) = \underbrace{\frac{1}{1-\gamma}\mathbb{E}_{d^\pi}\big[f(s,\pi) - f(s,\hat{\pi})\big]}_{\text{policy optimization error}} + \frac{1}{1-\gamma}\mathbb{E}_{d^{\hat{\pi}}}\big[f - \mathcal{T}^{\hat{\pi}}f\big] - \frac{1}{1-\gamma}\mathbb{E}_{d^\pi}\big[f - \mathcal{T}^{\hat{\pi}}f\big].
> \end{align}
> $$

# Properties
- An *identity* for every $f$. With $f = Q^{\hat{\pi}}$, both Bellman-error terms vanish and it reduces to the [[Performance Difference Lemma]].
- **Recovers the [[Bellman Error Performance Difference Bound]]** with $\hat{\pi} = \pi_f$ (the source writes $\pi = \pi_f$, but the reduction needs the *learned* policy to be greedy): the policy optimization error is $\leq 0$ by greediness, and $\mathcal{T}^{\pi_f}f = \mathcal{T}f$.
- Organizes several algorithms: [[Natural Policy Gradient]] controls the policy optimization error by mirror descent ([[Natural Policy Gradient Convergence Bound]]). *Pessimism* makes the $d^{\hat{\pi}}$ term non-positive, so data need only cover the comparator. *Optimism* removes the $d^\pi$ term instead, which drives efficient exploration.
- The second term equals $\mathbb{E}_{d_0}[f(s,\hat{\pi})] - J(\hat{\pi})$ by the [[Bellman Residual Telescoping Identity]].

# Questions
> [!question]- How does the decomposition recover the Bellman error performance difference bound $J(\pi) - J(\pi_f) \leq \frac{1}{1-\gamma}(\mathbb{E}_{d^\pi}[\mathcal{T}f - f] + \mathbb{E}_{d^{\pi_f}}[f - \mathcal{T}f])$?
> Set $\hat{\pi} = \pi_f$. Greediness gives $f(s,\pi) \leq \max_a f(s,a) = f(s,\pi_f)$, so the policy optimization error is $\leq 0$. And $\mathcal{T}^{\pi_f}f = \mathcal{T}f$, since $\pi_f$ attains the max in $V_f$. The remaining two terms are $\frac{1}{1-\gamma}\mathbb{E}_{d^{\pi_f}}[f - \mathcal{T}f] + \frac{1}{1-\gamma}\mathbb{E}_{d^\pi}[\mathcal{T}f - f]$.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 12](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=12)
