---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] $Q^\star$-Irrelevant Abstract Model Bound[^1]
> Let $\phi$ be an $\epsilon_{Q^\star}$-approximate [[Q-Star-Irrelevant Abstraction|$Q^\star$-irrelevant abstraction]] of $M$, and let $M_\phi$ be an [[Abstract Model (State Abstraction)|abstract model]] with arbitrary weights $\{p_x\}$. Then
> $$
> \begin{align}
> \left\|[Q^\star_{M_\phi}]_M - Q^\star_M\right\|_\infty \leq \frac{2\epsilon_{Q^\star}}{1-\gamma}.
> \end{align}
> $$
> In the exact case ($\epsilon_{Q^\star} = 0$), $[Q^\star_{M_\phi}]_M = Q^\star_M$.

# Properties
- Surprising, because the rewards and transitions of $M_\phi$ average over states that may have very different dynamics, so they need not mean anything individually. Yet the planned $Q^\star$ is still accurate, and with the [[Approximate Greedy Policy Suboptimality Bound]] its greedy policy has loss at most $\frac{4\epsilon_{Q^\star}}{(1-\gamma)^2}$.
- **Exact case.** Write $[Q^\star_M]_\phi(x,a) := Q^\star_M(s,a)$ for any $s \in \phi^{-1}(x)$; this is well-defined by $Q^\star$-irrelevance. For any $x, a$:
$$
\begin{align}
(\mathcal{T}_{M_\phi}[Q^\star_M]_\phi)(x,a) = \sum_{s\in\phi^{-1}(x)} p_x(s)\big(R(s,a) + \gamma\langle P(s,a), V^\star_M\rangle\big) = \sum_{s} p_x(s)\,Q^\star_M(s,a) = [Q^\star_M]_\phi(x,a),
\end{align}
$$
  so $[Q^\star_M]_\phi$ is the fixed point $Q^\star_{M_\phi}$. Here $\langle \Phi P(s,a), [V^\star_M]_\phi\rangle = \langle P(s,a), V^\star_M\rangle$ because $V^\star_M$ is piecewise constant.
- **Approximate case.** $Q^\star_M$ is no longer piecewise constant, so $\mathcal{T}_{M_\phi}$ cannot be applied to it. Introduce an auxiliary MDP over the *primitive* states, $M'_\phi = (\mathcal{S}, \mathcal{A}, P'_\phi, R'_\phi, \gamma)$, with $R'_\phi(s,a) = \mathbb{E}_{\tilde{s}\sim p_{\phi(s)}}[R(\tilde{s},a)]$ and $P'_\phi(s' \mid s,a) = \mathbb{E}_{\tilde{s}\sim p_{\phi(s)}}[P(s' \mid \tilde{s},a)]$.
  - Its optimal Q-function is the lifted one, $Q^\star_{M'_\phi} = [Q^\star_{M_\phi}]_M$, which one checks by showing $\mathcal{T}_{M'_\phi}[Q^\star_{M_\phi}]_M = [Q^\star_{M_\phi}]_M$.
  - It is defined on $\mathcal{S}$, so its Bellman operator can be applied to $Q^\star_M$.
  - Then $\|[Q^\star_{M_\phi}]_M - Q^\star_M\|_\infty \leq \frac{1}{1-\gamma}\|\mathcal{T}_{M'_\phi}Q^\star_M - Q^\star_M\|_\infty$. Each entry equals $|\sum_{\tilde{s}:\phi(\tilde{s})=\phi(s)} p_{\phi(s)}(\tilde{s})(Q^\star_M(\tilde{s},a) - Q^\star_M(s,a))| \leq 2\epsilon_{Q^\star}$, since aggregated states have $Q^\star_M$ within $2\epsilon_{Q^\star}$ of each other.
- Explains why guarantees of e.g. Delayed Q-learning (a PAC-MDP algorithm) extend to $Q^\star$-irrelevant abstractions.

# Questions
> [!question]- Why is the auxiliary MDP $M'_\phi$ over primitive states needed in the approximate case?
> The natural route, showing $Q^\star_M$ is nearly a fixed point of $\mathcal{T}_{M_\phi}$, fails because $Q^\star_M$ is a function on $\mathcal{S}$, not $\mathcal{S}_\phi$. When $\phi$ is inexact, $Q^\star_M$ is not piecewise constant and has no abstract version. $M'_\phi$ has the same aggregated parameters but lives on $\mathcal{S}$. Its optimal $Q$ is the lifted $Q^\star_{M_\phi}$, and its Bellman operator can be applied to $Q^\star_M$. The standard contraction argument then works on $\mathcal{S}$.

> [!question]- Where does the $2\epsilon_{Q^\star}$ in the Bellman residual come from?
> $(\mathcal{T}_{M'_\phi}Q^\star_M)(s,a) = \sum_{\tilde{s}} p_{\phi(s)}(\tilde{s})(R(\tilde{s},a) + \gamma\langle P(\tilde{s},a), V^\star_M\rangle) = \sum_{\tilde{s}} p_{\phi(s)}(\tilde{s})Q^\star_M(\tilde{s},a)$, an average of $Q^\star_M$ over the class of $s$. With $f$ the abstract function in the definition, $|Q^\star_M(\tilde{s},a) - Q^\star_M(s,a)| \leq |Q^\star_M(\tilde{s},a) - f(\phi(s),a)| + |f(\phi(s),a) - Q^\star_M(s,a)| \leq 2\epsilon_{Q^\star}$ for any $\tilde{s}$ in the same class.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 8–9](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=8)
