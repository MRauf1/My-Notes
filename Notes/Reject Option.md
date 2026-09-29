---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Reject Option[^1]
> Avoid making decisions on difficult cases, in anticipation of a lower error rate on the examples that are classified: introduce a threshold $\theta$ and reject every input $\mathbf{x}$ for which
> $$
> \begin{align}
> \max_k\, p(\mathcal{C}_k | \mathbf{x}) \leq \theta
> \end{align}
> $$

# Properties
- The fraction of rejected examples is controlled by $\theta$: $\theta = 1$ rejects all examples, while with $K$ classes $\theta < 1/K$ rejects none (the largest posterior is always at least $1/K$).[^1]
- Targets the regions where classification errors arise, namely where the largest posterior is well below $1$; e.g. an automatic system classifies the unambiguous X-rays and leaves ambiguous ones to a human expert.
- Extends to minimizing expected loss, given a loss matrix, by including the loss incurred for a reject decision ([[Minimum Expected Loss Decision Rule]]).
- Requires posterior probabilities; it cannot be applied with only a [[Discriminant Function]].[^2]

[^1]: [Bishop, 2006, p. 42](zotero://open-pdf/library/items/5G99AZ8U?page=62&annotation=4I34KSXG)
[^2]: [Bishop, 2006, p. 45](zotero://open-pdf/library/items/5G99AZ8U?page=65&annotation=FRWJ6TRQ)
