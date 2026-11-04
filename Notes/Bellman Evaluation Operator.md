---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Evaluation Operator[^1]
> For a [[Markov Decision Process]] and a [[Policy]] $\pi$, the operator $\mathcal{T}^\pi : \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|} \to \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$ defined, for $f \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$, by
> $$
> \begin{align}
> (\mathcal{T}^\pi f)(s,a) := R(s,a) + \gamma\, \mathbb{E}_{s' \sim P(s,a)}\big[f(s', \pi(s'))\big]
> \end{align}
> $$
> where for a [[Stochastic Policy|stochastic policy]] $f(s', \pi(s'))$ means $\mathbb{E}_{a' \sim \pi(s')}[f(s', a')]$. The [[Action-Value Function]] $Q^\pi$ is its fixed point, $Q^\pi = \mathcal{T}^\pi Q^\pi$, which restates the [[Bellman Equation (Policy Evaluation)]].

# Properties
- **Affine.** $\mathcal{T}^\pi f = R + \gamma P_\pi f$, where $P_\pi \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}| \times |\mathcal{S}\times\mathcal{A}|}$ is the row-stochastic matrix $[P_\pi]_{(s,a),(s',a')} = P(s'|s,a)\,\pi(a'|s')$. Unlike the [[Bellman Optimality Operator]] $\mathcal{T}$, it has no $\max$.
- **$\gamma$-contraction** under the [[Infinity Norm|infinity norm]]: $\|\mathcal{T}^\pi f - \mathcal{T}^\pi f'\|_\infty = \gamma \|P_\pi(f - f')\|_\infty \leq \gamma \|f - f'\|_\infty$, because each row of $P_\pi$ is a probability vector. By the [[Banach Fixed-Point Theorem]], $Q^\pi$ is its unique fixed point, and $(\mathcal{T}^\pi)^n f \to Q^\pi$ for every $f$.
- **Monotone.** $f \leq f'$ (elementwise) $\Rightarrow \mathcal{T}^\pi f \leq \mathcal{T}^\pi f'$, since $P_\pi$ has nonnegative entries. The optimality operator $\mathcal{T}$ is monotone too.
- **Relation to $\mathcal{T}$.** $\mathcal{T}^\pi f \leq \mathcal{T} f$ for every $\pi$ and $f$, with equality when $\pi = \pi_f$ is the [[Greedy Policy]] of $f$: $\mathcal{T}^{\pi_f} f = \mathcal{T} f$.
- **Use in policy iteration.** Monotonicity gives a short proof of the [[Policy Improvement Theorem]]: $Q^{\pi_k} = \mathcal{T}^{\pi_k} Q^{\pi_k} \leq \mathcal{T} Q^{\pi_k} = \mathcal{T}^{\pi_{k+1}} Q^{\pi_k}$, and applying $\mathcal{T}^{\pi_{k+1}}$ repeatedly gives $Q^{\pi_k} \leq (\mathcal{T}^{\pi_{k+1}})^\infty Q^{\pi_k} = Q^{\pi_{k+1}}$. The contraction and monotonicity of $\mathcal{T}^{\pi^\star}$ drive [[Policy Iteration Exponential Convergence]].
- The state-value version is $\mathcal{T}^\pi V = R^\pi + \gamma P^\pi V$ on $\mathbb{R}^{|\mathcal{S}|}$, with the policy's [[Transition Matrix (Markov Decision Process)|transition matrix]] $P^\pi$; its fixed point is $V^\pi$ ([[Policy Evaluation]]).

# Questions
> [!question]- Why is $\mathcal{T}^\pi$ a $\gamma$-contraction in $\|\cdot\|_\infty$?
> $\mathcal{T}^\pi f - \mathcal{T}^\pi f' = \gamma P_\pi (f - f')$, and every row of $P_\pi$ is a probability vector, so each entry of $P_\pi x$ is a convex combination of entries of $x$. Hence $\|P_\pi x\|_\infty \leq \|x\|_\infty$ and $\|\mathcal{T}^\pi f - \mathcal{T}^\pi f'\|_\infty \leq \gamma\|f - f'\|_\infty$.

> [!question]- Is the state-value operator $\mathcal{T}^\pi V = R^\pi + \gamma P^\pi V$ a contraction in the Euclidean norm $\|\cdot\|_2$ for every $\gamma < 1$?
> No. Take two states that both move to state 1, $P^\pi = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, and $x = (1, 0)^\top$. Then $P^\pi x = (1, 1)^\top$, so $\|\gamma P^\pi x\|_2 = \gamma\sqrt{2}\,\|x\|_2 > \|x\|_2$ when $\gamma > 1/\sqrt{2}$. Row-stochasticity controls $\|\cdot\|_\infty$, not $\|\cdot\|_2$. A weighted $L^2$ norm does work when the weights are the stationary distribution of $P^\pi$ (next card).

> [!question]- How does monotonicity of $\mathcal{T}^\pi$ prove that policy iteration never gets worse?
> With $\pi_{k+1} = \pi_{Q^{\pi_k}}$ greedy: $Q^{\pi_k} = \mathcal{T}^{\pi_k} Q^{\pi_k} \leq \mathcal{T} Q^{\pi_k} = \mathcal{T}^{\pi_{k+1}} Q^{\pi_k}$. Applying the monotone map $\mathcal{T}^{\pi_{k+1}}$ to both sides repeatedly gives $Q^{\pi_k} \leq (\mathcal{T}^{\pi_{k+1}})^n Q^{\pi_k}$ for all $n$. The right side converges to the unique fixed point $Q^{\pi_{k+1}}$ by the contraction property, so $Q^{\pi_k} \leq Q^{\pi_{k+1}}$.

> [!question]- Application: In LSTD with Laplacian features $\Phi$ (CS 542 project), the solution is the fixed point of $\Pi_\mu \mathcal{T}^\pi$, where $\Pi_\mu$ is the $\mu$-weighted orthogonal projection onto $\operatorname{span}(\Phi)$. Why does a unique fixed point exist when $\mu$ is the stationary distribution of $P^\pi$, and what does it cost?
> In $\|v\|_\mu^2 = \sum_s \mu(s) v(s)^2$, Jensen's inequality and $\mu^\top P^\pi = \mu^\top$ give $\|P^\pi v\|_\mu^2 = \sum_s \mu(s)\big(\sum_{s'} P^\pi_{ss'} v(s')\big)^2 \leq \sum_s \mu(s) \sum_{s'} P^\pi_{ss'} v(s')^2 = \|v\|_\mu^2$. So $\mathcal{T}^\pi$ is a $\gamma$-contraction in $\|\cdot\|_\mu$. $\Pi_\mu$ is an orthogonal projection in that inner product, hence non-expansive, so $\Pi_\mu \mathcal{T}^\pi$ is a $\gamma$-contraction with a unique fixed point $\Phi\theta^\star$ (Tsitsiklis & Van Roy, 1997).
>
> By Pythagoras, using $\Pi_\mu V^\pi = \Pi_\mu \mathcal{T}^\pi V^\pi$: $\|V^\pi - \Phi\theta^\star\|_\mu^2 = \|V^\pi - \Pi_\mu V^\pi\|_\mu^2 + \|\Pi_\mu \mathcal{T}^\pi V^\pi - \Pi_\mu \mathcal{T}^\pi \Phi\theta^\star\|_\mu^2 \leq \|V^\pi - \Pi_\mu V^\pi\|_\mu^2 + \gamma^2 \|V^\pi - \Phi\theta^\star\|_\mu^2$. That gives $\|V^\pi - \Phi\theta^\star\|_\mu \leq \|V^\pi - \Pi_\mu V^\pi\|_\mu / \sqrt{1 - \gamma^2}$.
>
> The $\ell_\infty$ argument does not transfer, because $\Pi_\mu$ is generally not non-expansive in $\|\cdot\|_\infty$. Off-policy weights $\mu$ can also break the $\mu$-norm contraction.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 7](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=7)
