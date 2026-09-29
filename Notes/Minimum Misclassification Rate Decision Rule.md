---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!abstract] Minimum Misclassification Rate Decision Rule[^1][^2]
> The probability of making a mistake is minimized by assigning each $\mathbf{x}$ to the class with the largest posterior probability $p(\mathcal{C}_k | \mathbf{x})$.
>
> For two classes, a mistake has probability
> $$
> \begin{align}
> p(\text{mistake}) = p(\mathbf{x} \in \mathcal{R}_1, \mathcal{C}_2) + p(\mathbf{x} \in \mathcal{R}_2, \mathcal{C}_1) = \int_{\mathcal{R}_1} p(\mathbf{x}, \mathcal{C}_2)\,d\mathbf{x} + \int_{\mathcal{R}_2} p(\mathbf{x}, \mathcal{C}_1)\,d\mathbf{x}
> \end{align}
> $$
> For $K$ classes, it is easier to maximize the probability of being correct,
> $$
> \begin{align}
> p(\text{correct}) = \sum_{k=1}^K p(\mathbf{x} \in \mathcal{R}_k, \mathcal{C}_k) = \sum_{k=1}^K \int_{\mathcal{R}_k} p(\mathbf{x}, \mathcal{C}_k)\,d\mathbf{x}
> \end{align}
> $$

**Why the posterior.** Each $\mathbf{x}$ can be placed in any [[Decision Region|decision region]] independently, so the integrals are optimized pointwise by assigning $\mathbf{x}$ to the class with the largest joint $p(\mathbf{x}, \mathcal{C}_k)$. By the product rule $p(\mathbf{x}, \mathcal{C}_k) = p(\mathcal{C}_k | \mathbf{x})\,p(\mathbf{x})$, and $p(\mathbf{x})$ is common to all classes, so this is the class with the largest posterior.

# Properties
- The special case of the [[Minimum Expected Loss Decision Rule]] with 0-1 loss $L_{kj} = 1 - I_{kj}$.
- Errors come from regions where the largest posterior is significantly less than $1$, i.e. where the joints $p(\mathbf{x}, \mathcal{C}_k)$ have comparable values, motivating the [[Reject Option]].
- The posteriors are obtained from class-conditional densities and priors via [[Bayes' Theorem]]; the [[Naive Bayes Classifier]] applies this rule under a conditional independence assumption.

[^1]: [Bishop, 2006, p. 39](zotero://open-pdf/library/items/5G99AZ8U?page=59&annotation=TCBWEFIC)
[^2]: [Bishop, 2006, p. 40](zotero://open-pdf/library/items/5G99AZ8U?page=60&annotation=QR4AM7LI)
