---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Effective Horizon
> The number of iterations $H \geq \dfrac{\log(R_{max}/(\epsilon(1-\gamma)))}{1-\gamma}$ sufficient for [[Value Iteration]] to compute a Q-value function $\epsilon$-close to $Q^\star$.

# Properties
- Often simplified to the rule of thumb $H = O\left(\dfrac{1}{1-\gamma}\right)$, used to translate between the [[Finite-Horizon Markov Decision Process|finite-horizon undiscounted]] and infinite-horizon discounted settings.
- The term "horizon" is often used generically in the discounted setting to mean $O(1/(1-\gamma))$.
