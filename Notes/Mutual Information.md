---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Mutual Information[^1]
> The [[Kullback-Leibler Divergence]] between the joint distribution of $\mathbf{x}, \mathbf{y}$ and the product of their marginals, measuring how close they are to being independent:
> $$
> \begin{align}
> \mathrm{I}[\mathbf{x}, \mathbf{y}] \equiv \mathrm{KL}\big(p(\mathbf{x}, \mathbf{y}) \,\|\, p(\mathbf{x})\,p(\mathbf{y})\big) = -\iint p(\mathbf{x}, \mathbf{y}) \ln\left(\frac{p(\mathbf{x})\,p(\mathbf{y})}{p(\mathbf{x}, \mathbf{y})}\right) d\mathbf{x}\,d\mathbf{y}
> \end{align}
> $$

> [!abstract] Relation to Conditional Entropy[^1]
> $$
> \begin{align}
> \mathrm{I}[\mathbf{x}, \mathbf{y}] = \mathrm{H}[\mathbf{x}] - \mathrm{H}[\mathbf{x} | \mathbf{y}] = \mathrm{H}[\mathbf{y}] - \mathrm{H}[\mathbf{y} | \mathbf{x}]
> \end{align}
> $$

# Properties
- $\mathrm{I}[\mathbf{x}, \mathbf{y}] \geq 0$, with equality if and only if $\mathbf{x}$ and $\mathbf{y}$ are [[Independent Random Variable|independent]], inherited from the KL divergence.[^1]
- Symmetric in $\mathbf{x}$ and $\mathbf{y}$, unlike the KL divergence itself.
- The reduction in uncertainty about $\mathbf{x}$ from being told $\mathbf{y}$, or vice versa ([[Entropy]], [[Conditional Entropy]]).[^2]
- **Bayesian reading**: with $p(\mathbf{x})$ as the prior and $p(\mathbf{x} | \mathbf{y})$ as the posterior after observing data $\mathbf{y}$, mutual information is the expected reduction in uncertainty about $\mathbf{x}$ due to the new observation ([[Bayes' Theorem]]).[^2]

[^1]: [Bishop, 2006, p. 57](zotero://open-pdf/library/items/5G99AZ8U?page=77&annotation=5F4Y3GJ2)
[^2]: [Bishop, 2006, p. 58](zotero://open-pdf/library/items/5G99AZ8U?page=78&annotation=556EL5L4)
