---
tags:
  - computer_science
  - computer_vision
---

# Definition

A type of [[Gradient Descent|gradient descent]], where instead of calculating the [[Gradient Vector|gradients]] of all training data (expensive), the algorithm samples (without replacement) a batch of training data and calculates the gradient for that batch. Then it continues for a different batch until all batches have been used up ($1$ epoch has finished).[^1]

Less accurate than full gradient descent, but is faster and less expensive to computer, which creates a tradeoff between accuracy and speed.

For a [[Cost Function]] that is the average of per-example losses, $J(\theta) = \frac{1}{N}\sum_{i=1}^N \mathcal{L}(f_\theta(\mathbf{x}^{(i)}), \mathbf{y}^{(i)})$, SGD estimates the full gradient by averaging over a randomly sampled batch of [[Batch Size|size]] $B$:
$$
\begin{align}
\tilde{\mathbf{g}} = \frac{1}{N}\sum_{b=1}^B \nabla_\theta \mathcal{L}(f_\theta(\mathbf{x}^{(b)}), \mathbf{y}^{(b)})
\end{align}
$$

Because a random batch is sampled, SGD may be able to jump over small bumps in the loss curvature.

SGD can implicitly regularize the learning problem; for example, for linear problems (i.e., $f_\theta$ linear) with multiple parameter settings that minimize the loss, SGD will often converge specifically to the solution with minimum parameter norm.

# Cons
- Need to normalize the inputs
- The learning rate is not adaptive

[^1]: https://visionbook.mit.edu/gradient_descent.html