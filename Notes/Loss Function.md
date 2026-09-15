---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Definition (Loss Function)[^1]
> An [[Objective Function]] $L$ that scores a [[Learned Function|model's]] outputs, $L: \mathcal{Y} \to \mathbb{R}$, or compares its outputs to target answers, $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$, and that is always to be minimized.

# Properties
- Unlike a general [[Objective Function]], which may describe an objective to be either minimized or maximized, a loss always refers to an objective to be minimized.
- Called a [[Cost Function]] when framed as $J(\theta)$, a function of the model parameters alone for fixed training data, as minimized by [[Gradient Descent|gradient-based optimization]].

# Types
- [[L1 Loss]]
- [[L2 Loss]]

## [[Regression]]
- [[Mean Squared Error]]

## [[Classification]]
- [[Cross-Entropy Loss]]

[^1]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)