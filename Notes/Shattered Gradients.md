---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Shattered Gradients[^1]
> The phenomenon in which, for a deep network, a tiny change in the input (or in the parameters of early layers) produces a completely different gradient. It is measured by the autocorrelation function of the gradient: for shallow networks nearby gradients are correlated, but for deep networks this correlation quickly drops to zero.

# Properties
- **Conjectured cause of poor trainability of deep networks**: even with a good [[Weight Initialization|initialization]] (no [[Exploding Gradients|exploding]] or [[Vanishing Gradients|vanishing gradients]]), the gradient is only valid for an infinitesimal change, whereas optimization uses a finite step size. Any reasonable step may land where the gradient is completely different and unrelated, so the loss surface looks like an enormous range of tiny mountains rather than a single smooth structure, and [[Gradient Descent]] fails to make progress.[^2]
- **Mechanism**: for a sequential network $\mathbf{y} = \mathrm{f}_4[\mathrm{f}_3[\mathrm{f}_2[\mathrm{f}_1[\mathbf{x}]]]]$, by the chain rule
$$
\begin{align}
\frac{\partial \mathbf{y}}{\partial \mathrm{f}_1} = \frac{\partial \mathrm{f}_2}{\partial \mathrm{f}_1}\frac{\partial \mathrm{f}_3}{\partial \mathrm{f}_2}\frac{\partial \mathrm{f}_4}{\partial \mathrm{f}_3}
\end{align}
$$
When the parameters of $\mathrm{f}_1$ change, every factor is evaluated at a slightly different location (since $\mathrm{f}_2, \mathrm{f}_3, \mathrm{f}_4$ are computed from $\mathrm{f}_1$), so the updated gradient may be completely different, and more so the deeper the network.[^3]
- **Mitigations**:
	- [[Residual Connection|Residual connections]] add an identity term and short chains of derivatives to each layer's gradient, which are better behaved.[^4]
	- [[Batch Normalization]] makes the loss surface and its gradient change more smoothly, allowing higher [[Learning Rate|learning rates]].[^5]

[^1]: [Prince, p. 187](zotero://open-pdf/library/items/BWT7FYX5?page=201&annotation=PV8Y676E)
[^2]: [Prince, p. 187](zotero://open-pdf/library/items/BWT7FYX5?page=201&annotation=UQJWJL9R)
[^3]: [Prince, p. 189](zotero://open-pdf/library/items/BWT7FYX5?page=203&annotation=UJQ5BV57)
[^4]: [Prince, p. 191](zotero://open-pdf/library/items/BWT7FYX5?page=205&annotation=3Z4ZT9ZY)
[^5]: [Prince, p. 194](zotero://open-pdf/library/items/BWT7FYX5?page=208&annotation=QXYSXZTD)
