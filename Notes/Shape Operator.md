---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Shape Operator[^1]
> The shape operator of a [[Smooth Surface]] $f: M \rightarrow \mathbb{R}^3$ with [[Gauss Map]] $N$ is the unique linear map $S: TM \rightarrow TM$ satisfying
> $$\begin{align}
> df(SX) = -dN(X) \quad \text{for all tangent vectors } X.
> \end{align}$$
> This is O'Neill's $S_p(\mathbf{v}) = -\nabla_{\mathbf{v}} U$ (O'Neill writes $U$ for the unit normal), expressed on the parameter domain $M$.

The shape operator and the [[Weingarten Map]] $dN$ express the same idea, how the normal changes along $X$, but $S$ records the change as a tangent vector on $M$, while $dN$ records it as a tangent vector in $\mathbb{R}^3$. Keeping them distinct makes the dependence on the immersion $f$ explicit, which matters when computing.[^1]

$S$ is always well defined because $N$ is a unit vector: it cannot grow or shrink in the normal direction, so $dN(X)$ is tangent and lies in the image of $df$.[^1]

> [!abstract] Matrix Representation[^2]
> With $\mathrm{I}$ the matrix of the [[Induced Metric]] and $\mathrm{II}$ that of the [[Second Fundamental Form]], $\mathrm{II} = \mathrm{I}S$, i.e. $S = \mathrm{I}^{-1}\mathrm{II}$.

**Sign convention (O'Neill).** The minus sign makes $S(X)\cdot X > 0$ when the surface bends *toward* $N$. E.g. a sphere of radius $r$ with outward normal has $S = -\frac{1}{r}\mathrm{Id}$. Crane instead writes $df(SX) = dN(X)$ (no minus), which flips the sign of $S$, the principal curvatures, $H$ and $\mathrm{II}$ (but not $K$).

# Properties
- [[Self-Adjoint Linear Map|Self-adjoint]] with respect to the [[Induced Metric]]: $g(SX, Y) = g(X, SY)$.[^2]
- Eigenvectors/eigenvalues are the principal directions/[[Principal Curvature|principal curvatures]]: $SX_i = \kappa_iX_i$.
- [[Gaussian Curvature]] $K = \det S$, [[Mean Curvature]] $H = \tfrac{1}{2}\operatorname{tr} S$.
- [[Normal Curvature]] is its Rayleigh quotient: $\kappa_n(X) = \frac{g(SX,X)}{g(X,X)}$.
- $S$ is a linear operator, so its matrix transforms as $S \mapsto PSP^{-1}$, unlike $\mathrm{I}$ and $\mathrm{II}$ ([[Bilinear Form]]).

[^1]: [Crane, p. 39](zotero://open-pdf/library/items/9N6JDPI2?page=40&annotation=LMULAKA2)
[^2]: [Crane, p. 44](zotero://open-pdf/library/items/9N6JDPI2?page=45&annotation=WNXWD9B4)
