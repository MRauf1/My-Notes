---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Learning Rate)[^1]
> A hyperparameter $\eta$ of [[Gradient Descent|gradient descent]] and related [[Gradient-Based Learning|gradient-based learning algorithms]] that controls the step size taken at each iteration, equal to the learning rate times the gradient magnitude.

# Properties
- If sufficiently small, together with a random parameter initialization, gradient descent will almost surely converge to a local minimum; however, to descend more quickly, it can help to use a higher learning rate.
- Often varied over the course of training according to a [[Learning Rate Schedule]] rather than held fixed.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
