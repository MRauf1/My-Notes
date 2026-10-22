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

More generally, for a [[Group]] $G$ [[Group Action|acting]] on the input space by $\rho_{\text{in}}$ and on the output space by $\rho_{\text{out}}$, $f$ is $G$-equivariant if $f(\rho_{\text{in}}(g)\mathbf{x}) = \rho_{\text{out}}(g) f(\mathbf{x})$ for all $g \in G$; [[Invariant Function|invariance]] is the case $\rho_{\text{out}}(g) = \mathrm{id}$.[^2]

**Equivariance of a map = invariance of a point in the space of maps.**[^2] Invariance always means "fixed point of some action", while equivariance is a property of a map checked on its inputs and outputs. The two meet because a map is also a point of $\mathrm{Map}(X, Y)$, on which $G$ acts by the induced conjugation [[Group Action|action]]:
$$
\begin{align}
(g \cdot F)(x) = \rho_{\text{out}}(g)\, F\big(\rho_{\text{in}}(g)^{-1} x\big).
\end{align}
$$
Then $g \cdot F = F$ for all $g$ if and only if $F$ is equivariant: substituting $x = \rho_{\text{in}}(g)\,x'$ turns $\rho_{\text{out}}(g)F(\rho_{\text{in}}(g)^{-1}x) = F(x)$ into $\rho_{\text{out}}(g)F(x') = F(\rho_{\text{in}}(g)x')$. So "equivariant map" and "invariant point of the map space" are one condition seen at two levels, not a distinction between functions and operators. Which word is used depends on whether $F$ is examined by evaluating it (equivariant) or treated as a single object that a transformation might move (invariant). Every "invariant/equivariant" claim is meaningful only once the action on each space is specified.
- *Operators:* for $L$ acting on functions with $(T_g f)(\mathbf{x}) = f(g^{-1}\mathbf{x})$, the induced action is $L \mapsto T_g L T_g^{-1}$. "$L$ is invariant" (PDE and physics: the law does not change under a change of frame; signal processing: [[Shift-Invariant System]]) means exactly "$L$ is equivariant", $L T_g = T_g L$, e.g. the [[Laplacian Operator]].
- *Scalar fields:* for $u: \mathbb{R}^n \to \mathbb{R}$ with $G$ acting trivially on $\mathbb{R}$, the induced action is $u \mapsto u \circ g^{-1} = T_g u$, so "$u$ is invariant as a point of the function space" ($T_g u = u$) means "$u$ is equivariant with trivial output action", which is an [[Invariant Function]].
- The levels nest: each $u$ is a map on $\mathbb{R}^n$ and a point of the function space; $\Delta$ is a map on the function space and a point of the operator space.

# Properties
- Per-pixel image segmentation networks should be equivariant: if the image is translated, rotated, or flipped, the returned segmentation should be transformed in the same way.[^1]
- [[Convolutional Layer|Convolutional layers]] are equivariant to translation (strictly, to translations by multiples of the stride and away from boundary effects).[^3]
- A linear operator is translation-equivariant if and only if it is a convolution; this is the [[Shift-Invariant System]] of signal processing (its "shift-invariant" is deep learning's "shift-equivariant").[^2]
- Compositions of equivariant maps are equivariant, so a stack of convolutional layers with pointwise [[Activation Layer|activations]] is translation-equivariant.[^2]
- The [[Laplacian Operator]] is equivariant to rigid motions, $\Delta(f\circ g) = (\Delta f)\circ g$; PDE texts call this "invariance" of the operator, meaning invariance under conjugation $T_g \Delta T_g^{-1} = \Delta$ ([[Laplacian Operator Rigid Motion Invariance]]).[^2]
- [[Self-Attention]] is equivariant to permutations of its inputs, so word order must be supplied by a [[Positional Encoding]].[^4]
- Layers of a [[Graph Neural Network]] must be equivariant to permutations of the node indices: $\mathbf{H}_{k+1}\mathbf{P} = \mathbf{F}[\mathbf{H}_k\mathbf{P}, \mathbf{P}^T\mathbf{A}\mathbf{P}, \boldsymbol{\phi}_k]$, as are node-level and edge-level outputs.[^5]

[^1]: [Prince, p. 162](zotero://open-pdf/library/items/BWT7FYX5?page=176&annotation=Z6JPWHMF)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 163](zotero://open-pdf/library/items/BWT7FYX5?page=177&annotation=CDIV2Z4I); [Prince, p. 163](zotero://open-pdf/library/items/BWT7FYX5?page=177&annotation=6LPDNNE6)
[^4]: [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=QUSJZKJ7)
[^5]: [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=FQRNJX4J)
