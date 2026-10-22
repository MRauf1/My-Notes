---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplacian Operator Rigid Motion Invariance[^1][^2]
> Let $g(\mathbf{x}) = B\mathbf{x} + \mathbf{a}$ be a [[Rigid-Body Transformation|rigid motion]] of $\mathbb{R}^n$ ($B$ an [[Orthogonal Matrix]], $\mathbf{a}$ a translation). Then the [[Laplacian Operator]] commutes with $g$: for every $f \in C^2$,
> $$
> \begin{align}
> \Delta (f \circ g) = (\Delta f) \circ g .
> \end{align}
> $$
> Equivalently (passive form), if $\mathbf{x}' = B\mathbf{x} + \mathbf{a}$ are new Cartesian coordinates, then
> $$
> \begin{align}
> u_{x_1 x_1} + \cdots + u_{x_n x_n} = u_{x'_1 x'_1} + \cdots + u_{x'_n x'_n}.
> \end{align}
> $$
> In the plane, translations are $x' = x + a,\ y' = y + b$ and rotations are $x' = x\cos\alpha + y\sin\alpha,\ y' = -x\sin\alpha + y\cos\alpha$.

**Proof.**[^2] By the chain rule $\nabla(f \circ g)(\mathbf{x}) = B^T \nabla f(g(\mathbf{x}))$ and the [[Hessian Matrix|Hessian]] transforms as $H_{f\circ g}(\mathbf{x}) = B^T H_f(g(\mathbf{x}))\, B$. The translation $\mathbf{a}$ drops out under differentiation, and since $\Delta f = \operatorname{tr} H_f$ and $BB^T = I$,
$$
\begin{align}
\Delta(f\circ g)(\mathbf{x}) = \operatorname{tr}\!\big(B^T H_f B\big) = \operatorname{tr}\!\big(H_f B B^T\big) = \operatorname{tr} H_f\big(g(\mathbf{x})\big) = (\Delta f)(g(\mathbf{x})).
\end{align}
$$
In 2D this is the textbook computation: the cross terms $u_{x'y'}$ cancel and $u_{x'x'} + u_{y'y'}$ picks up the factor $\cos^2\alpha + \sin^2\alpha = 1$.[^1]

**Invariant or equivariant?**[^2] Both words describe the same fact, applied to different objects. Let rigid motions [[Group Action|act]] on functions by $(T_g f)(\mathbf{x}) = f(g^{-1}\mathbf{x})$ (move the graph by $g$).
- *$\Delta$ as a map on functions is [[Equivariant Function|equivariant]]:* $\Delta(T_g f) = T_g(\Delta f)$. Transforming the input transforms the output the same way. It is **not** [[Invariant Function|invariant]] in the sense $\Delta(T_g f) = \Delta f$; that holds for a given $f$ exactly when $\Delta f$ itself is a $g$-invariant function.
- *$\Delta$ as an element of the space of operators is invariant:* rigid motions act on operators by conjugation, $L \mapsto T_g L T_g^{-1}$, and $T_g \Delta T_g^{-1} = \Delta$. An operator is a fixed point of conjugation iff it commutes with $T_g$, so "invariant operator" and "equivariant map" are the same statement. This is the PDE textbook usage, and also the signal-processing usage of "shift-invariant" ([[Shift-Invariant System]]).
- *Passive (coordinate) view:* $(\Delta u)(p)$ at a physical point $p$ is the same number in every Cartesian frame; the formula $\sum \partial^2/\partial x_i^2$ keeps its form with no cross terms. This is the same fact read as a change of coordinates rather than a motion of the function.

**Operator vs. equation vs. solution.**[^2]
- The *operator* $\Delta$ commutes with rigid motions (above).
- The *equation* $\Delta u = 0$ is invariant as a set: if $u$ is harmonic on $D$, then $T_g u$ is harmonic on $g(D)$. Rigid motions map solutions to solutions.
- An *individual solution* is generally not invariant. A solution of a boundary value problem inherits a symmetry $g$ only if the domain and the data are $g$-invariant (then $T_g u$ solves the same problem, so $T_g u = u$ by [[Laplace Equation Dirichlet Problem Uniqueness|uniqueness]]). The solutions that are themselves rotation invariant are the [[Radial Harmonic Function|radial harmonic functions]].

# Properties
- Physically, $\Delta$ models isotropic situations with no preferred direction.[^1]
- Holds for the full orthogonal group (reflections included), i.e. for all [[Isometry|isometries]] of $\mathbb{R}^n$.[^3]
- Under dilations, $\Delta$ is homogeneous of degree 2: $\Delta\big(f(\lambda \mathbf{x})\big) = \lambda^2 (\Delta f)(\lambda\mathbf{x})$, so the solution set of the [[Laplace Equation]] is also dilation invariant.[^3]
- Characterization: for $n \ge 2$, every linear differential operator on $\mathbb{R}^n$ that commutes with all rigid motions is a polynomial in $\Delta$ with constant coefficients.[^3]
- Rotational invariance makes polar and spherical coordinates natural: [[Laplacian in Polar Coordinates]], [[Laplacian in Spherical Coordinates]].
- In vision, rotation equivariance is why the [[Laplacian Filter]] (and Laplacian of Gaussian) is an isotropic edge detector needing no separate filter per orientation, unlike first-order directional derivatives, which are only translation equivariant.[^3]
- The [[Diffusion Equation]] and [[Wave Equation]] inherit the same symmetries ([[Diffusion Equation Invariance Properties]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=168&annotation=SUJAHLI8); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=168&annotation=NNBT4983); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=170&annotation=MR6BG2G9); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=170&annotation=VLZFIKNU)
[^2]: Proof via the Hessian and the invariant/equivariant distinction added from general knowledge (clarification requested by the creator).
[^3]: Added from general knowledge.
