---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Flow Equations[^1]
> The constraint of the [[Dual Linear Program (Markov Decision Process)|dual linear program]] for a [[Markov Decision Process]] with initial distribution $d_0$ and transition matrix $P$:
> $$
> \begin{align}
> \left[\sum_{a\in\mathcal{A}} d(s,a)\right]_{s\in\mathcal{S}} = \gamma P^\top d + (1-\gamma) d_0
> \end{align}
> $$
> characterizing the space of discounted [[State-Action Occupancy|state-action occupancies]] $d$ of stationary policies.

# Properties
- The LHS marginalizes out actions to give the induced [[Discounted State Occupancy|state occupancy]] $\tilde{d}^\pi$.
- $P^\top q$, for a state-action distribution $q$, "pushes" $q$ through the MDP dynamics for one time step: $s' \sim P^\top q \iff (s,a) \sim q, \; s' \sim P(\cdot|s,a)$.
- Satisfied by $d = d^\pi$, the state-action occupancy of any policy $\pi$: $\gamma P^\top d^\pi$ accounts for the state-occupancy terms from time step $2$ onward, and $(1-\gamma)d_0$ supplies the missing $t=1$ term.
- Paired against an arbitrary "test function" $f \in \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$, the flow equations become the [[Bellman Residual Telescoping Identity]] $\mathbb{E}_{d_0,\pi}[f] - J(\pi) = \frac{1}{1-\gamma}\mathbb{E}_{d^\pi}[f - \mathcal{T}^\pi f]$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 11](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=11)
