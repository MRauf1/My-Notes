---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Finite-Horizon Markov Decision Process
> A [[Markov Decision Process]] in which the agent acts for only a fixed, finite number of time steps $H$ (the horizon), with no discounting.

# Properties
- Can be emulated by an infinite-horizon discounted [[Markov Decision Process]] via state-space augmentation: given $M = (\mathcal{S}, \mathcal{A}, P, R)$ with horizon $H$, define $\tilde{M} = (\tilde{\mathcal{S}}, \mathcal{A}, \tilde{P}, \tilde{R}, \gamma{=}1)$ with $\tilde{\mathcal{S}} = (\mathcal{S} \times [H]) \cup \{s_{absorbing}\}$: $H$ level-indexed copies of the state space plus an [[Absorbing State]] that all actions transition into with $0$ reward.
- Transitions only go from level $h$ to level $h+1$, with $\tilde{P}((s', h{+}1) \mid (s,h), a) = P(s'|s,a)$; states at the last level $(s, H)$ transition to $s_{absorbing}$ deterministically, and $\tilde{R}((s,h), a) = R(s,a)$.
- Although $\gamma = 1$ can generally cause infinite value, the agent always loops in $s_{absorbing}$ after $H$ steps and receives no further reward, so the total reward — and hence value — remains finite.
- The optimal policy for a finite-horizon MDP is generally non-stationary: it depends on both the state $s$ and the time step $h$, unlike the stationary [[Optimal Policy]] of the infinite-horizon discounted setting.
- An instance of an [[Episodic Task]].
