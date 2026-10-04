---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Hyperparameter Search[^1]
> The process of finding the best [[Hyperparameter|hyperparameters]], both model hyperparameters (e.g. the numbers of hidden layers and hidden units) and learning-algorithm hyperparameters (e.g. learning rate, batch size). For each choice, a model is trained on the training set and evaluated on a [[Validation Set]]; the best one is selected, and its performance is measured on the test set. When focused on network structure, it is called **neural architecture search**.

# Types
- **Random search**: sample the hyperparameter space randomly (Bergstra & Bengio, 2012).[^2]
- [[Bayesian Optimization]]: model performance as a function of the hyperparameters, together with its uncertainty, and sample where uncertainty is high (explore) or performance looks promising (exploit). The Beta-Bernoulli bandit is a roughly equivalent model for discrete variables.
- **SMAC** (sequential model-based configuration; Hutter et al., 2011): models the objective with a random forest, using the mean of the tree predictions as the best guess and their variance as the uncertainty; handles continuous, discrete, and conditional hyperparameters.
- **Tree-Parzen estimators** (Bergstra et al., 2011): also handles mixed and conditional hyperparameters, but models the probability of the hyperparameters given the performance rather than of the performance given the hyperparameters.
- [[Hyperband]] and BOHB, which use cheap, partial training runs to discard poor configurations early.

# Properties
- Performance is not measured on the test set for selection, since the chosen hyperparameters might just happen to suit the test set and not generalize further.[^1]
- The hyperparameter space is smaller than the parameter space but still too large to search exhaustively; many hyperparameters are discrete (e.g. number of layers) or conditional on others (the width of layer 10 matters only if there are at least 10 layers), so [[Gradient Descent]] cannot be used. Hyperparameter optimization algorithms instead sample the space intelligently given previous results.[^3]
- Expensive, since each evaluation trains an entire model; [[Cross-Validation|569JNRXghklfold cross-validation]] uses a larger proportion of the data for training, reducing variance.[^4]

[^1]: [Prince, p. 118](zotero://open-pdf/library/items/BWT7FYX5?page=132&annotation=IV4FGBA9); [Prince, p. 132](zotero://open-pdf/library/items/BWT7FYX5?page=146&annotation=2997MF4K); [Prince, p. 133](zotero://open-pdf/library/items/BWT7FYX5?page=147&annotation=JZRS9992)
[^2]: [Prince, p. 135](zotero://open-pdf/library/items/BWT7FYX5?page=149&annotation=8V7CBB8K); [Prince, p. 136](zotero://open-pdf/library/items/BWT7FYX5?page=150&annotation=T2T8G9K2); [Prince, p. 136](zotero://open-pdf/library/items/BWT7FYX5?page=150&annotation=5B5F5TGY)
[^3]: [Prince, p. 133](zotero://open-pdf/library/items/BWT7FYX5?page=147&annotation=GCM7T53K)
[^4]: [Prince, p. 134](zotero://open-pdf/library/items/BWT7FYX5?page=148&annotation=96Y2TTSV)
