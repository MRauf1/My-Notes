---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (Approximation Error)
> $$
> \begin{align}
> J_{approx} = \frac{1}{N} \sum_{i=1}^{N} L(f_{\theta}(x^{(i)}_{train}), y^{(i)}_{train})
> \end{align}
> $$

The [[Cost Function|cost]] between the predicted training samples and the ground truth training samples.[^1]

This is the cost function being minimized in [[Empirical Risk Minimization|ERM]].

[^1]: https://visionbook.mit.edu/problem_of_generalization.html