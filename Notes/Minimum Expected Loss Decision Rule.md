---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Loss Matrix[^1]
> If the true class of $\mathbf{x}$ is $\mathcal{C}_k$ and we assign it to $\mathcal{C}_j$ ($j$ may or may not equal $k$), we incur a loss $L_{kj}$, the $(k, j)$ element of a loss matrix. A utility function is equivalent, taking utility to be the negative of the loss.

> [!abstract] Minimum Expected Loss Decision Rule[^2][^3]
> Since the true class is unknown, minimize the average loss with respect to $p(\mathbf{x}, \mathcal{C}_k)$:
> $$
> \begin{align}
> \mathbb{E}[L] = \sum_k \sum_j \int_{\mathcal{R}_j} L_{kj}\, p(\mathbf{x}, \mathcal{C}_k)\,d\mathbf{x}
> \end{align}
> $$
> This is minimized by assigning each new $\mathbf{x}$ to the class $j$ for which
> $$
> \begin{align}
> \sum_k L_{kj}\, p(\mathcal{C}_k | \mathbf{x})
> \end{align}
> $$
> is a minimum.

Each $\mathbf{x}$ is assigned independently, so the choice of [[Decision Region|decision regions]] minimizes $\sum_k L_{kj}\,p(\mathbf{x}, \mathcal{C}_k)$ pointwise, and the common factor $p(\mathbf{x})$ cancels via the product rule.

# Properties
- Trivial to apply once the posterior class probabilities are known; this is why the decision stage is simple compared with the inference stage ([[Three Approaches to Decision Problems]]).
- 0-1 loss recovers the [[Minimum Misclassification Rate Decision Rule]]; asymmetric losses (e.g. a missed cancer diagnosis costing far more than a false alarm) shift the decision boundaries toward the less costly error.
- If the loss matrix is revised, the posteriors let the rule be updated trivially, whereas a [[Discriminant Function]] would have to be retrained.
- Extends to the [[Reject Option]] by assigning a loss to the reject decision.
- The [[Loss Function|loss]] convention mirrors [[Expected Utility]] maximization in [[Decision Theory]].

[^1]: [Bishop, 2006, p. 41](zotero://open-pdf/library/items/5G99AZ8U?page=61&annotation=26LZ9D5F)
[^2]: [Bishop, 2006, p. 41](zotero://open-pdf/library/items/5G99AZ8U?page=61&annotation=EMHMNFII)
[^3]: [Bishop, 2006, p. 42](zotero://open-pdf/library/items/5G99AZ8U?page=62&annotation=GC9PAVZ5)
