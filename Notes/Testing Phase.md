---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Testing Phase)[^1]
> The phase of [[Machine Learning|learning]] in which the algorithm produced during the [[Training Phase]] is deployed to solve new instances of the problem.

# Properties
- Performance on the testing phase's new instances, rather than on the [[Training Phase|training]] instances themselves, is what learning ultimately aims to optimize.
- The new inputs on which the trained model is evaluated form the **test set**; correctly handling them is [[Generalization|generalization]]. When model design has been iterated against a [[Validation Set]], a separate test set is kept aside for the final evaluation.[^2]

[^1]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)
[^2]: [Bishop, 2006, p. 2](zotero://open-pdf/library/items/5G99AZ8U?page=22&annotation=WGK999BD)
