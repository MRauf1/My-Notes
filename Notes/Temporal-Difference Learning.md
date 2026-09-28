---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Temporal-Difference Learning[^1]
> A [[Reinforcement Learning|reinforcement-learning]] method that updates a [[Value Function|value function]] from the discrepancy between successive predictions ("learning a guess from a guess"), using the temporal-difference error
> $$\begin{align}
> \delta_t &= r_{t+1} + \gamma V(s_{t+1}) - V(s_t), \\
> V(s_t) &\leftarrow V(s_t) + \alpha\, \delta_t,
> \end{align}$$
> where $\gamma$ is the discount factor and $\alpha$ the learning rate.

# Properties
- $\delta_t > 0$ means the world suddenly seems more promising than predicted, $\delta_t < 0$ less promising, and $\delta_t = 0$ that things are exactly as good or bad as expected.[^1]
- Phasic [[Dopamine|dopamine]] signals implement the TD error in the brain ([[Reward Prediction Error Hypothesis]]).[^2]
- Addresses the [[Temporal Credit Assignment Problem]] by propagating value backward through time.

[^1]: [Christian, 2021, p. 145](zotero://open-pdf/library/items/P27SWKW4?page=145&annotation=YJIQPLAC); [Christian, 2021, p. 145](zotero://open-pdf/library/items/P27SWKW4?page=145&annotation=2WITGJMR); [Christian, 2021, p. 145](zotero://open-pdf/library/items/P27SWKW4?page=145&annotation=7JAADVKQ)
[^2]: [Christian, 2021, p. 145](zotero://open-pdf/library/items/P27SWKW4?page=145&annotation=W3X3NDCX)
