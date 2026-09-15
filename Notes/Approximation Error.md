---
tags:
  - computer_science
  - computer_vision
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

# Properties
- Contrasts with [[Generalization Error]], which measures expected cost on new data rather than fit to the training data; approximation error alone going down (e.g., as [[Model Capacity]] increases) does not imply generalization error is also going down.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html