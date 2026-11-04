---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Multi-Armed Bandit (MAB)[^1]
> A multi-armed bandit problem is specified by $K$ [[Probability Distribution|distributions]] $\{R_i\}_{i=1}^K$ over $\mathbb{R}$, each supported on $[0, 1]$ with mean $\mu_i$. Let $\mu^\star = \max_{i \in [K]} \mu_i$. In each round $t = 1, 2, \dots, T$, the learner
> 1. chooses an arm $i_t \in [K]$, and
> 2. receives a reward $r_t \sim R_{i_t}$.

# Properties
- The learner only observes the reward of the arm it pulls, so it must trade off trying arms against using the empirically best one ([[Exploration-Exploitation Tradeoff]]).
- Common objectives:
  - [[Pseudo-Regret]], which poses the exploration–exploitation challenge.
  - [[Simple Regret]], which poses the pure-exploration challenge.
  - [[Best-Arm Identification]].
- Can be viewed as a [[Markov Decision Process]] with a single state and stochastic rewards: actions are arms, and there are no state transitions to plan over.
- The simplest algorithm, sampling every arm equally, is analysed by the [[Uniform Sampling Simple Regret Bound]]. The [[Best-Arm Identification Lower Bound]] shows that its linear dependence on $K$ is unavoidable.
- Adding a context observed before each pull gives the [[Contextual Bandit]].

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=2)
