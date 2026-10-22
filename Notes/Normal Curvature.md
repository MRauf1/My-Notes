---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Normal Curvature[^1]
> Let $df(X)$ be a unit tangent direction at a point of a [[Smooth Surface]] with unit normal $N$. The plane spanned by $df(X)$ and $N$ cuts the surface in a curve (the *normal section*); the curvature $\kappa_n(X)$ of this curve is the normal curvature in direction $X$. It is computed from the [[Weingarten Map]] as[^2]
> $$\begin{align}
> \kappa_n(X) = -\frac{df(X) \cdot dN(X)}{|df(X)|^2} = \frac{g(SX, X)}{g(X, X)}.
> \end{align}$$
> For a unit vector $\mathbf{u}$ tangent to the surface this is O'Neill's $k(\mathbf{u}) = S(\mathbf{u}) \cdot \mathbf{u}$.

![[Normal Curvature.png]]

Derivation: if $\alpha$ is a unit-speed curve in the surface with $\alpha'(0)$ in direction $df(X)$, then $\kappa_n = \alpha'' \cdot N$ (the normal component of its acceleration $T' = \kappa N_\alpha$, [[Frenet Formula]]). Differentiating $\alpha' \cdot N = 0$ gives $\alpha'' \cdot N = -\alpha' \cdot N'$, i.e. minus the tangential part of the change in normal. The denominator $|df(X)|^2$ undoes any stretching from $M$ into $\mathbb{R}^3$, so $X$ need not be unit in the domain.[^3]

Normal curvature is *signed*: the surface can bend toward the normal or away from it.[^3] With O'Neill's convention, $\kappa_n > 0$ means the surface bends toward $N$, $\kappa_n < 0$ away from it. (Crane's formula omits the minus sign, reversing this.)

> [!abstract] Classical Form[^4]
> In terms of the [[First Fundamental Form]] and [[Second Fundamental Form]],
> $$\begin{align}
> \kappa_n(u) = \frac{\mathrm{II}(u,u)}{\mathrm{I}(u,u)} = \frac{u^T \mathrm{I} S u}{u^T \mathrm{I} u} = \frac{(Ju)^T(JSu)}{(Ju)^T(Ju)} = -\frac{df(u)\cdot dN(u)}{|df(u)|^2},
> \end{align}$$
> using $JSu = df(Su) = -dN(u)$; this agrees with the curve-based formula.

For surfaces, curvature is naturally measured as the change of the *normal* (there is no distinguished tangent direction), whereas for curves tangent and normal differ only by a quarter turn, so either works.[^5]

# Properties
- Its extreme values over directions are the [[Principal Curvature|principal curvatures]]; all other values follow from [[Euler's Curvature Formula]].
- It is a Rayleigh quotient of the [[Shape Operator]] with respect to the [[Induced Metric]]: $\kappa_n(X) = \frac{g(SX, X)}{g(X,X)}$.

[^1]: [Crane, p. 38](zotero://open-pdf/library/items/9N6JDPI2?page=39&annotation=3EXYPRAA)
[^2]: [Crane, p. 38](zotero://open-pdf/library/items/9N6JDPI2?page=39&annotation=IW8QK2X4)
[^3]: [Crane, p. 39](zotero://open-pdf/library/items/9N6JDPI2?page=40&annotation=JWJILAED)
[^4]: [Crane, p. 45](zotero://open-pdf/library/items/9N6JDPI2?page=46&annotation=J2Y2DFEC)
[^5]: [Crane, p. 37](zotero://open-pdf/library/items/9N6JDPI2?page=38&annotation=4LRWYT9N)
