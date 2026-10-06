---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Coupling Flow[^1]
> A [[Normalizing Flow|normalizing flow]] layer that splits the input $\mathbf{h} = [\mathbf{h}_1^T, \mathbf{h}_2^T]^T$, copies the first part, and transforms the second part with parameters computed from the first:
> $$
> \begin{align}
> \mathbf{h}_1' &= \mathbf{h}_1 \\
> \mathbf{h}_2' &= \mathbf{g}\left[\mathbf{h}_2, \boldsymbol{\phi}[\mathbf{h}_1]\right]
> \end{align}
> $$
> where $\mathbf{g}[\bullet, \boldsymbol{\phi}]$ is an [[Elementwise Flow|elementwise flow]] (or other invertible layer) and $\boldsymbol{\phi}[\bullet]$ is an arbitrary, usually neural, function that need not be invertible. The inverse is
> $$
> \begin{align}
> \mathbf{h}_1 &= \mathbf{h}_1' \\
> \mathbf{h}_2 &= \mathbf{g}^{-1}\left[\mathbf{h}_2', \boldsymbol{\phi}[\mathbf{h}_1]\right]
> \end{align}
> $$

![[Coupling Flow.png]]

# Properties
- **Triangular Jacobian**: if $\mathbf{g}$ is elementwise, the [[Jacobian Matrix]] is [[Lower Triangular Matrix|lower triangular]],
$$
\begin{align}
\frac{\partial \mathbf{h}'}{\partial \mathbf{h}} = \begin{bmatrix} \mathbf{I} & \mathbf{0} \\ \dfrac{\partial \mathbf{h}_2'}{\partial \mathbf{h}_1} & \operatorname{diag}\left[\dfrac{\partial \mathbf{g}}{\partial \mathbf{h}_2}\right] \end{bmatrix}
\end{align}
$$
  so its determinant is the product of the elementwise derivatives ([[Triangular Matrix Determinant]]); the possibly complicated block $\partial \mathbf{h}_2' / \partial \mathbf{h}_1$ never needs to be computed.[^1]
- Both the inverse and the Jacobian determinant are efficient, and both directions are a single parallel pass.[^1]
- **Mixing via permutations**: a single layer only transforms the second half in a way that depends on the first. Between layers, the elements are shuffled with [[Permutation Matrix|permutation matrices]] so every variable is ultimately transformed by every other. These are hard to learn, so they are initialized randomly and frozen. For images, the channels are split into halves and permuted between layers with [[1x1 Convolution|1×1 convolutions]] ([[Glow]]).[^1]
- The special case of a [[Autoregressive Flow|autoregressive flow]] with two blocks.[^2]
- An additive transformer $\mathbf{g}[\mathbf{h}_2, \boldsymbol{\phi}] = \mathbf{h}_2 + \boldsymbol{\phi}$ gives a volume-preserving layer (NICE); an affine one $\mathbf{g} = \mathbf{h}_2 \odot \exp[\mathbf{s}] + \mathbf{t}$ gives RealNVP.

[^1]: [Prince, p. 311](zotero://open-pdf/library/items/BWT7FYX5?page=325&annotation=AZ5J9TUN); [Prince, p. 312](zotero://open-pdf/library/items/BWT7FYX5?page=326&annotation=H6TW4UAA)
[^2]: [Prince, p. 313](zotero://open-pdf/library/items/BWT7FYX5?page=327&annotation=RX38FBNQ)
