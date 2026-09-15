---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Validation Set)[^1]
> A heldout subset of data, disjoint from the data used for [[Training Phase|training]] and [[Testing Phase|testing]], used to approximate a model's [[Generalization Error]] without touching the test set.

# Properties
- Generalization error is approximated by measuring performance on the validation set:
> $$
> \begin{align}
> J_{gen} \approx \frac{1}{N}\sum_{i=1}^N \mathcal{L}(f_\theta(x^{(i)}_{val}), y^{(i)}_{val})
> \end{align}
> $$
- Kept separate from the [[Training Phase|training data]] used to compute [[Approximation Error]], so that it reflects how well the model generalizes rather than how well it fits data it has already seen.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
