---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Riemannian Metric (Metric Tensor)[^1]
> A Riemannian metric on a smooth [[Manifold]] $M$ is a smoothly varying choice of [[Inner Product]] $g_p: T_pM \times T_pM \rightarrow \mathbb{R}$ on every [[Tangent Space]] $T_pM$: each $g_p$ is a symmetric, positive-definite [[Bilinear Form]]. In local coordinates it is written $g = \sum_{i,j} g_{ij}\, dx^i dx^j$ (the "line element" $ds^2$).

The [[Induced Metric]] $g(X,Y) = df(X)\cdot df(Y)$ of a [[Smooth Surface]] is the special case where the inner product is pulled back from $\mathbb{R}^3$ by an immersion; abstract Riemannian manifolds need not sit inside any Euclidean space.

**Metric tensor vs. distance [[Metric]].** The two are different objects:
- A distance metric $d(x, y)$ (real analysis) takes two *points* and returns a nonnegative number satisfying positivity, symmetry and the triangle inequality. It is global.
- A metric tensor $g_p(X, Y)$ takes two *tangent vectors at the same point* and returns a real number (possibly negative, e.g. $g(X, -X) < 0$). It is local, an infinitesimal ruler and protractor.

They are tied together: $g$ *induces* a distance function. The length of a curve $\gamma: [a,b] \rightarrow M$ is
$$\begin{align}
L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}(\gamma'(t), \gamma'(t))}\, dt,
\end{align}$$
and the Riemannian distance is $d(p, q) = \inf_\gamma L(\gamma)$ over all piecewise smooth curves from $p$ to $q$. On a connected manifold this $d$ satisfies all the [[Metric]] axioms, turns $M$ into a [[Metric Space]], and induces the manifold's original topology. Length-minimizing curves are geodesics.[^2]

**Why both are called "metric".** Both are the basic *measuring* device of their field (Greek *metron*, measure). Riemann introduced the infinitesimal line element $ds^2$ in 1854; Fréchet axiomatized abstract distance spaces in his 1906 thesis, and the name *metric space* (metrischer Raum) was coined by Hausdorff in 1914. The shared name reflects that the tensor produces a distance as above.[^2]

# Properties
- Lengths: $|X|_g = \sqrt{g(X,X)}$; angles: $\cos\theta = \frac{g(X,Y)}{|X|_g |Y|_g}$.
- In coordinates $g$ is represented by a symmetric positive-definite matrix ($\mathrm{I} = [g_{ij}]$), which transforms as a [[Bilinear Form]].
- The [[Dot Product]] itself is the metric tensor of flat $\mathbb{R}^n$; it is not a distance metric, but induces the [[Euclidean Distance]] $d(x,y) = \sqrt{(x-y)\cdot(x-y)}$.
- [[Conformal Map|Conformal]] changes of metric: $\tilde g = e^{u} g$ preserve angles but not lengths.

[^1]: [Crane, p. 29](zotero://open-pdf/library/items/9N6JDPI2?page=30&annotation=SPIM9EV7)
[^2]: [Riemannian manifold - Wikipedia](https://en.wikipedia.org/wiki/Riemannian_manifold)
