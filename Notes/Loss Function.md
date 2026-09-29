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
- In decision theory, a loss function (also called a cost function) is a single overall measure of loss incurred by taking any of the available decisions; a utility function is equivalent, taking utility to be the negative of the loss. For classification it is given by a loss matrix $L_{kj}$ ([[Minimum Expected Loss Decision Rule]]).[^2]
- Called a [[Cost Function]] when framed as $J(\theta)$, a function of the model parameters alone for fixed training data, as minimized by [[Gradient Descent|gradient-based optimization]].

# Types
- [[L1 Loss]]
- [[L2 Loss]]

## [[Regression]]
- [[Mean Squared Error]]

- [[Minkowski Loss]]

## [[Classification]]
- [[Cross-Entropy Loss]]

[^1]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
[^2]: [Bishop, 2006, p. 41](zotero://open-pdf/library/items/5G99AZ8U?page=61&annotation=26LZ9D5F)