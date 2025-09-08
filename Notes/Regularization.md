---
tags: computer_science, computer_vision
---

# Definition

Mechanisms that penalize [[Function Complexity|function complexity]] in order to reduce/prevent [[Overfitting|overfitting]].[^1]

These are additional [[Term|terms]] added to the [[Objective Function|objective function]] that guides towards simpler [[Function|functions]]. Ideally, one wants a function that is complex enough to fit the data, while not too complex/flexible as to cause overfitting.

They embody the principle of Occam's Razor: when multiple functions can fit the data, choose the simplest one.

Regularizers can also be thought of as [[Bayes' Theorem|priors]] for the types of functions that are to be selected (hypothesis).

# Types

- $L_p$ [[Norm|Norms]]
	- These encourages most parameters to be $0$/near $0$.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html