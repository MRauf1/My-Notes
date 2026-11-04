---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Actor-Critic[^1]
> A family of policy gradient methods that combine a parameterized policy (the **actor**) with an estimated value function $\hat{V}^\pi$ or $\hat{Q}^\pi$ (the **critic**) in the [[Policy Gradient Theorem]], e.g.
> $$
> \begin{align}
> \widehat{\nabla J} \propto \nabla_\theta\log\pi(a|s)\,\big(\hat{Q}^\pi(s,a) - \hat{V}^\pi(s)\big), \qquad (s,a) \sim d^\pi.
> \end{align}
> $$
> The critic assesses the actor's performance and guides how to improve it (Konda & Tsitsiklis 2000).

# Properties
- Using $\hat{V}^\pi$ only as a baseline keeps the gradient unbiased, since $\mathbb{E}_{a\sim\pi}[\nabla\log\pi(a|s)] = 0$. Replacing $Q^\pi$ by $\hat{Q}^\pi$ reduces variance further at the cost of bias.
- The critic is typically estimated by dynamic programming / [[Temporal-Difference Learning]]. Compare the [[Critic]] of a learning agent.
- Compare [[REINFORCE]], which uses the Monte Carlo return instead of a critic.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 8](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=8)
