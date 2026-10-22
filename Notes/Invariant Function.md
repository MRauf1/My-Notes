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

More generally, for a [[Group]] $G$ [[Group Action|acting]] on the input space, $f$ is $G$-invariant if $f(g \cdot \mathbf{x}) = f(\mathbf{x})$ for all $g \in G$; invariance is the special case of [[Equivariant Function|equivariance]] in which $G$ acts trivially on the output.[^2]

**Invariance as a fixed point; relation to equivariance.**[^2] Invariance always means "fixed point of some [[Group Action|action]]". The condition $f(g \cdot \mathbf{x}) = f(\mathbf{x})$ above can be read in two ways:
- *As a map:* $f$ is [[Equivariant Function|equivariant]] with the trivial action on the output.
- *As a point:* $f$ is a fixed point of the induced action $f \mapsto f \circ g^{-1}$ on the space of functions.

One level up, a map $F: X \to Y$ is a point of $\mathrm{Map}(X, Y)$, where $G$ acts by conjugation $(g \cdot F)(x) = \rho_{\text{out}}(g)\,F(\rho_{\text{in}}(g)^{-1}x)$; $F$ is invariant under this action if and only if it is equivariant. Hence an "invariant operator" in PDE or signal processing (e.g. $T_g \Delta T_g^{-1} = \Delta$ for the [[Laplacian Operator]], [[Laplacian Operator Rigid Motion Invariance]]) is an equivariant map, not one satisfying $L(T_g f) = L f$. The latter is equivariance with a trivial output action, a different and much stronger condition. The word changes with the level at which the object is viewed (point vs. map), not with whether it is a "function" or an "operator", and each claim needs its action specified.

# Properties
- Image classification networks should be invariant to geometric transformations (translation, rotation, flipping, warping): the same object should be identified regardless.[^1]
- In [[Convolutional Neural Network|CNNs]], partial translation invariance is induced by [[Max Pooling|pooling]] on top of equivariant [[Convolutional Layer|convolutional layers]]; it can also be learned from data via [[Data Augmentation]].
- Composing an equivariant map with an invariant one yields an invariant map: if $f$ is equivariant and $g$ invariant, $g[f[t[\mathbf{x}]]] = g[t[f[\mathbf{x}]]] = g[f[\mathbf{x}]]$.[^2]
- Graph-level outputs of a [[Graph Neural Network]] are invariant to node permutations: equivariant layers followed by [[Average Pooling|mean pooling]] $\mathbf{H}_K\mathbf{1}/N$, since $\mathbf{P}\mathbf{1} = \mathbf{1}$.[^3]

[^1]: [Prince, p. 162](zotero://open-pdf/library/items/BWT7FYX5?page=176&annotation=S3G56EUB)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=PPRKSFIE)
