---
tags: [mathematics, complex_analysis]
---

# Definition

> [!info] Definition 1 (Cauchy-Riemann Conditions)
> In particular, we have the Cauchy-Riemann Conditions which are
> $$
> \begin{align}
> u_x(z_0) &= v_y(z_0) \\
> u_y(z_0) &= - v_x(z_0)
> \end{align}
> $$
> which are necessary, but not sufficient for differentiability (i.e. function is differentiable $\implies$ Cauchy-Riemann Conditions hold true).

> [!abstract] Theorem 2 (Cauchy-Riemann Conditions Theorem)
> [[Function]] $f(z) = u(z) + i\ v(z)$ is [[Differentiable Function]] at $z = x + i\ y$ if and only if both $u, v$ are [[Differentiable Function]] at $(x, y) \in \mathbb{R}^2$ and Cauchy-Riemann conditions hold true. In which case,
> $$
> \begin{align}
> f'(z_0) = u_x(z_0) + i\ v_x(z_0) = v_y(z_0) - i\ u_y(z_0)
> \end{align}
> $$

> [!abstract] Corollary 3 (Cauchy-Riemann Conditions Corollary)
> Both $u, v$ have [[Continuous Function]] [[Partial Derivative]] on [[Open Set]] $U \subseteq \mathbb{C}$ and Cauchy-Riemann conditions hold on $U$ if and only if $f(z) = u(z) + i\ v(z)$ is [[Differentiable Function]] on $U$ and $f'(z)$ is [[Continuous Function]] on $U$.
> Such [[Function]] $f$ is called [[Analytic Function]].