---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Discount Factor
> In a [[Markov Decision Process]], the constant $\gamma \in [0, 1)$ that defines a horizon for the problem, weighting the reward received $t$ steps in the future by $\gamma^{t-1}$ in the [[Discounted Return]].

# Properties
- Because $\gamma < 1$, the sum $\sum_{t=1}^{\infty} \gamma^{t-1} R_{max} = \dfrac{R_{max}}{1-\gamma}$ converges, which bounds the [[Discounted Return]] and hence the [[Value Function|value]] and [[Action-Value Function|action-value]] functions in $[0, R_{max}/(1-\gamma)]$.
- This boundedness is important when analyzing the error propagation of planning and learning algorithms.
