---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Discriminative Model[^1]
> An approach that directly models the posterior class probabilities $p(\mathcal{C}_k | \mathbf{x})$ (or, for regression, the conditional density $p(t | \mathbf{x})$), then uses [[Decision Theory|decision theory]] to assign each new $\mathbf{x}$ to a class.

# Properties
- Contrasts with a [[Generative Model]], which models the distribution of the inputs as well, $p(\mathbf{x}, \mathcal{C}_k)$ or $p(\mathbf{x} | \mathcal{C}_k)\,p(\mathcal{C}_k)$.
- Less demanding of data and computation when only decisions are needed, since class-conditional densities may contain much structure with little effect on the posteriors.[^2]
- Cannot provide the marginal $p(\mathbf{x})$, so it does not support [[Novelty Detection|novelty detection]].
- Unlike a [[Discriminant Function]], it retains the posteriors, supporting the [[Reject Option]], revision of the loss matrix, compensation for class priors, and combination of models.
- E.g. [[Logistic Regression]]. The relative merits of generative and discriminative approaches, and ways to combine them, remain an active topic.

[^1]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=8IPZ2JC6)
[^2]: [Bishop, 2006, p. 44](zotero://open-pdf/library/items/5G99AZ8U?page=64&annotation=FNCQYKUP)
