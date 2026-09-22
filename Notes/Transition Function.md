---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Transition Function
> In a [[Markov Decision Process]], the function $P: \mathcal{S} \times \mathcal{A} \to \Delta(\mathcal{S})$, where $P(s' \mid s, a)$ is the probability of transitioning into state $s'$ upon taking action $a$ in state $s$.

# Properties
- Governs the randomness of state transitions along a [[Trajectory]]: $s_{t+1} \sim P(s_t, a_t)$.
- Together with the [[Reward Function (Markov Decision Process)|reward function]], [[Discount Factor]], state space, and action space, fully specifies a [[Markov Decision Process]].
- For a fixed [[Policy]] $\pi$, induces the [[Transition Matrix (Markov Decision Process)|transition matrix]] $P^\pi$, with $[P^\pi]_{s,s'} = \mathbb{E}_{a \sim \pi(s)}[P(s'|s,a)]$.
- Also represented as a matrix $P \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}| \times |\mathcal{S}|}$ (not conditioned on a policy), used e.g. in the [[Bellman Flow Equations]] of the [[Dual Linear Program (Markov Decision Process)|dual linear program]] for planning.
