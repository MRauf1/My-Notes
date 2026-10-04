---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Ensemble Learning[^1]
> Building several models and combining their predictions, either by taking the mean of the outputs (regression) or of the pre-softmax activations (classification), or, for robustness, the median output (regression) or the most frequent class (classification).

# Types
- Different random initializations, which helps far from the training data, where the fitted function is relatively unconstrained and different models disagree.[^2]
- [[Bagging]]: models trained on bootstrap resamples of the training data.
- Different [[Hyperparameter|hyperparameters]], or completely different families of models.[^3]

# Properties
- Reliably improves test performance, at the cost of training and storing multiple models and running inference multiple times.
- Averaging assumes the models' errors are independent and cancel out, reducing variance ([[Bias-Variance Tradeoff]]).
- [[Dropout]] with Monte Carlo inference and the Bayesian [[Predictive Distribution]] (an infinite weighted ensemble) are closely related.

[^1]: [Prince, p. 145](zotero://open-pdf/library/items/BWT7FYX5?page=159&annotation=FTAYQGZ8); [Prince, p. 146](zotero://open-pdf/library/items/BWT7FYX5?page=160&annotation=PFP7RHVZ); [Prince, p. 146](zotero://open-pdf/library/items/BWT7FYX5?page=160&annotation=H6B8MYS2)
[^2]: [Prince, p. 146](zotero://open-pdf/library/items/BWT7FYX5?page=160&annotation=XVVM6JD6)
[^3]: [Prince, p. 147](zotero://open-pdf/library/items/BWT7FYX5?page=161&annotation=8F8EJW9W)
