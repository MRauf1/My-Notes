---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Reward Function)[^1]
> In [[Reinforcement Learning]], a function $r: \mathcal{Y} \to \mathbb{R}$ that explicitly measures the quality of a learned function's output. The learner tries to come up with a function that maximizes reward.

# Properties
- Plays a role analogous to a [[Loss Function|loss]] or [[Objective Function]] in other kinds of learning, except that reward is maximized rather than minimized.
- Becoming an increasingly important part of computer vision, especially in the context of vision for robots.
- Compare with the [[Reward Function (Markov Decision Process)|reward function]] of a [[Markov Decision Process]], which is formalized instead as a function of state-action pairs, $R: \mathcal{S} \times \mathcal{A} \to [0, R_{max}]$.

[^1]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
