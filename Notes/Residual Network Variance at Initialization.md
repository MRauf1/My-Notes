---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Residual Network Variance at Initialization[^1]
> In a [[Residual Connection|residual network]] with [[ReLU Function|ReLU]] activations and [[He Initialization]], each residual block preserves the expected [[Variance|variance]] of its input, and its output is (approximately) uncorrelated with the input. Since the block's output is added back to its input,
> $$
> \begin{align}
> \mathrm{Var}[\mathbf{h}_k] = \mathrm{Var}[\mathbf{h}_{k-1}] + \mathrm{Var}\big[\mathrm{f}_k[\mathbf{h}_{k-1}]\big] = 2\,\mathrm{Var}[\mathbf{h}_{k-1}] \quad\Longrightarrow\quad \mathrm{Var}[\mathbf{h}_K] = 2^K\,\mathrm{Var}[\mathbf{h}_0]
> \end{align}
> $$
> i.e. the activation variance grows exponentially with the number of blocks; a similar argument applies to the gradients in the backward pass of [[Backpropagation]].

# Properties
- Limits the possible depth before [[Floating-Point Number System|floating-point]] precision is exceeded in the forward pass; residual networks thus still suffer from unstable forward propagation and [[Exploding Gradients|exploding gradients]] even with He initialization.[^1]
- **Fix 1 (rescaling)**: multiply the combined output of each block by $1/\sqrt{2}$ to compensate for the doubling, keeping the variance constant.[^2]
- **Fix 2 ([[Batch Normalization]], the usual choice)**: apply BN as the first step of each block with offset $\delta = 0$ and scale $\gamma = 1$. The block input then has unit variance, and with He initialization so does the block output, so
$$
\begin{align}
\mathrm{Var}[\mathbf{h}_k] = \mathrm{Var}[\mathbf{h}_{k-1}] + 1
\end{align}
$$
grows only **linearly** (the $k$-th block adds one unit of variance to an existing variance of $\approx k$).[^3]
	- Side-effect: at initialization, later blocks contribute relatively less to the overall variation and are dominated by the residual connection, so they are close to computing the identity. The network is effectively shallower at the start of training and can control its own **effective depth** by increasing the scales $\gamma$ of later layers.[^4]

[^1]: [Prince, p. 192](zotero://open-pdf/library/items/BWT7FYX5?page=206&annotation=2UWTBVRL); [Prince, p. 192](zotero://open-pdf/library/items/BWT7FYX5?page=206&annotation=VLLI2DAA)
[^2]: [Prince, p. 192](zotero://open-pdf/library/items/BWT7FYX5?page=206&annotation=UZQAV5GA)
[^3]: [Prince, p. 193](zotero://open-pdf/library/items/BWT7FYX5?page=207&annotation=ISKCA6FM)
[^4]: [Prince, p. 194](zotero://open-pdf/library/items/BWT7FYX5?page=208&annotation=82VD6Y8W)
