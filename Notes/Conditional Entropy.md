---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Conditional Entropy[^1]
> Given a joint distribution $p(\mathbf{x}, \mathbf{y})$, if $\mathbf{x}$ is known, the additional information needed to specify $\mathbf{y}$ is $-\ln p(\mathbf{y} | \mathbf{x})$. Its average is the conditional entropy of $\mathbf{y}$ given $\mathbf{x}$:
> $$
> \begin{align}
> \mathrm{H}[\mathbf{y} | \mathbf{x}] = -\iint p(\mathbf{y}, \mathbf{x}) \ln p(\mathbf{y} | \mathbf{x})\,d\mathbf{y}\,d\mathbf{x}
> \end{align}
> $$
> (with sums in place of integrals for discrete variables).

> [!abstract] Chain Rule[^2]
> $$
> \begin{align}
> \mathrm{H}[\mathbf{x}, \mathbf{y}] = \mathrm{H}[\mathbf{y} | \mathbf{x}] + \mathrm{H}[\mathbf{x}]
> \end{align}
> $$
> The information needed to describe $\mathbf{x}$ and $\mathbf{y}$ is that needed for $\mathbf{x}$ alone plus the additional information needed for $\mathbf{y}$ given $\mathbf{x}$.

# Properties
- Follows from the product rule $p(\mathbf{x}, \mathbf{y}) = p(\mathbf{y} | \mathbf{x})\,p(\mathbf{x})$ by taking $-\ln$ and averaging.
- Conditioning never increases entropy: $\mathrm{H}[\mathbf{y} | \mathbf{x}] \leq \mathrm{H}[\mathbf{y}]$, with equality iff $\mathbf{x}$ and $\mathbf{y}$ are independent; the gap is the [[Mutual Information]].
- Defined for both discrete [[Entropy]] and [[Differential Entropy]].

[^1]: [Bishop, 2006, p. 54](zotero://open-pdf/library/items/5G99AZ8U?page=74&annotation=CXLC2Q6J)
[^2]: [Bishop, 2006, p. 55](zotero://open-pdf/library/items/5G99AZ8U?page=75&annotation=PQKCF8MX)
