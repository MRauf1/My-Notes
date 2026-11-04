---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Absorbing State[^1]
> A state $s_{absorbing}$ in a [[Markov Decision Process]] from which all actions transition back to itself and yield $0$ reward.

# Properties
- Used to model termination in an [[Episodic Task]].
- Lets an otherwise infinite-horizon discounted MDP (even with $\gamma = 1$) retain finite value, since the agent accumulates no further reward once absorbed.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 5](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=5)
