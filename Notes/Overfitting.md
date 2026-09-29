---
tags:
  - computer_science
  - computer_vision
---

# Definition

When the [[Machine Learning|machine learning]] model fails to [[Optimization|optimize]] the [[Objective Function|objective function]] on the testing data, while doing well on the training data.[^1] In other words, the model learns to fit the properties of the training data (such as training noise or correlations in the training data) not present in the testing data. Typically, the model is more complex than it needs to be to fit the training data. As the model overfits, there may be more than one [[Function|function]] that fits the data, but selecting the best would usually depend on the optimizer (such as initialization schema).

Low training error and high validation error.

[[Regularization|Regularization]] can be used to decrease overfitting.

A learner may perform poorly for one of two reasons: it may fail to optimize the objective on the training data at all ([[Underfitting]]), or it may succeed on the training data in a way that does not generalize to the test setting (overfitting).

# Properties
- Intuitively, more flexible models (e.g. higher-order polynomials) become increasingly tuned to the random noise on the target values.[^2]
- For a given model complexity, over-fitting becomes less severe as the data set grows: the larger the data set, the more complex a model one can afford to fit. A rough heuristic asks for a number of data points no less than some multiple (say $5$ or $10$) of the number of adaptive parameters, though the number of parameters is not necessarily the right measure of [[Model Capacity|model complexity]].[^3]
- Can be understood as a general property of [[Maximum Likelihood Estimation|maximum likelihood]] (least squares being a special case); its root is the bias of maximum likelihood, as in the underestimated variance of [[Normal Distribution Maximum Likelihood Estimation]]. A Bayesian approach, which marginalizes over parameters ([[Predictive Distribution]]), avoids it: models with far more parameters than data points pose no difficulty, since the effective number of parameters adapts automatically to the size of the data set.[^4]
- Controlled by [[Regularization]], or by choosing complexity through [[Model Selection]] ([[Validation Set]], [[Cross-Validation]]).
- **Why overparameterized deep networks often do not overfit** despite having far more parameters than training datapoints is an active research question, but several findings help explain it: see [[Model Capacity]] for a summary of double descent, benign overfitting, and the implicit regularization of gradient-based training.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html
[^2]: [Bishop, 2006, p. 9](zotero://open-pdf/library/items/5G99AZ8U?page=29&annotation=GDXNE3K5)
[^3]: [Bishop, 2006, p. 9](zotero://open-pdf/library/items/5G99AZ8U?page=29&annotation=6C4RVSZG)
[^4]: [Bishop, 2006, p. 9](zotero://open-pdf/library/items/5G99AZ8U?page=29&annotation=SWZX4766)