---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Learned Function)[^1]
> The algorithm $f: \mathcal{X} \to \mathcal{Y}$ output by a learner, mapping inputs $\mathbf{x} \in \mathcal{X}$ to outputs $\mathbf{y} \in \mathcal{Y}$.

# Properties
- Selected from a [[Hypothesis Space]] $\mathcal{F}$, the set of all functions under consideration by the learner.
- Evaluated by an [[Objective Function]], typically a [[Loss Function|loss]] $L: \mathcal{Y} \to \mathbb{R}$ scoring its outputs directly, or $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$ comparing its outputs to target answers.
- In [[Empirical Risk Minimization|ERM]], the learned function is the one minimizing average loss over the training data; in [[Maximum Likelihood Learning|maximum likelihood learning]], it is instead the one assigning the highest probability to the training data.

[^1]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
