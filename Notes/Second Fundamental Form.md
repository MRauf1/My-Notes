---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Second Fundamental Form[^1]
> The second fundamental form of a [[Smooth Surface]] is the symmetric [[Bilinear Form]]
> $$\begin{align}
> \mathrm{II}(X, Y) := g(SX, Y) = -dN(X) \cdot df(Y),
> \end{align}$$
> built from the [[Shape Operator]] $S$ (O'Neill convention $df(SX) = -dN(X)$) and [[Induced Metric]] $g$. For tangent vectors in $\mathbb{R}^3$ this is O'Neill's $\mathrm{II}(\mathbf{v}, \mathbf{w}) = S(\mathbf{v}) \cdot \mathbf{w}$.[^2]

Like the [[First Fundamental Form]], it introduces no new geometric idea: it is a repackaging of $g$ and $S$, themselves functions of the two truly fundamental objects $f$ and $N$.[^1]

> [!abstract] Matrix Representation[^2][^3]
> $$\begin{align}
> \mathrm{II} = \mathrm{I}S = \begin{bmatrix} l & m \\ m & n \end{bmatrix}, \quad l = N \cdot f_{xx},\ m = N \cdot f_{xy},\ n = N \cdot f_{yy},
> \end{align}$$
> where $f_{xy}$ is the second partial derivative of the immersion. (O'Neill's $l, m, n$; Crane and other classical texts write $e, f, g$.)

Geometrically, $\mathrm{II}$ is the normal component of the second derivative of $f$: since $N \cdot f_x = 0$, differentiating gives $l = N \cdot f_{xx} = -N_x \cdot f_x = S(f_x) \cdot f_x$, which is the $-dN \cdot df$ form above.

**Transformation.** $\mathrm{I}S$ is a product of a bilinear form and a linear map, but since it represents a bilinear form it transforms as $\mathrm{I}S \mapsto P^{-T}\mathrm{I}SP^{-1}$. One cannot read this off the matrices alone; one must remember what they represent.[^4]

# Properties
- Symmetric: $\mathrm{II}(u, v) = \mathrm{II}(v, u)$ (equivalently $S$ is self-adjoint w.r.t. $g$).
- [[Normal Curvature]]: $\kappa_n(u) = \frac{\mathrm{II}(u,u)}{\mathrm{I}(u,u)}$.
- [[Gaussian Curvature]] $K = \frac{\det\mathrm{II}}{\det \mathrm{I}} = \frac{ln - m^2}{EG - F^2}$, [[Mean Curvature]] $H = \frac{Gl + En - 2Fm}{2(EG - F^2)}$.

[^1]: [Crane, p. 41](zotero://open-pdf/library/items/9N6JDPI2?page=42&annotation=BAM68KBF)
[^2]: [Crane, p. 44](zotero://open-pdf/library/items/9N6JDPI2?page=45&annotation=WNXWD9B4)
[^3]: [Crane, p. 45](zotero://open-pdf/library/items/9N6JDPI2?page=46&annotation=VLSRZJG5)
[^4]: [Crane, p. 45](zotero://open-pdf/library/items/9N6JDPI2?page=46&annotation=GGYIFPVF)
