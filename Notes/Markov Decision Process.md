---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Markov Decision Process (MDP)
> A tuple $M = (\mathcal{S}, \mathcal{A}, P, R, \gamma)$ modeling the interaction between an agent and an environment, specified by:
> - State space $\mathcal{S}$ (finite).
> - Action space $\mathcal{A}$ (finite).
> - [[Transition Function]] $P: \mathcal{S} \times \mathcal{A} \to \Delta(\mathcal{S})$.
> - [[Reward Function (Markov Decision Process)|Reward function]] $R: \mathcal{S} \times \mathcal{A} \to [0, R_{max}]$.
> - [[Discount Factor]] $\gamma \in [0, 1)$.
>
> When the initial state distribution $d_0 \in \Delta(\mathcal{S})$ is of importance to the discussion, it is included as part of the tuple: $M = (\mathcal{S}, \mathcal{A}, P, R, \gamma, d_0)$.

# Properties
- The agent starts at some state $s_1$ (sampled from $d_0$ when specified), and at each time step $t = 1, 2, \dots$ takes an action $a_t \in \mathcal{A}$, obtains immediate reward $r_t = R(s_t, a_t)$, and observes the next state $s_{t+1} \sim P(s_t, a_t)$.
- This interaction protocol generates a [[Trajectory]].
- The agent chooses a [[Policy]] $\pi$ to maximize the expected [[Discounted Return]], i.e. the [[Value Function|value]] $V^\pi_M(s_1)$.
- $\Delta(\mathcal{S})$ denotes the [[Simplex|probability simplex]] over $\mathcal{S}$, i.e. the space of probability distributions over $\mathcal{S}$.

# Types
- [[Finite-Horizon Markov Decision Process]]
