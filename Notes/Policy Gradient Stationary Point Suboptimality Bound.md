---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Policy Gradient Stationary Point Suboptimality Bound[^1]
> For any policy $\hat{\pi}$, let $\pi^+ := \pi_{Q^{\hat{\pi}}}$ be the [[Greedy Policy]] of $Q^{\hat{\pi}}$ and $g^{\hat{\pi}}(\pi) := \mathbb{E}_{s\sim d^{\hat{\pi}}}\big[\sum_a Q^{\hat{\pi}}(s,a)\pi(a|s)\big]$, with $\hat{\pi}$ held fixed inside $Q^{\hat{\pi}}$ and $d^{\hat{\pi}}$. Then
> $$
> \begin{align}
> J(\pi^\star) - J(\hat{\pi}) \leq \frac{\|d^{\pi^\star}/d^{\hat{\pi}}\|_\infty}{1-\gamma}\Big(g^{\hat{\pi}}(\pi^+) - g^{\hat{\pi}}(\hat{\pi})\Big),
> \end{align}
> $$
> where $d^\pi$ are normalized discounted [[Discounted State Occupancy|state occupancies]] from $d_0$.

# Properties
- **Proof.**
$$
\begin{align}
J(\pi^\star) - J(\hat{\pi}) &= \tfrac{1}{1-\gamma}\mathbb{E}_{s\sim d^{\pi^\star}}[Q^{\hat{\pi}}(s, \pi^\star) - V^{\hat{\pi}}(s)] \leq \tfrac{1}{1-\gamma}\mathbb{E}_{s\sim d^{\pi^\star}}[Q^{\hat{\pi}}(s, \pi^+) - V^{\hat{\pi}}(s)] \\
&\leq \tfrac{\|d^{\pi^\star}/d^{\hat{\pi}}\|_\infty}{1-\gamma}\mathbb{E}_{s\sim d^{\hat{\pi}}}\Big[\textstyle\sum_a Q^{\hat{\pi}}(s,a)(\pi^+(a|s) - \hat{\pi}(a|s))\Big].
\end{align}
$$
  The first step is the [[Performance Difference Lemma]]. Relaxing $\pi^\star$ to $\pi^+$ makes the integrand $\max_a Q^{\hat{\pi}}(s,a) - V^{\hat{\pi}}(s) \geq 0$, which the change of measure needs.
- **Link to the gradient.** By the [[Policy Gradient Theorem]], $\nabla J(\hat{\pi}) = \frac{1}{1-\gamma}\nabla_\theta g^{\hat{\pi}}(\pi_\theta)|_{\hat{\theta}}$. $g^{\hat{\pi}}$ is linear in the vector $[\pi(a|s)]_{s,a}$, $g^{\hat{\pi}}(\pi) = \beta^\top\pi$ with $\beta(s,a) = Q^{\hat{\pi}}(s,a)d^{\hat{\pi}}(s)$, so $\nabla J(\hat{\pi}) = \frac{1}{1-\gamma}\beta^\top\nabla\pi$, with $\nabla\pi$ the $|\mathcal{S}\times\mathcal{A}|\times d$ Jacobian. A small gradient $\|\beta^\top\nabla\pi\|$ only controls the gap $\beta^\top(\pi^+ - \hat{\pi})$ if some direction $\alpha \in \mathbb{R}^d$ has $\nabla\pi\,\alpha \approx \pi^+ - \hat{\pi}$. Then $\beta^\top(\pi^+ - \hat{\pi}) \approx (1-\gamma)\nabla J(\hat{\pi})^\top\alpha \leq (1-\gamma)\|\nabla J(\hat{\pi})\|\|\alpha\|$.
- **Two obstacles to global optimality of stationary points.**
  1. *Parameterization*: the policy class must be able to move toward $\pi^+$ at $\hat{\theta}$. This holds for tabular or suitable linear classes (Agarwal et al. 2020), but can fail for poorly parameterized or under-expressive classes, giving bad stationary points. [[Natural Policy Gradient]] addresses this.
  2. *Distribution mismatch* $\|d^{\pi^\star}/d^{\hat{\pi}}\|_\infty$, which is more fundamental. Running PG from an exploratory initial distribution $\nu$ gives $d^{\hat{\pi}}_\nu \geq (1-\gamma)\nu$, so the ratio is at most $\|d^{\pi^\star}/\nu\|_\infty/(1-\gamma)$. With a non-exploratory $\nu$, PG can fail even with tabular policies. Compare the [[Concentrability Coefficient]].
- PG is stochastic gradient ascent, so it finds approximate stationary points (small $\|\nabla J(\hat{\pi})\|_2$, or small $\nabla J(\hat{\pi})^\top(\theta' - \hat{\theta})$ for all $\theta' \in \Theta$ when $\Theta$ is constrained) even for non-concave $J$.

# Questions
> [!question]- Why is $\pi^\star$ relaxed to $\pi^+ = \pi_{Q^{\hat{\pi}}}$ before the change of measure?
> The step $\mathbb{E}_{d^{\pi^\star}}[h] \leq \|d^{\pi^\star}/d^{\hat{\pi}}\|_\infty\,\mathbb{E}_{d^{\hat{\pi}}}[h]$ holds only for $h \geq 0$. $Q^{\hat{\pi}}(s, \pi^\star) - V^{\hat{\pi}}(s)$ can be negative at some states, but $Q^{\hat{\pi}}(s, \pi^+) - V^{\hat{\pi}}(s) = \max_a Q^{\hat{\pi}}(s,a) - V^{\hat{\pi}}(s) \geq 0$ everywhere, and it upper bounds the former.

> [!question]- Why does running PG from an exploratory start distribution $\nu$ bound the mismatch by $\|d^{\pi^\star}/\nu\|_\infty/(1-\gamma)$?
> The normalized occupancy $d^{\hat{\pi}}_\nu = (1-\gamma)\sum_t\gamma^{t-1}d^{\hat{\pi}}_{t}$ includes the $t = 1$ term $(1-\gamma)\nu$, so $d^{\hat{\pi}}_\nu(s) \geq (1-\gamma)\nu(s)$ pointwise, whatever $\hat{\pi}$ does. Hence $d^{\pi^\star}(s)/d^{\hat{\pi}}_\nu(s) \leq d^{\pi^\star}(s)/((1-\gamma)\nu(s))$. This doesn't depend on the unknown learned policy, which is the point.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 8–9](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=8)
