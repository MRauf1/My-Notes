---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Novelty Detection (Outlier Detection)[^1]
> Detecting new data points that have low probability under a model of the input distribution $p(\mathbf{x})$, and for which the model's predictions may therefore be of low accuracy.

# Properties
- Requires a model of the marginal density of the inputs, which a [[Generative Model|generative]] approach provides via $p(\mathbf{x}) = \sum_k p(\mathbf{x} | \mathcal{C}_k)\,p(\mathcal{C}_k)$, but a [[Discriminative Model]] or [[Discriminant Function]] does not ([[Three Approaches to Decision Problems]]).
- A form of [[Density Estimation]] used as a guard on downstream predictions.
- In high dimensions, low density does not imply atypicality: typical samples of a Gaussian lie in a thin shell far from its high-density mode ([[Curse of Dimensionality]]).

[^1]: [Bishop, 2006, p. 44](zotero://open-pdf/library/items/5G99AZ8U?page=64&annotation=I9D3CDSL)
