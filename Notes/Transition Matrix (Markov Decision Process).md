---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Transition Matrix (Markov Decision Process)
> For a [[Markov Decision Process]] and [[Policy]] $\pi$, the $|\mathcal{S}| \times |\mathcal{S}|$ matrix $P^\pi$ whose $(s,s')$-th entry is
> $$
> \begin{align}
> [P^\pi]_{s,s'} = \mathbb{E}_{a \sim \pi(s)}[P(s'|s,a)]
> \end{align}
> $$

# Properties
- Describes the Markov chain induced by the [[Markov Decision Process|MDP]] $M$ and policy $\pi$: its $s$-th row is the distribution over next states upon following $\pi$ at state $s$.
- Used together with the reward vector $R^\pi$ (where $[R^\pi]_s = \mathbb{E}_{a \sim \pi(s)}[R(s,a)]$) to express the [[Bellman Equation (Policy Evaluation)|Bellman equation]] in matrix form and solve [[Policy Evaluation]] analytically.
