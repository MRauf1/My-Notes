---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Equivariant Function[^1]
> A function $f[\mathbf{x}]$ of an image $\mathbf{x}$ is **equivariant** (or **covariant**) to a transformation $t[\mathbf{x}]$ if
> $$
> \begin{align}
> f[t[\mathbf{x}]] = t[f[\mathbf{x}]]
> \end{align}
> $$
> i.e. its output changes in the same way under the transformation as the input.

More generally, for a [[Group]] $G$ acting on the input space by $\rho_{\text{in}}$ and on the output space by $\rho_{\text{out}}$, $f$ is $G$-equivariant if $f(\rho_{\text{in}}(g)\mathbf{x}) = \rho_{\text{out}}(g) f(\mathbf{x})$ for all $g \in G$; [[Invariant Function|invariance]] is the case $\rho_{\text{out}}(g) = \mathrm{id}$.[^2]

# Properties
- Per-pixel image segmentation networks should be equivariant: if the image is translated, rotated, or flipped, the returned segmentation should be transformed in the same way.[^1]
- [[Convolutional Layer|Convolutional layers]] are equivariant to translation (strictly, to translations by multiples of the stride and away from boundary effects).[^3]
- A linear operator is translation-equivariant if and only if it is a convolution; this is the [[Shift-Invariant System]] of signal processing (its "shift-invariant" is deep learning's "shift-equivariant").[^2]
- Compositions of equivariant maps are equivariant, so a stack of convolutional layers with pointwise [[Activation Layer|activations]] is translation-equivariant.[^2]
- [[Self-Attention]] is equivariant to permutations of its inputs, so word order must be supplied by a [[Positional Encoding]].[^4]
- Layers of a [[Graph Neural Network]] must be equivariant to permutations of the node indices: $\mathbf{H}_{k+1}\mathbf{P} = \mathbf{F}[\mathbf{H}_k\mathbf{P}, \mathbf{P}^T\mathbf{A}\mathbf{P}, \boldsymbol{\phi}_k]$, as are node-level and edge-level outputs.[^5]

[^1]: [Prince, p. 162](zotero://open-pdf/library/items/BWT7FYX5?page=176&annotation=Z6JPWHMF)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 163](zotero://open-pdf/library/items/BWT7FYX5?page=177&annotation=CDIV2Z4I); [Prince, p. 163](zotero://open-pdf/library/items/BWT7FYX5?page=177&annotation=6LPDNNE6)
[^4]: [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=QUSJZKJ7)
[^5]: [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=FQRNJX4J)
