---
tags: computer_science, computer_vision
---

# Definition

When the [[Machine Learning|machine learning]] model fails to [[Optimization|optimize]] the [[Objective Function|objective function]] on the testing data, while doing well on the training data.[^1] In other words, the model learns to fit the properties of the training data (such as training noise or correlations in the training data) not present in the testing data. Typically, the model is more complex than it needs to be to fit the training data. As the model overfits, there may be more than one [[Function|function]] that fits the data, but selecting the best would usually depend on the optimizer (such as initialization schema).

Low training error and high validation error.

[[Regularization|Regularization]] can be used to decrease overfitting.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html