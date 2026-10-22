---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] First Fundamental Form[^1]
> The first fundamental form of a [[Smooth Surface]] $f: M \rightarrow \mathbb{R}^3$ is the [[Induced Metric]]:
> $$\begin{align}
> \mathrm{I}(X, Y) := g(X, Y) = df(X) \cdot df(Y).
> \end{align}$$
> In coordinates, $\mathrm{I} = J^TJ = \begin{bmatrix} E & F \\ F & G \end{bmatrix}$ with $E = f_x\cdot f_x$, $F = f_x \cdot f_y$, $G = f_y \cdot f_y$.[^2]

The name is historical: it introduces no new geometric idea beyond the induced metric, which is itself just a function of the immersion $f$. Fewer modern authors use the term.[^1]

# Properties
- Symmetric positive-definite [[Bilinear Form]]; transforms as $\mathrm{I} \mapsto P^{-T}\mathrm{I}P^{-1}$.
- Together with the [[Second Fundamental Form]]: $\kappa_n(u) = \frac{\mathrm{II}(u,u)}{\mathrm{I}(u,u)}$ ([[Normal Curvature]]), $K = \frac{\det \mathrm{II}}{\det \mathrm{I}}$ ([[Gaussian Curvature]]).
- Special case of a [[Riemannian Metric]].

[^1]: [Crane, p. 41](zotero://open-pdf/library/items/9N6JDPI2?page=42&annotation=BAM68KBF)
[^2]: [Crane, p. 44](zotero://open-pdf/library/items/9N6JDPI2?page=45&annotation=W4WHEZJQ)
