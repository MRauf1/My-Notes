---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Invariant Function[^1]
> A function $f[\mathbf{x}]$ of an image $\mathbf{x}$ is **invariant** to a transformation $t[\mathbf{x}]$ if
> $$
> \begin{align}
> f[t[\mathbf{x}]] = f[\mathbf{x}]
> \end{align}
> $$
> i.e. the output is the same regardless of the transformation.

More generally, for a [[Group]] $G$ acting on the input space, $f$ is $G$-invariant if $f(g \cdot \mathbf{x}) = f(\mathbf{x})$ for all $g \in G$; invariance is the special case of [[Equivariant Function|equivariance]] in which $G$ acts trivially on the output.[^2]

# Properties
- Image classification networks should be invariant to geometric transformations (translation, rotation, flipping, warping): the same object should be identified regardless.[^1]
- In [[Convolutional Neural Network|CNNs]], partial translation invariance is induced by [[Max Pooling|pooling]] on top of equivariant [[Convolutional Layer|convolutional layers]]; it can also be learned from data via [[Data Augmentation]].
- Composing an equivariant map with an invariant one yields an invariant map: if $f$ is equivariant and $g$ invariant, $g[f[t[\mathbf{x}]]] = g[t[f[\mathbf{x}]]] = g[f[\mathbf{x}]]$.[^2]
- Graph-level outputs of a [[Graph Neural Network]] are invariant to node permutations: equivariant layers followed by [[Average Pooling|mean pooling]] $\mathbf{H}_K\mathbf{1}/N$, since $\mathbf{P}\mathbf{1} = \mathbf{1}$.[^3]

[^1]: [Prince, p. 162](zotero://open-pdf/library/items/BWT7FYX5?page=176&annotation=S3G56EUB)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=PPRKSFIE)
