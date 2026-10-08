---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Dirichlet Energy[^1]
> For a function $u$ on a domain $\Omega \subset \mathbb{R}^d$,
> $$
> \begin{align}
> D[u] = \int_\Omega |\nabla u|^2 \, d\mathbf{x} \qquad \left(= \int_0^l |u'|^2\, dx \text{ on an interval}\right),
> \end{align}
> $$
> sometimes with a factor $\tfrac12$. It is the quadratic form of $-\Delta$ ([[Laplacian Operator]]): by [[Integration by Parts]] (Green's identity),
> $$
> \begin{align}
> \langle -\Delta u, u \rangle = D[u] - \int_{\partial\Omega} \bar u\, \frac{\partial u}{\partial n}\, dS,
> \end{align}
> $$
> and the boundary term vanishes for Dirichlet or Neumann conditions and becomes $\int_{\partial\Omega} a|u|^2\, dS$ for Robin conditions $\partial u/\partial n + au = 0$.

**Rayleigh quotient.** Eigenvalues of $-\Delta$ with a given boundary condition are the critical values of $R[u] = D_{\text{bc}}[u] / \|u\|^2$; the smallest is $\lambda_1 = \min R$, and the Courant–Fischer min–max principle gives all the others. Dirichlet conditions restrict the admissible $u$, Neumann conditions do not, which yields the bracketing $\lambda_n^{\text{Neumann}} \le \lambda_n^{\text{Dirichlet}}$.

**In an eigenbasis.** If $u = \sum_n c_n \hat X_n$ with $\{\hat X_n\}$ an orthonormal eigenbasis, then $\|u\|^2 = \sum |c_n|^2$ ([[Parseval's Theorem]]) and $D[u] = \sum \lambda_n |c_n|^2$: the eigenfunctions simultaneously diagonalize mass and energy, so $D$ is a frequency-weighted norm (the $\dot H^1$ seminorm).

# Properties
- Positive semidefinite; its kernel (with Neumann conditions on a connected domain) is the constants, giving the Poincaré–Wirtinger inequality $\|u - \bar u\|^2 \le D[u]/\lambda_1$ (see [[Neumann Eigenvalue Problem on an Interval]], [[Dirichlet Eigenvalue Problem on an Interval]]).
- Sign of the Robin quadratic form decides the sign of the eigenvalues ([[Robin Eigenvalue Problem on an Interval]]).
- Diffusion is its $L^2$ gradient flow and dissipates it ([[Diffusion Equation on a Finite Interval]]); for waves it is the potential part of the conserved energy ([[Wave Equation Energy Conservation]]).
- Minimizers with prescribed boundary values are [[Harmonic Function|harmonic functions]] (Dirichlet's principle).
- Discrete counterpart: $\mathbf{x}^T\mathbf{L}\mathbf{x} = \sum_{(i,j)\in E}(x_i - x_j)^2$ for the [[Graph Laplacian Matrix]]; the smoothness regularizer used in spectral clustering and geometry processing.

[^1]: Added from general knowledge to connect the eigenvalue problems of [[Separation of Variables]] to spectral theory.
