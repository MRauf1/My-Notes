---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] State Abstraction Hierarchy Theorem[^1]
> For an MDP $M$ with rewards in $[0, R_{max}]$ and a [[State Abstraction|state abstraction]] $\phi$:
> 1. If $\phi$ is an $(\epsilon_R, \epsilon_P)$-approximate [[Model-Irrelevant Abstraction|model-irrelevant abstraction]], it is an approximate [[Q-Star-Irrelevant Abstraction|$Q^\star$-irrelevant abstraction]] with
> $$
> \begin{align}
> \epsilon_{Q^\star} = \frac{\epsilon_R}{1-\gamma} + \frac{\gamma\,\epsilon_P\,R_{max}}{2(1-\gamma)^2}.
> \end{align}
> $$
> 2. If $\phi$ is an $\epsilon_{Q^\star}$-approximate $Q^\star$-irrelevant abstraction, it is an approximate [[Pi-Star-Irrelevant Abstraction|$\pi^\star$-irrelevant abstraction]] with $\epsilon_{\pi^\star} = 2\epsilon_{Q^\star}/(1-\gamma)$.
>
> In particular (all errors $0$): model-irrelevance $\Rightarrow$ $Q^\star$-irrelevance $\Rightarrow$ $\pi^\star$-irrelevance.

# Properties
- **Proof of (2).** Apply the [[Approximate Greedy Policy Suboptimality Bound]] with $f = [f_\phi]_M$. Its greedy policy $\pi_{[f_\phi]_M}$ is constant on classes of $\phi$, hence a lifted abstract policy.
- **Proof of (1).** Take $f = Q^\star_{M_\phi}$ for the [[Abstract Model (State Abstraction)|abstract model]] with any weights. The contraction of $\mathcal{T}$ (cf. [[Bellman Error]]) gives $\|[Q^\star_{M_\phi}]_M - Q^\star_M\|_\infty \leq \frac{1}{1-\gamma}\|[\mathcal{T}_{M_\phi}Q^\star_{M_\phi}]_M - \mathcal{T}[Q^\star_{M_\phi}]_M\|_\infty$. For each $(s,a)$, the reward mismatch is at most $\epsilon_R$ by the abstract-model lemma.
  - Since $[V^\star_{M_\phi}]_M$ is piecewise constant, $\langle P(s,a), \Phi^\top V^\star_{M_\phi}\rangle = \langle \Phi P(s,a), V^\star_{M_\phi}\rangle$. The transition mismatch is therefore $\gamma|\langle P_\phi(\phi(s),a) - \Phi P(s,a), V^\star_{M_\phi}\rangle| \leq \gamma\epsilon_P\frac{R_{max}}{2(1-\gamma)}$, after centering as in the [[Simulation Lemma]].
- Lenient notions (e.g. $\pi^\star$-irrelevance) give more generalization but work with fewer algorithms. Strict notions (bisimulation) preserve more structure of $M$ and work with more algorithms, but aggregate less.
- The hierarchy is from Li, Walsh & Littman (2006), who also include two further abstraction types and the raw state representation.

# Questions
> [!question]- Why does the proof of claim (1) need the lifted $V^\star_{M_\phi}$ to be piecewise constant?
> It lets the true next-state distribution $P(s,a)$ over $\mathcal{S}$ be replaced by its collapse $\Phi P(s,a)$ over $\mathcal{S}_\phi$: $\langle P(s,a), \Phi^\top V\rangle = \langle \Phi P(s,a), V\rangle$. The approximate bisimulation condition only controls $\Phi P$, the distribution over abstract states, not $P$ itself. Then the difference is between two distributions on $\mathcal{S}_\phi$, $\ell_1$-close by the abstract-model lemma.

> [!question]- Is the converse of "model-irrelevance $\Rightarrow$ $Q^\star$-irrelevance" true?
> No. Take two states with a single action, where $s^{(1)}$ gets reward $1$ and then moves to an absorbing zero-reward state, and $s^{(2)}$ gets reward $0$ and moves to an absorbing state with reward $1/\gamma - 1 \geq 0$ per step (for $\gamma \in (1/2, 1)$, so the reward is in $[0,1]$). Then $Q^\star(s^{(1)}) = 1$ and $Q^\star(s^{(2)}) = 0 + \gamma \cdot \frac{1/\gamma - 1}{1-\gamma} = 1$. Aggregating $s^{(1)}, s^{(2)}$ (and keeping the absorbing states separate) is $Q^\star$-irrelevant but not model-irrelevant, since the rewards differ. Agreeing on $Q^\star$ does not require agreeing on rewards or dynamics.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 2, 5–6](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=5)
