---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Discriminant Function[^1][^2]
> A function $f(\mathbf{x})$ that maps each input $\mathbf{x}$ directly onto a class label, solving the inference and decision problems together. E.g. for two classes, $f$ might be binary valued with $f = 0$ representing $\mathcal{C}_1$ and $f = 1$ representing $\mathcal{C}_2$. Probabilities play no role.

# Properties
- The simplest of the [[Three Approaches to Decision Problems]]; the regression analogue is learning a regression function $y(\mathbf{x})$ directly from the training data.
- Loses access to the posteriors $p(\mathcal{C}_k | \mathbf{x})$, and with them:[^3][^4]
	- **Minimizing risk**: a change to the loss matrix requires returning to the training data and re-solving the problem, whereas posteriors allow the [[Minimum Expected Loss Decision Rule]] to be revised trivially.
	- **[[Reject Option]]**: no rejection criterion is available.
	- **Compensating for class priors**: the posterior re-weighting used after training on artificially balanced data cannot be applied.
	- **Combining models**: outputs cannot be combined via the rules of probability.
- The [[Decision Region|decision regions]] it induces are separated by [[Decision Boundary|decision boundaries]], e.g. the hyperplane of a [[Perceptron]].

[^1]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=95NCHVM8)
[^2]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=LGAAC82F)
[^3]: [Bishop, 2006, p. 44](zotero://open-pdf/library/items/5G99AZ8U?page=64&annotation=2I8ADBT8)
[^4]: [Bishop, 2006, p. 45](zotero://open-pdf/library/items/5G99AZ8U?page=65&annotation=6SKI8QAQ)
