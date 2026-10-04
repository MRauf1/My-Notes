---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Hyperparameter[^1]
> A variable that controls the distribution of the model parameters (or, more broadly, the model's complexity) rather than being one of the parameters themselves. E.g. the precision $\alpha$ of a Gaussian prior $p(\mathbf{w} | \alpha) = \mathcal{N}(\mathbf{w} | \mathbf{0}, \alpha^{-1}\mathbf{I})$.

# Properties
- Selected empirically by [[Hyperparameter Search]] (neural architecture search when focused on network structure).[^5]
- The choices of learning algorithm, [[Batch Size|batch size]], [[Learning Rate Schedule|learning rate schedule]], and momentum coefficients are hyperparameters of the training algorithm: they directly affect final performance but are distinct from the model parameters. Choosing them is more art than science; training many models with different hyperparameters and keeping the best is called **hyperparameter search**.[^4]
- Examples include the regularization coefficient $\lambda$ of [[Regularization]], the polynomial order $M$, and the prior and noise precisions $\alpha, \beta$; for [[L2 Regularization]] derived as MAP, $\lambda = \alpha / \beta$.
- Not fitted by maximizing the training likelihood (which would always favour maximal complexity), but set by [[Model Selection]]: a [[Validation Set]], [[Cross-Validation]], information criteria like the [[Akaike Information Criterion]], or, in a fully Bayesian treatment, by inference from the data itself.
- In neural networks, the number of layers $K$ and the number of hidden units per layer $D_1, \dots, D_K$ are hyperparameters chosen before the weights and biases are learned; for fixed hyperparameters the model is a family of functions, so the network with its hyperparameters represents a family of families of functions ([[Deep Neural Network]]).[^3]
- Searching combinations of several hyperparameters by cross-validation can require a number of training runs exponential in the number of hyperparameters.[^2]

[^1]: [Bishop, 2006, p. 30](zotero://open-pdf/library/items/5G99AZ8U?page=50&annotation=KQLPNKN2)
[^2]: [Bishop, 2006, p. 33](zotero://open-pdf/library/items/5G99AZ8U?page=53&annotation=B95CXRC2)
[^3]: [Prince, p. 46](zotero://open-pdf/library/items/BWT7FYX5?page=60&annotation=3BIZK6QZ)
[^4]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
[^5]: [Prince, p. 132](zotero://open-pdf/library/items/BWT7FYX5?page=146&annotation=2997MF4K)
