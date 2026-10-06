---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Residual Flow (Reversible Residual Layer)[^1]
> A [[Normalizing Flow|normalizing flow]] layer inspired by [[Residual Connection|residual networks]] that splits the input $\mathbf{h} = [\mathbf{h}_1^T, \mathbf{h}_2^T]^T$ and applies two residual updates:
> $$
> \begin{align}
> \mathbf{h}_1' &= \mathbf{h}_1 + \mathbf{f}_1[\mathbf{h}_2, \boldsymbol{\phi}_1] \\
> \mathbf{h}_2' &= \mathbf{h}_2 + \mathbf{f}_2[\mathbf{h}_1', \boldsymbol{\phi}_2]
> \end{align}
> $$
> where $\mathbf{f}_1, \mathbf{f}_2$ need not be invertible. The inverse reverses the order of computation and replaces addition by subtraction:
> $$
> \begin{align}
> \mathbf{h}_2 &= \mathbf{h}_2' - \mathbf{f}_2[\mathbf{h}_1', \boldsymbol{\phi}_2] \\
> \mathbf{h}_1 &= \mathbf{h}_1' - \mathbf{f}_1[\mathbf{h}_2, \boldsymbol{\phi}_1]
> \end{align}
> $$

![[Residual Flow.png]]

> [!info] Contractive (Invertible) Residual Flow[^2]
> A residual layer $\mathbf{h}' = \mathbf{h} + \mathbf{f}[\mathbf{h}, \boldsymbol{\phi}]$ in which $\mathbf{f}$ is a [[Contraction|contraction mapping]] ([[Lipschitz Continuity|Lipschitz constant]] less than one). By the [[Banach Fixed-Point Theorem]], the inverse of a given $\mathbf{h}'$ is the unique fixed point of $\mathbf{h} \mapsto \mathbf{h}' - \mathbf{f}[\mathbf{h}, \boldsymbol{\phi}]$, reached by iterating from any $\mathbf{h}_0$:
> $$
> \begin{align}
> \mathbf{h}_{k+1} = \mathbf{h}' - \mathbf{f}[\mathbf{h}_k, \boldsymbol{\phi}]
> \end{align}
> $$

# Properties
- **Mixing**: as for [[Coupling Flow|coupling flows]], the split into blocks restricts the representable transformations, so the inputs are permuted between layers.[^1]
- **No efficient Jacobian** for the reversible form with general $\mathbf{f}_1, \mathbf{f}_2$, so it is mainly used to **save memory** when training residual networks: since the network is invertible, the activations need not be stored in the forward pass and are recomputed during backpropagation (RevNets; cf. [[Gradient Checkpointing]]).[^1]
- **Enforcing contraction**: assuming activation slopes are at most one, the Lipschitz constant is below one if the largest [[Singular Value|singular value]] of every weight matrix $\boldsymbol{\Omega}$ is below one. A crude way is clipping the magnitudes of the weights (spectral normalization is a more precise alternative).[^2][^3]
- **Log-determinant by power series**: the Jacobian determinant cannot be computed easily, but using $\log|\mathbf{A}| = \operatorname{trace}[\log \mathbf{A}]$ (from [[Trace Eigenvalue]] and [[Determinant Eigenvalue]]) and the series of $\log(\mathbf{I} + \mathbf{J})$,[^3]
$$
\begin{align}
\log\left[\left|\mathbf{I} + \frac{\partial \mathbf{f}[\mathbf{h}, \boldsymbol{\phi}]}{\partial \mathbf{h}}\right|\right] = \operatorname{trace}\left[\log\left[\mathbf{I} + \frac{\partial \mathbf{f}[\mathbf{h}, \boldsymbol{\phi}]}{\partial \mathbf{h}}\right]\right] = \sum_{k=1}^{\infty} \frac{(-1)^{k-1}}{k} \operatorname{trace}\left[\left(\frac{\partial \mathbf{f}[\mathbf{h}, \boldsymbol{\phi}]}{\partial \mathbf{h}}\right)^k\right]
\end{align}
$$
  The series converges because the contraction makes every eigenvalue of $\partial \mathbf{f} / \partial \mathbf{h}$ smaller than one in magnitude, which also makes $\mathbf{I} + \partial \mathbf{f}/\partial \mathbf{h}$ nonsingular with positive determinant. The series is truncated and each [[Trace|trace]] is approximated with [[Hutchinson's Trace Estimator]] using only vector-Jacobian products.[^4]

[^1]: [Prince, p. 314](zotero://open-pdf/library/items/BWT7FYX5?page=328&annotation=3ZYNKFI4); [Prince, p. 315](zotero://open-pdf/library/items/BWT7FYX5?page=329&annotation=RYUBCM5Z)
[^2]: [Prince, p. 315](zotero://open-pdf/library/items/BWT7FYX5?page=329&annotation=FTEWWCF7); [Prince, p. 316](zotero://open-pdf/library/items/BWT7FYX5?page=330&annotation=W5C73CL7)
[^3]: [Prince, p. 317](zotero://open-pdf/library/items/BWT7FYX5?page=331&annotation=7UL48MRD)
[^4]: [Prince, p. 317](zotero://open-pdf/library/items/BWT7FYX5?page=331&annotation=HZ8DDNJ8)
