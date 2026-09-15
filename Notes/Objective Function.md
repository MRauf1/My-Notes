---
tags:
  - computer_science
  - artificial_intelligence
---

# Definition
> [!info] Definition (Objective Function)[^2]
> A function that scores a [[Learned Function|model's]] outputs, typically denoted $L: \mathcal{Y} \to \mathbb{R}$, or that compares a model's outputs to target answers, $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$.

# Properties
- A [[Loss Function|loss]] refers specifically to an objective to be minimized, whereas an objective function may also describe an objective to be maximized, such as a [[Reward Function]] in [[Reinforcement Learning]].
- In [[Empirical Risk Minimization|ERM]], the learner minimizes the average value of the objective function over the training data.
- Called a [[Cost Function]] when framed as $J(\theta)$, a function of the model parameters alone for fixed training data, as minimized by [[Gradient Descent|gradient-based optimization]].

When setting our objectives, it's hard to make sure what we think is perfectly replicated in the mathematical formulation ([[Value-Alignment Problem]]). One potential solution is not fully revealing the objective to the agent, so that the agent is more cautious, asks to learn more about what we want, and defers to human control.[^1]

While humans specify this for usual models, true AGI should be able to set its own objectives.

[^1]: [Artificial Intelligence: A Modern Approach](zotero://open-pdf/library/items/JZXT5DZQ?page=1)
[^2]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)