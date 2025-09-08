---
tags: computer_science, machine_learning
---

# Definition

In [[Machine Learning]], for a given [[Set|set]] of inputs $\mathbf{x}$ and outputs $\mathbf{y}$, one wants a model with parameters $\mathbf{\phi}$. In other words, $\mathbf{y} = f(\mathbf{x}, \mathbf{\phi})$, where $f$ represents the family of functions with corresponding parameters $\mathbf{\phi}$. To pick the best set of parameters from within the family of functions, one seeks the best parameters that minimize the [[Loss Function|loss function]]: $\hat{\mathbf{\phi}} = \underset{\mathbf{\phi}}{\mathrm{\arg \min}} [L(\{\mathbf{x}, \mathbf{y}\}, \mathbf{\phi})]$.[^1]

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=32)
