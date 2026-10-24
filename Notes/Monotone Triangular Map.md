---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Monotone Triangular Map[^1]
> A map $T: \mathbb{R}^D \to \mathbb{R}^D$ is **triangular** if its $i$-th component depends only on the first $i$ inputs,
> $$
> \begin{align}
> T(\mathbf{x}) = \big(T_1(x_1),\; T_2(x_1, x_2),\; \dots,\; T_D(x_1, \dots, x_D)\big)
> \end{align}
> $$
> and **monotone (increasing)** if each $T_i$ is strictly increasing in its last argument $x_i$. Its [[Jacobian Matrix]] is then [[Lower Triangular Matrix|lower triangular]] with positive diagonal entries $\partial T_i / \partial x_i > 0$.

# Properties
- **Invertible by forward substitution**: given $\mathbf{y} = T(\mathbf{x})$, recover $x_1$ from $y_1 = T_1(x_1)$, then $x_2$ from $y_2 = T_2(x_1, x_2)$ with $x_1$ known, and so on; each step inverts a strictly increasing 1D function, so $T$ is a [[Bijective Function|bijection]] onto its image. This is the nonlinear analogue of [[Triangular Matrix Invertibility]] (nonzero diagonal).
- **Cheap determinant**: $\det J_T(\mathbf{x}) = \prod_{i=1}^D \partial T_i / \partial x_i$, an $O(D)$ computation instead of $O(D^3)$ ([[Triangular Matrix Determinant]]); the off-diagonal entries never need to be computed.
- **Inversion is sequential**: the inverse needs $D$ dependent steps, while the forward pass can be parallel (or vice versa); this is the fast/slow asymmetry of [[Autoregressive Flow|autoregressive flows]].
- **Composition**: compositions of triangular maps are triangular; interleaving [[Permutation Matrix|permutations]] gives non-triangular maps that keep a cheap determinant ([[Coupling Flow]]).
- **No loss of generality for transport**: any absolutely continuous distribution can be pushed onto any other by a monotone triangular map ([[Knothe-Rosenblatt Rearrangement]]), which is why restricting [[Normalizing Flow|normalizing flows]] to triangular Jacobians does not shrink the set of reachable distributions ([[Normalizing Flow Expressivity]]).

[^1]: Supplementary notes provided by the creator.
