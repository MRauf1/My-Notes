---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Feature Extraction (Pre-processing)[^1]
> A pre-processing stage that transforms the original input variables $\mathbf{x}$ into a new space of variables in which, it is hoped, the [[Pattern Recognition|pattern recognition]] problem will be easier to solve.

# Properties
- New test data must be pre-processed using exactly the same steps (and the same fitted parameters, e.g. normalization statistics computed on the training set) as the training data.[^1]
- May also be performed to speed up computation, e.g. by reducing the dimensionality of the input and discarding information irrelevant to the task.[^2]
- [[Featurization]] is the special case in which features $\boldsymbol{\phi}(\mathbf{x})$ are chosen so that a model nonlinear in $\mathbf{x}$ becomes a [[Linear Model|linear model]] in its parameters.
- Mitigates the [[Curse of Dimensionality]] by mapping inputs to a lower-dimensional space that retains the task-relevant variation.

[^1]: [Bishop, 2006, p. 2](zotero://open-pdf/library/items/5G99AZ8U?page=22&annotation=Q7LYJMRM)
[^2]: [Bishop, 2006, p. 2](zotero://open-pdf/library/items/5G99AZ8U?page=22&annotation=MGNBKQ85)
