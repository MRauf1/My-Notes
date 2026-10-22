---
tags:
  - mathematics
  - abstract_algebra
---

# Definition
> [!info] Group Action[^1]
> A (left) action of a [[Group]] $G$ on a [[Set|set]] $X$ is a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$, such that for all $g, h \in G$ and $x \in X$
> 1) Identity: $e \cdot x = x$
> 2) Compatibility: $g \cdot (h \cdot x) = (gh) \cdot x$
>
> Equivalently, a [[Group Homomorphism]] $\rho: G \to \mathrm{Sym}(X)$ into the [[Symmetric Group]] of $X$, with $\rho(g)(x) = g \cdot x$. When $X$ is a vector space and every $\rho(g)$ is linear, $\rho: G \to \mathrm{GL}(X)$ is a linear representation ([[General Linear Group]]).

**Induced actions on functions and maps.**[^1] An action on $X$ induces one on functions $f: X \to \mathbb{R}$ by $(g \cdot f)(x) = f(g^{-1} \cdot x)$, which moves the graph of $f$ by $g$. The inverse is needed for compatibility, $(g \cdot (h \cdot f))(x) = f(h^{-1}g^{-1}x) = ((gh) \cdot f)(x)$. More generally, actions $\rho_X$ on $X$ and $\rho_Y$ on $Y$ induce the conjugation action on $\mathrm{Map}(X, Y)$:
$$
\begin{align}
(g \cdot F)(x) = \rho_Y(g)\, F\big(\rho_X(g)^{-1} x\big),
\end{align}
$$
whose fixed points are exactly the [[Equivariant Function|equivariant maps]]; with $\rho_Y$ trivial they are the [[Invariant Function|invariant functions]]. Applied to operators $L$ on a function space, this is $L \mapsto T_g L T_g^{-1}$ ([[Laplacian Operator Rigid Motion Invariance]]).

# Types
- Trivial action: $g \cdot x = x$ for all $g$.
- Faithful: $\rho$ is injective (only $e$ acts as the identity).
- Free: $g \cdot x = x$ for some $x$ implies $g = e$.
- Transitive: a single orbit.
- Conjugation action of $G$ on itself, $g \cdot x = gxg^{-1}$ ([[Group Conjugate]]); left multiplication $g \cdot x = gx$ (free and transitive, giving Cayley's theorem $G \hookrightarrow \mathrm{Sym}(G)$).

# Properties
- Each $\rho(g)$ is a [[Bijective Function|bijection]] of $X$ with inverse $\rho(g^{-1})$.
- Orbit $G \cdot x = \{g \cdot x : g \in G\}$; "$x \sim y$ iff $y \in G \cdot x$" is an [[Equivalence Relation]], so the orbits [[Equivalence Relation on Set and Partition Theorem|partition]] $X$.
- Stabilizer $G_x = \{g : g \cdot x = x\}$ is a [[Subgroup]]; orbit-stabilizer theorem $|G \cdot x| = [G : G_x]$ (cf. [[Lagrange's Theorem]]), via the bijection $gG_x \mapsto g \cdot x$ from [[Left Coset|left cosets]].
- $x$ is a fixed point (invariant) iff $G_x = G$, i.e. its orbit is $\{x\}$. "Invariant" is always relative to a specified action.
- Equivariant maps are exactly the structure-preserving maps between $G$-sets, and they send orbits to orbits.
- Symmetries in geometry, physics, and vision are actions: rigid motions on $\mathbb{R}^n$ ([[Rigid-Body Transformation]], [[Group of Special Orthogonal Matrices]]), translations on images ([[Convolutional Layer]]), and permutations on graph nodes ([[Graph Neural Network]]).

[^1]: Added from general knowledge.
