---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Value Iteration
> An algorithm for [[Planning]] that computes a sequence of Q-value functions $Q^{\star,0}, Q^{\star,1}, \dots, Q^{\star,H}$ directly approximating $Q^\star$ (without alternating between value functions and policies as in [[Policy Iteration]]), via
> $$
> \begin{align}
> Q^{\star,h} = \mathcal{T} Q^{\star,h-1}
> \end{align}
> $$
> where $\mathcal{T}$ is the [[Bellman Optimality Operator]] and $Q^{\star,0}$ is often initialized to $\mathbf{0}_{|\mathcal{S}\times\mathcal{A}|}$.

# Properties
- Since $\mathcal{T}$ is a $\gamma$-[[Contraction]] under the infinity norm, $\|Q^{\star,h} - Q^\star\|_\infty \leq \gamma \|Q^{\star,h-1}-Q^\star\|_\infty$, so after $H$ iterations, using $\|Q^{\star,0}-Q^\star\|_\infty \leq R_{max}/(1-\gamma)$:
$$
\begin{align}
\|Q^{\star,H} - Q^\star\|_\infty \leq \gamma^H \frac{R_{max}}{1-\gamma}
\end{align}
$$
- This rate is equivalently derivable by comparing $Q^{\star,H}$ to the [[Truncated Value Function|$H$-step truncated value]] of $\pi^\star$.
- Setting $H \geq \dfrac{\log(R_{max}/(\epsilon(1-\gamma)))}{1-\gamma}$ — the [[Effective Horizon]] — suffices for $Q^{\star,H}$ to be $\epsilon$-close to $Q^\star$.
- The suboptimality of the [[Greedy Policy]] of $Q^{\star,H}$ follows from the [[Approximate Greedy Policy Suboptimality Bound]]: $\|V^\star - V^{\pi_{Q^{\star,H}}}\|_\infty \leq 2\gamma^H R_{max}/(1-\gamma)^2$.
- Convergence can be monitored without knowing $Q^\star$ via the [[Bellman Error]] $\|f - \mathcal{T}f\|_\infty$ of the iterates.
- Outputting the non-stationary policy $\pi_{Q^{\star,H}}, \pi_{Q^{\star,H-1}}, \dots, \pi_{Q^{\star,1}}$ (instead of the greedy policy of the final iterate alone) achieves suboptimality $\gamma^H R_{max}/(1-\gamma)$, dropping a factor of the effective horizon compared to using a single stationary policy.
