---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Banach Fixed-Point Theorem (Contraction Mapping Theorem)[^1]
> Let $(X, d)$ be a nonempty [[Complete Metric Space]] and $T: X \to X$ a [[Contraction|contraction]], i.e. there is $\beta \in [0, 1)$ with
> $$
> \begin{align}
> d(T z', T z) \leq \beta\, d(z', z) \quad \forall z, z' \in X
> \end{align}
> $$
> Then $T$ has a unique fixed point $z^* = T z^*$, and for any $z_0 \in X$ the iterates $z_{k+1} = T z_k$ converge to $z^*$, with
> $$
> \begin{align}
> d(z_k, z^*) \leq \beta^k d(z_0, z^*) \leq \frac{\beta^k}{1 - \beta}\, d(z_0, z_1)
> \end{align}
> $$

**Intuition.** Applying $T$ to both the fixed point and the current iterate leaves the fixed point unchanged but shrinks their distance by a factor $\beta$, so the iterate must approach the fixed point.[^1]

# Properties
- **Inverting $y = z + f(z)$**: if $f$ is a contraction on $\mathbb{R}^D$ (which is complete), then $T(z) = y^* - f(z)$ is also a contraction, so the unique $z^*$ with $z^* + f(z^*) = y^*$ is found by iterating $z_{k+1} = y^* - f(z_k)$ from any $z_0$. This is used to invert contractive [[Residual Flow|residual flows]].[^1]
- On $\mathbb{R}^D$, a differentiable map is a contraction (w.r.t. the Euclidean norm) if its [[Lipschitz Continuity|Lipschitz constant]] $\sup \|\mathbf{J}\|_2 < 1$.
- The convergence of [[Value Iteration]] follows from the [[Bellman Optimality Operator]] being a $\gamma$-contraction in the [[Infinity Norm|infinity norm]].
- Completeness and $\beta < 1$ are both needed: the strict-inequality condition $d(Tz', Tz) < d(z', z)$ alone does not guarantee a fixed point on a non-compact space (e.g. $T(z) = z + 1/z$ on $[1, \infty)$).

[^1]: [Prince, p. 315](zotero://open-pdf/library/items/BWT7FYX5?page=329&annotation=FTEWWCF7); [Prince, p. 316](zotero://open-pdf/library/items/BWT7FYX5?page=330&annotation=W5C73CL7)
