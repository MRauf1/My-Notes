---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Residual Connection (Skip Connection)[^1]
> A branch in the computational path whereby the input to a network layer $\mathrm{f}_k[\cdot, \boldsymbol{\phi}_k]$ is added back to its output, so that each layer learns an **additive change** to the current representation rather than transforming it directly. A **residual network** with four layers is
> $$
> \begin{align}
> \mathbf{h}_1 &= \mathbf{x} + \mathrm{f}_1[\mathbf{x}, \boldsymbol{\phi}_1] \\
> \mathbf{h}_2 &= \mathbf{h}_1 + \mathrm{f}_2[\mathbf{h}_1, \boldsymbol{\phi}_2] \\
> \mathbf{h}_3 &= \mathbf{h}_2 + \mathrm{f}_3[\mathbf{h}_2, \boldsymbol{\phi}_3] \\
> \mathbf{y} &= \mathbf{h}_3 + \mathrm{f}_4[\mathbf{h}_3, \boldsymbol{\phi}_4]
> \end{align}
> $$
> where the first term on each right-hand side is the residual connection. Each additive combination $\mathbf{h}_{k} = \mathbf{h}_{k-1} + \mathrm{f}_k[\mathbf{h}_{k-1}]$ is a **residual block** (or **residual layer**). Since the output is added to the input, each $\mathrm{f}_k$ must output a tensor of the same size as its input.

# Properties
- **Unraveled view**: substituting recursively writes the output as the input plus a sum of smaller networks, giving $2^K$ paths of different lengths between input and output for $K$ blocks ([[Residual Network as Ensemble]]).[^2]
- **Gradient decomposition**: the derivative of the output with respect to the first block contains an identity term plus chains of all lengths (one term per path through $\mathrm{f}_1$, here $8$ of the $16$):[^3]
$$
\begin{align}
\frac{\partial \mathbf{y}}{\partial \mathrm{f}_1} = \mathbf{I} + \frac{\partial \mathrm{f}_2}{\partial \mathrm{f}_1} + \left(\frac{\partial \mathrm{f}_3}{\partial \mathrm{f}_1} + \frac{\partial \mathrm{f}_2}{\partial \mathrm{f}_1}\frac{\partial \mathrm{f}_3}{\partial \mathrm{f}_2}\right) + \left(\frac{\partial \mathrm{f}_4}{\partial \mathrm{f}_1} + \frac{\partial \mathrm{f}_2}{\partial \mathrm{f}_1}\frac{\partial \mathrm{f}_4}{\partial \mathrm{f}_2} + \frac{\partial \mathrm{f}_3}{\partial \mathrm{f}_1}\frac{\partial \mathrm{f}_4}{\partial \mathrm{f}_3} + \frac{\partial \mathrm{f}_2}{\partial \mathrm{f}_1}\frac{\partial \mathrm{f}_3}{\partial \mathrm{f}_2}\frac{\partial \mathrm{f}_4}{\partial \mathrm{f}_3}\right)
\end{align}
$$
	- The identity term means the parameters $\boldsymbol{\phi}_1$ contribute directly to $\mathbf{y}$; since gradients through shorter paths are better behaved, residual networks suffer less from [[Shattered Gradients]]. There is always a direct path from every layer to the output, so the gradients do not [[Vanishing Gradients|vanish]] with depth.
- **Order of operations (pre-activation)**: each $\mathrm{f}_k$ must contain a nonlinearity (e.g. [[ReLU Function|ReLU]]), or the whole network is linear. If the block ends with a ReLU (the usual layer ordering), its output is non-negative and the block can only *increase* its input. Hence the activation is applied first and the block terminates with a [[Linear Layer|linear transformation]] (possibly with several layers of processing inside). Since a block starting with a ReLU does nothing to a negative input, the network typically starts with a linear transformation rather than a residual block.[^4]
- **Limited trainable depth alone**: residual connections without normalization roughly double the depth that can be practically trained, because the activation variance still explodes exponentially at initialization ([[Residual Network Variance at Initialization]]). Combined with [[Batch Normalization]], very deep networks (e.g. ResNets with $1000$ layers) can be trained.[^5]
- **Depth is not the whole story**: shallower, wider residual networks sometimes outperform deeper, narrower ones with a comparable parameter count (wide ResNets with only $16$ layers outperformed all residual networks of their time), and gradients do not propagate effectively through very long paths of the unraveled network. The current view is that residual connections add value of their own beyond enabling depth: the loss surface around a minimum is smoother and more predictable than for the same network without skip connections, which may make good, generalizing solutions easier to find.[^6]
- **Why they help** (not completely understood): reducing [[Shattered Gradients]] at the start of training, a smoother loss surface near minima, and (alternatively) eliminating singularities, i.e. places on the loss surface where the [[Hessian Matrix]] is degenerate.[^7]
- **Effect on [[L2 Regularization]]**: in a vanilla network, L2 regularization of the weights encourages a layer's output to be a constant function determined by the biases; in a residual network without BatchNorm, it encourages each residual block to compute the *identity plus a constant* determined by the biases.[^8]
- A building block of [[Deep Neural Network|deep networks]] such as residual [[Convolutional Neural Network|CNNs]] (ResNet).
- Residual connections made deep [[Graph Neural Network|graph neural networks]] trainable, countering suspended animation and [[Oversmoothing]]; in a [[Graph Convolutional Network|GCN]] the transformed, activated neighbour aggregate is summed or concatenated with the current node.[^9]

[^1]: [Prince, p. 186](zotero://open-pdf/library/items/BWT7FYX5?page=200&annotation=9UTCW7BL); [Prince, p. 189](zotero://open-pdf/library/items/BWT7FYX5?page=203&annotation=JP5SVSMG)
[^2]: [Prince, p. 189](zotero://open-pdf/library/items/BWT7FYX5?page=203&annotation=28NMNQFK)
[^3]: [Prince, p. 191](zotero://open-pdf/library/items/BWT7FYX5?page=205&annotation=3Z4ZT9ZY)
[^4]: [Prince, p. 191](zotero://open-pdf/library/items/BWT7FYX5?page=205&annotation=F6CKE9TE); [Prince, p. 191](zotero://open-pdf/library/items/BWT7FYX5?page=205&annotation=J2HGQR7L)
[^5]: [Prince, p. 186](zotero://open-pdf/library/items/BWT7FYX5?page=200&annotation=RS4M62RZ); [Prince, p. 192](zotero://open-pdf/library/items/BWT7FYX5?page=206&annotation=HAGEA9BV); [Prince, p. 199](zotero://open-pdf/library/items/BWT7FYX5?page=213&annotation=R92DRVX3)
[^6]: [Prince, p. 199](zotero://open-pdf/library/items/BWT7FYX5?page=213&annotation=R92DRVX3)
[^7]: [Prince, p. 202](zotero://open-pdf/library/items/BWT7FYX5?page=216&annotation=8HUWG2BB)
[^8]: [Prince, p. 202](zotero://open-pdf/library/items/BWT7FYX5?page=216&annotation=GRAWBTGS)
[^9]: [Prince, p. 257](zotero://open-pdf/library/items/BWT7FYX5?page=271&annotation=RPGSV7IR); [Prince, p. 266](zotero://open-pdf/library/items/BWT7FYX5?page=280&annotation=X2CIB63G)
