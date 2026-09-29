---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Inference (Machine Learning)[^1]
> Computing the prediction $\mathbf{y}$ from the input $\mathbf{x}$ by passing it through the model with fixed parameters $\boldsymbol{\phi}$:
> $$
> \begin{align}
> \mathbf{y} = \mathbf{f}[\mathbf{x}, \boldsymbol{\phi}]
> \end{align}
> $$

# Properties
- The model $\mathbf{f}[\bullet, \boldsymbol{\phi}]$ is an equation of fixed form describing a family of possible input-output relationships; the parameters $\boldsymbol{\phi}$ select the particular relationship ([[Supervised Learning Formulation from Machine Learning Perspective]], [[Hypothesis Space]]).[^2]
- Performed after the [[Training Phase]] has chosen $\hat{\boldsymbol{\phi}}$, in the hope that predictions are good on new inputs whose true output is unknown ([[Generalization]], [[Testing Phase]]).
- Direct for a [[Discriminative Model]]; for a [[Generative Model]] $\mathbf{x} = \mathbf{g}[\mathbf{y}, \boldsymbol{\phi}]$ it requires inverting $\mathbf{g}$, which may be difficult.[^3]
- Differs from statistical [[Inference]], which is about understanding the relationship between inputs and outputs.

[^1]: [Prince, p. 18](zotero://open-pdf/library/items/BWT7FYX5?page=32&annotation=GFPBQNBM)
[^2]: [Prince, p. 17](zotero://open-pdf/library/items/BWT7FYX5?page=31&annotation=E9WW45C3); [Prince, p. 18](zotero://open-pdf/library/items/BWT7FYX5?page=32&annotation=27J47C29)
[^3]: [Prince, p. 23](zotero://open-pdf/library/items/BWT7FYX5?page=37&annotation=36X3XLPQ)
