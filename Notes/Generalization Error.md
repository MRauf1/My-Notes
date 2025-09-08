---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (Generalization Error)
> $$
> \begin{align}
> J_{gen} &= \mathbb{E}_{x,y \sim data} [L(f_{\theta}(x), y)] = \\
> &\approx \frac{1}{N} \sum_{i=1}^{N} L(f_{\theta}(x^{(i)}_{val}), y^{(i)}_{val})
> \end{align}
> $$

The expected [[Cost Function|cost]] between the predicted testing sample and the ground truth testing sample.[^1]

In [[Machine Learning|learning]], this is the cost function that one wants to be minimized for good performance of the model.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html