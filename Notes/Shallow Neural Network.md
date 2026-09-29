---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Shallow Neural Network[^1]
> A neural network $\mathbf{y} = \mathbf{f}[\mathbf{x}, \boldsymbol{\phi}]$ with a single hidden layer, mapping $\mathbf{x} \in \mathbb{R}^{D_i}$ to $\mathbf{y} \in \mathbb{R}^{D_o}$ through $D$ hidden units
> $$
> \begin{align}
> h_d &= a\left[\theta_{d0} + \sum_{i=1}^{D_i} \theta_{di} x_i\right], \quad d = 1, \dots, D \\
> y_j &= \phi_{j0} + \sum_{d=1}^{D} \phi_{jd} h_d, \quad j = 1, \dots, D_o
> \end{align}
> $$
> where $a[\bullet]$ is a nonlinear [[Activation Layer|activation function]] and $\boldsymbol{\phi} = \{\theta_{\bullet\bullet}, \phi_{\bullet\bullet}\}$ are the parameters.

# Properties
- Has $D(D_i + 1) + D_o(D + 1)$ parameters; for $D_i = D_o = 1$ this is $3D + 1$.[^2]
- With [[ReLU Function|ReLU]] activations, each hidden unit computes a linear function of the input that is clipped below zero; the clipped functions are weighted and summed, and the offset $\phi_{j0}$ sets the overall height. The output is a continuous piecewise linear function of the input ([[Linear Regions of ReLU Network]]).[^3]
	- For $D_i = 1$, each hidden unit contributes one "joint" where its line crosses zero, so the output has at most $D$ joints and $D + 1$ linear regions. Only $D$ of the $D+1$ slopes are independent: the remaining one is zero (all units inactive) or a sum of the others' slopes.
	- For $D_i = 2$, each unit is an oriented plane clipped at zero, and the output is a continuous piecewise linear surface of convex polygonal regions; for $D_i > 2$ the regions are convex polytopes.[^4]
- The number of hidden units $D$ is a measure of the network's [[Model Capacity|capacity]]; adding hidden units adds linear regions, each covering a smaller section of the target function that is better approximated by a line, which is the intuition behind the [[Universal Approximation Theorem]].[^2]
- For some functions the required number of hidden units is impractically large; a [[Deep Neural Network]] can produce many more linear regions for the same number of parameters ([[Depth Separation]]).[^5]
- A [[Multilayer Perceptron]] with one hidden layer; the name contrasts with a [[Deep Neural Network]], which has multiple hidden layers.[^6]

[^1]: [Prince, p. 25](zotero://open-pdf/library/items/BWT7FYX5?page=39&annotation=8CHKW5RA); [Prince, p. 33](zotero://open-pdf/library/items/BWT7FYX5?page=47&annotation=QJHEDUX9); [Prince, p. 35](zotero://open-pdf/library/items/BWT7FYX5?page=49&annotation=UZPZIFFU)
[^2]: [Prince, p. 29](zotero://open-pdf/library/items/BWT7FYX5?page=43&annotation=IRUAYRI5); [Prince, p. 29](zotero://open-pdf/library/items/BWT7FYX5?page=43&annotation=5KHBND28); [Prince, p. 50](zotero://open-pdf/library/items/BWT7FYX5?page=64&annotation=C9SH66XE)
[^3]: [Prince, p. 27](zotero://open-pdf/library/items/BWT7FYX5?page=41&annotation=JHA8UETU); [Prince, p. 27](zotero://open-pdf/library/items/BWT7FYX5?page=41&annotation=X2XCZJXY)
[^4]: [Prince, p. 33](zotero://open-pdf/library/items/BWT7FYX5?page=47&annotation=8JSUFIFE); [Prince, p. 33](zotero://open-pdf/library/items/BWT7FYX5?page=47&annotation=TKVQ7XJS)
[^5]: [Prince, p. 41](zotero://open-pdf/library/items/BWT7FYX5?page=55&annotation=6XB2G7AV)
[^6]: [Prince, p. 35](zotero://open-pdf/library/items/BWT7FYX5?page=49&annotation=LV3HF7ZK)
