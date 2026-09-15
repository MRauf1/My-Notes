---
tags:
  - computer_science
  - computer_vision
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

# Properties
- Approximated in practice by measuring performance on a [[Validation Set]], rather than computed exactly, since the true data-generating distribution is unknown.
- As a function of [[Model Capacity|model capacity]] (e.g., the degree $K$ in [[Polynomial Regression]]), generalization error is often U-shaped: high when [[Underfitting|underfitting]], decreasing as capacity grows, then increasing again when [[Overfitting|overfitting]]; [[Model Capacity|recent findings on overparameterized models]] show this shape does not always hold once capacity grows far past the interpolation point.
- Contrasts with [[Approximation Error]], which measures fit to the training data rather than to new data.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html