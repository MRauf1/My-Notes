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
- Also called a **hold-out set**; used to optimize model complexity (e.g. the polynomial order $M$ or the regularization coefficient $\lambda$) while the training set determines the parameters $\mathbf{w}$ ([[Model Selection]]).[^2]
- If the model design is iterated many times on a limited data set, the model can over-fit the validation data, so a third test set may be kept aside for the final evaluation.[^3]
- Often too wasteful of scarce training data, and a small validation set gives a noisy estimate of performance, motivating [[Cross-Validation]].
- Kept separate from the [[Training Phase|training data]] used to compute [[Approximation Error]], so that it reflects how well the model generalizes rather than how well it fits data it has already seen.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
[^2]: [Bishop, 2006, p. 11](zotero://open-pdf/library/items/5G99AZ8U?page=31&annotation=V3VEJ6V8)
[^3]: [Bishop, 2006, p. 32](zotero://open-pdf/library/items/5G99AZ8U?page=52&annotation=SWB3LAH4)
