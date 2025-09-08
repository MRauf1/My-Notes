---
tags: computer_science, computer_vision
---

# Definition

A type of [[Gradient Descent|gradient descent]], where instead of calculating the [[Gradient|gradients]] of all training data (expensive), the algorithm samples (without replacement) a batch of training data and calculates the gradient for that batch. Then it continues for a different batch until all batches have been used up ($1$ epoch has finished).[^1]

Less accurate than full gradient descent, but is faster and less expensive to computer, which creates a tradeoff between accuracy and speed.

Because a random batch is sampled, SGD may be able to jump over small bumps in the loss curvature.

SGD can implicitly regularize the learning problem.

[^1]: https://visionbook.mit.edu/gradient_descent.html