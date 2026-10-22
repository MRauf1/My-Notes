---
tags:
  - mathematics
  - differential_geometry
---

# Definition

> [!info] Definition 1 ([[Tangent]] [[Mapping|Map]] for [[Smooth Curve]])[^1]
> Let $F: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be a [[Mapping]] and $\alpha: I \rightarrow \mathbb{R}^n$ be a [[Curve]] in $\mathbb{R}^n$ with initial [[Velocity Vector of Smooth Curve]] $\alpha'(0) = \mathbf{v}_{\mathbf{p}} \in T_{\mathbf{p}}(\mathbb{R}^n)$. Then $F_*: T_{\mathbf{p}}(\mathbb{R}^n) \rightarrow T_{F(\mathbf{p})}(\mathbb{R}^m)$ with $F_*(\mathbf{v}_{\mathbf{p}}) = \beta'(0)$, where $\beta$ is the [[Curve Under Mapping]], is the tangent map.

$F_*$ sends [[Tangent Vector]] in $\mathbb{R}^n$ to [[Tangent Vector]] in $\mathbb{R}^m$. In particular, it sends the [[Velocity Vector of Smooth Curve]] of $\alpha$ at $\alpha(t) = \mathbf{p}$ to a [[Velocity Vector of Smooth Curve]] of $\beta$ at $F(\mathbf{p})$.

> [!info] Definition 2 (Calculating Tangent Map)
> Let $F = (f_1, \dots, f_m)$ be a [[Mapping]] $F: \mathbb{R}^n \rightarrow \mathbb{R}^m$. If $\mathbf{v}_{\mathbf{p}} \in T_{\mathbf{p}}(\mathbb{R}^n)$, then
> $$
> \begin{align}
> F_*(\mathbf{v}_{\mathbf{p}}) = (\nabla_{\mathbf{v}} f_1(\mathbf{p}), \dots, \nabla_{\mathbf{v}} f_m(\mathbf{p}))_{F(\mathbf{p})}
> \end{align}
> $$

> [!info] Definition 3 (Differential / Pushforward)[^2][^3]
> The differential $df$ of a map $f$ between spaces tells how to map ("push forward") a tangent vector $X$ in the domain to the corresponding tangent vector $df(X)$ in the target:
> $$\begin{align}
> df_p(X) = \lim_{h \rightarrow 0} \frac{f(p + hX) - f(p)}{h}.
> \end{align}$$
> In coordinates it is the [[Jacobian Matrix]]: for $f(x_1, x_2) = (f_1, f_2, f_3)$, $df(X) = JX$ with $J = \left[\partial f_i/\partial x_j\right] \in \mathbb{R}^{3 \times 2}$.[^4]

Fundamentally there is nothing deeper to the differential than this picture: it tells how to stretch out or push forward little arrows as one goes from one space to another. Any map can be viewed as bending, twisting, stretching (or tearing); derivatives describe what happens to little arrows along the way.[^2][^5] $F_*$, $df$ and "pushforward" are names for the same object.

![[Smooth Surface Immersion.png]]

**Points vs. vectors.** Yes: $f$ maps points to points, $df_p$ maps tangent vectors at $p$ to tangent vectors at $f(p)$, linearly ($df_p: T_pM \rightarrow T_{f(p)}N$). The pair $(p, X) \mapsto (f(p), df_p(X))$ is a map of [[Tangent Bundle|tangent bundles]] $TM \rightarrow TN$.

**Higher differentials.** The second derivative $d^2f_p$ is not a map on vectors but a *symmetric bilinear* map: it eats two tangent vectors and returns a vector in the target, $d^2f_p(X, Y) = \sum_{i,j} X_iY_j\, \partial_i\partial_j f$ (for $f: \mathbb{R}^2 \rightarrow \mathbb{R}^3$ an array of shape $3 \times 2 \times 2$, i.e. a [[Hessian Matrix]] per output component). The $k$-th derivative is a symmetric $k$-linear map (a tensor with $k$ vector inputs and one vector output). Caveats:
- On curved domains/targets, $d^2f$ is not coordinate-independent by itself; one needs a connection (covariant derivative) to define a Hessian. With flat $M \subset \mathbb{R}^2$ and target $\mathbb{R}^3$, as for a [[Smooth Surface]], it is fine.
- The normal component of $d^2f$ of a surface is exactly the [[Second Fundamental Form]] ($l = N \cdot f_{xx}$, etc.).
- In exterior calculus, $d$ denotes the [[Exterior Derivative]] and $d \circ d = 0$, so "$d^2f$" there means something else entirely (it vanishes).

**Real-valued case.** For $\phi: M \rightarrow \mathbb{R}$, the pushforward $d\phi(X)$ is a tangent vector on $\mathbb{R}$. Since $T_q\mathbb{R}$ is a 1-dimensional vector space, choosing the positively oriented unit vector $e$ as its basis identifies every tangent vector $ce$ with the real number $c$ (its signed coordinate, not its norm, so the identification is a bijective linear isomorphism $T_q\mathbb{R} \cong \mathbb{R}$). Under this identification $d\phi(X)$ is a number and the pushforward coincides with the [[Differential]] as a [[1-Form]]: on $\mathbb{R}$, $\phi' = d\phi(X)$ for $X$ the positive unit vector, the "stretch factor" between the two copies of $\mathbb{R}$; on $\mathbb{R}^2$, $d\phi(X)$ is the [[Directional Derivative]].[^6]

![[Derivative as Stretch Factor.png]]

Checking that both sides of a formula have the same type (scalar vs. vector, tangent to which space) is a useful sanity check, like matching physical units.[^6] E.g. the graph $\gamma(x) = (x, \phi(x))$ also stretches $\mathbb{R}$, but into $\mathbb{R}^2$: $d\gamma(X)$ is a 2-vector with $|d\gamma(X)| = \sqrt{1 + (\phi')^2}$, which is not the derivative $\phi'$.[^7]

# Properties
- [[Tangent Map as Linear Transformation]]
- [[Tangent Map Velocity Vector of Curve]]
- [[Tangent Map on Natural Frame Field]]
- [[Induced Metric]]: $g(X,Y) = df(X)\cdot df(Y)$
- [[Weingarten Map]]: the differential of the [[Gauss Map]]
- [[Conformal Map]], [[Isometric Parameterization]]: constraints on how $df$ stretches vectors

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=52)
[^2]: [Crane, p. 29](zotero://open-pdf/library/items/9N6JDPI2?page=30&annotation=ZRLUCB2U)
[^3]: [Crane, p. 42](zotero://open-pdf/library/items/9N6JDPI2?page=43&annotation=49FPU7GV)
[^4]: [Crane, p. 42](zotero://open-pdf/library/items/9N6JDPI2?page=43&annotation=G3X64FUD)
[^5]: [Crane, p. 34](zotero://open-pdf/library/items/9N6JDPI2?page=35&annotation=Q82RWRSI)
[^6]: [Crane, p. 32](zotero://open-pdf/library/items/9N6JDPI2?page=33&annotation=A253QKNN)
[^7]: [Crane, p. 33](zotero://open-pdf/library/items/9N6JDPI2?page=34&annotation=W2U8ZJGC)
