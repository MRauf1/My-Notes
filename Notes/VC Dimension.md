---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] VC Dimension[^1]
> The Vapnik-Chervonenkis dimension of a class of binary classifiers $\mathcal{F}$ (Vapnik & Chervonenkis, 1971) is the largest number of training examples that the class can label arbitrarily, i.e. the size of the largest set of points that $\mathcal{F}$ **shatters** (realizes all ^N$ labelings of).

# Properties
- A formal measure of [[Model Capacity]], in contrast to informal counts of parameters or hidden units.
- For neural networks, Bartlett et al. (2019) give upper and lower bounds on the VC dimension in terms of the number of layers and weights.
- Generalization bounds based on it scale with the VC dimension relative to the number of training examples, which is vacuous for [[Overparameterized Model|over-parameterized]] networks that can fit random labels ([[Double Descent]]).[^2]
- An alternative capacity measure is [[Rademacher Complexity]].

[^1]: [Prince, p. 134](zotero://open-pdf/library/items/BWT7FYX5?page=148&annotation=EYUEGV6I)
[^2]: Added from general knowledge of learning theory.
