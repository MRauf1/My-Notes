---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Linear Flow[^1]
> A [[Normalizing Flow|normalizing flow]] layer that applies an affine map
> $$
> \begin{align}
> \mathbf{f}[\mathbf{h}] = \boldsymbol{\beta} + \boldsymbol{\Omega}\mathbf{h}, \qquad \boldsymbol{\Omega} \in \mathbb{R}^{D \times D}
> \end{align}
> $$
> It is invertible iff $\boldsymbol{\Omega}$ is invertible ([[Determinant Invertible Matrix Theorem]]), and its Jacobian is $\boldsymbol{\Omega}$, so the Jacobian determinant is $|\boldsymbol{\Omega}|$.

# Types
Special forms of $\boldsymbol{\Omega}$ trade generality for efficiency:[^1]
- **General**: inverse and determinant both cost $\mathcal{O}[D^3]$, which is expensive for large $D$.
- **[[Diagonal Matrix|Diagonal]]**: inverse and determinant in $\mathcal{O}[D]$, but the elements of $\mathbf{h}$ do not interact.
- **[[Orthogonal Matrix|Orthogonal]]**: efficient to invert ($\boldsymbol{\Omega}^{-1} = \boldsymbol{\Omega}^T$) with fixed determinant $\pm 1$, but the individual dimensions cannot be scaled.
- **Triangular** ([[Lower Triangular Matrix|lower]] or [[Upper Triangular Matrix|upper]]): invertible by [[Back-Substitution|back-substitution]] in $\mathcal{O}[D^2]$, with determinant equal to the product of the diagonal entries ([[Triangular Matrix Determinant]]).
- **[[LU Decomposition|LU]]-parameterized**: general, efficient to invert, and with a cheap Jacobian, by parameterizing directly
$$
\begin{align}
\boldsymbol{\Omega} = \mathbf{P}\mathbf{L}(\mathbf{U} + \mathbf{D})
\end{align}
$$
  where $\mathbf{P}$ is a predetermined [[Permutation Matrix|permutation matrix]], $\mathbf{L}$ is lower triangular, $\mathbf{U}$ is upper triangular with zeros on the diagonal, and $\mathbf{D}$ is diagonal and supplies the missing diagonal. Inversion is $\mathcal{O}[D^2]$ and $\log|\boldsymbol{\Omega}|$ is the sum of the logs of the absolute diagonal values of $\mathbf{L}$ and $\mathbf{D}$ (see [[LUP Decomposition]], [[LDU Decomposition]]).

# Properties
- **Not expressive enough alone**: an affine map of a normal is normal ([[Multivariate Normal Distribution Affine Transformation]]); if $\mathbf{h} \sim \mathrm{Norm}_{\mathbf{h}}[\boldsymbol{\mu}, \boldsymbol{\Sigma}]$, then $\mathbf{f}[\mathbf{h}] \sim \mathrm{Norm}[\boldsymbol{\beta} + \boldsymbol{\Omega}\boldsymbol{\mu}, \boldsymbol{\Omega}\boldsymbol{\Sigma}\boldsymbol{\Omega}^T]$. Composing linear flows therefore cannot map a normal to an arbitrary density.[^1]
- Mixes the input dimensions, so it complements [[Elementwise Flow|elementwise flows]], which are nonlinear but do not mix dimensions.[^2]
- A fixed permutation between [[Coupling Flow|coupling layers]] is a linear flow with $|\det \mathbf{P}| = 1$; for images, the channel permutation is generalized to a learned invertible [[1x1 Convolution]] ([[Glow]]).[^3]

[^1]: [Prince, p. 310](zotero://open-pdf/library/items/BWT7FYX5?page=324&annotation=DTZLI65K)
[^2]: [Prince, p. 311](zotero://open-pdf/library/items/BWT7FYX5?page=325&annotation=UBA3APKL)
[^3]: [Prince, p. 312](zotero://open-pdf/library/items/BWT7FYX5?page=326&annotation=H6TW4UAA)
