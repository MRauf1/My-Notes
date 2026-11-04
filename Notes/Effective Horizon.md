---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Effective Horizon[^1]
> The number of iterations $H \geq \dfrac{\log(R_{max}/(\epsilon(1-\gamma)))}{1-\gamma}$ sufficient for [[Value Iteration]] to compute a Q-value function $\epsilon$-close to $Q^\star$.

# Properties
- Often simplified to the rule of thumb $H = O\left(\dfrac{1}{1-\gamma}\right)$, used to translate between the [[Finite-Horizon Markov Decision Process|finite-horizon undiscounted]] and infinite-horizon discounted settings.
- The term "horizon" is often used generically in the discounted setting to mean $O(1/(1-\gamma))$.

# Questions
> [!question]- Verify that $H \geq \frac{\log(R_{max}/(\epsilon(1-\gamma)))}{1-\gamma}$ gives $\gamma^H R_{max}/(1-\gamma) \leq \epsilon$.
> Write $\gamma^H = (1 - (1-\gamma))^{\frac{1}{1-\gamma}\cdot H(1-\gamma)}$ and use $(1 - 1/x)^x \leq 1/e$ for $x > 1$, with $x = 1/(1-\gamma)$. Then $\gamma^H \leq e^{-H(1-\gamma)} \leq \frac{\epsilon(1-\gamma)}{R_{max}}$. Multiplying by $R_{max}/(1-\gamma)$ gives $\epsilon$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 9](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=9)
