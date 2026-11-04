---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Optimality Operator[^1]
> For a [[Markov Decision Process]] $M$, the operator $\mathcal{T}_M : \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|} \to \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$ (or simply $\mathcal{T}$) defined, for $f \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$, by
> $$
> \begin{align}
> (\mathcal{T}f)(s,a) := R(s,a) + \gamma \langle P(s,a), V_f \rangle
> \end{align}
> $$
> where $V_f(\cdot) := \max_{a\in\mathcal{A}} f(\cdot, a)$.

**Interpretation: one step of backward induction.** Read $f$ as a terminal payoff. Then $(\mathcal{T}f)(s,a)$ is the optimal value of the game "take $a$ at $s$, collect $R(s,a)$, move to $s'$, choose $a'$ optimally, and collect $f(s',a')$". Iterating, $\mathcal{T}^k f$ is the optimal value of the $k$-step problem with terminal payoff $f$ ([[Dynamic Programming]] on a [[Finite-Horizon Markov Decision Process]]):
$$
\begin{align}
(\mathcal{T}^k f)(s,a) = \max_{\pi_2, \dots, \pi_{k+1}} \mathbb{E}\Big[\sum_{t=1}^{k} \gamma^{t-1} r_t + \gamma^k f(s_{k+1}, a_{k+1}) \,\Big|\, s_1 = s, a_1 = a\Big]
\end{align}
$$
The max is over non-stationary policies, where $\pi_t$ chooses $a_t$.
- *Convergence.* The terminal payoff enters discounted by $\gamma^k$, so its influence is at most $\gamma^k\|f - f'\|_\infty$. This is the contraction property, read as "the far future doesn't matter". $Q^\star$ is therefore the infinite-horizon limit of the finite-horizon problems, whatever the initial guess, and $\mathcal{T}^k \mathbf{0}$ is the optimal value of the truncated $k$-step problem ([[Value Iteration]]).
- *Fixed point.* $Q^\star = \mathcal{T}Q^\star$ says that adding one more step of optimal lookahead changes nothing: $Q^\star$ is the unique function that is self-consistent under one-step lookahead. The residual $\|f - \mathcal{T}f\|_\infty$ ([[Bellman Error]]) measures how inconsistent $f$ is and certifies $\|f - Q^\star\|_\infty \leq \|f - \mathcal{T}f\|_\infty/(1-\gamma)$.
- *Iteration vs. policy iteration.* Iterating $\mathcal{T}$ is [[Value Iteration]]. Since $\mathcal{T}f = \mathcal{T}^{\pi_f}f$, each step is "greedy step, then one evaluation step". [[Policy Iteration]] is the other extreme: it runs the evaluation to convergence (the fixed point of $\mathcal{T}^{\pi}$) before each greedy step.

# Properties
- $Q^\star$ is the fixed point of $\mathcal{T}$: $Q^\star = \mathcal{T}Q^\star$, giving a concise restatement of the [[Bellman Optimality Equation]].
- $\mathcal{T}$ is a $\gamma$-[[Contraction]] under the [[Infinity Norm|infinity norm]]: $\|\mathcal{T}f - \mathcal{T}f'\|_\infty \leq \gamma\|f-f'\|_\infty$ for any $f, f' \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$. This property drives the convergence of [[Value Iteration]].
- **Monotone:** $f \leq f' \Rightarrow \mathcal{T}f \leq \mathcal{T}f'$ (elementwise). Its policy-specific counterpart is the [[Bellman Evaluation Operator]] $\mathcal{T}^\pi$, with $\mathcal{T}^\pi f \leq \mathcal{T}f$ and equality for the [[Greedy Policy]] $\pi = \pi_f$.
- **Upper envelope of the evaluation operators:** $\mathcal{T}f = \max_\pi \mathcal{T}^\pi f$ pointwise, with the max attained by $\pi_f$. The two operators perform the same one-step backup and differ only in how the next action is chosen: $\mathcal{T}^\pi$ averages, $f(s',\pi) = \mathbb{E}_{a'\sim\pi(s')}[f(s',a')]$, and $\mathcal{T}$ maximizes, $\max_{a'} f(s',a')$. The superscript tells them apart: $\mathcal{T}^\pi$ is affine, and $\mathcal{T}$ is nonlinear (convex and piecewise affine in $f$).

# Questions
> [!question]- Why is $\mathcal{T}$ a $\gamma$-contraction in $\|\cdot\|_\infty$, despite the nonlinear $\max$?
> $|(\mathcal{T}f - \mathcal{T}f')(s,a)| = \gamma|\langle P(s,a), V_f - V_{f'}\rangle| \leq \gamma\|V_f - V_{f'}\|_\infty$, and $|\max_a f(s,a) - \max_a f'(s,a)| \leq \max_a |f(s,a) - f'(s,a)|$. For the latter, if $V_f(s) \geq V_{f'}(s)$, let $a_0$ be greedy for $f$; then $V_f(s) - V_{f'}(s) \leq f(s, a_0) - f'(s, a_0)$. So $\|V_f - V_{f'}\|_\infty \leq \|f - f'\|_\infty$: the max is 1-Lipschitz in $\|\cdot\|_\infty$.

> [!question]- What decision problem does $\mathcal{T}^k f$ solve, and how does that explain why value iteration converges from any $f$?
> $\mathcal{T}^k f$ is the optimal $Q$-value of the $k$-step problem with terminal payoff $f$ (one backward-induction step per application). Two such problems differ only in their terminal payoff, which enters discounted by $\gamma^k$. For every policy their values differ by at most $\gamma^k\|f - f'\|_\infty$, and a max of functions that are uniformly $\varepsilon$-close is $\varepsilon$-close, so $\|\mathcal{T}^k f - \mathcal{T}^k f'\|_\infty \leq \gamma^k\|f-f'\|_\infty \to 0$. Taking $f' = Q^\star$ gives $\mathcal{T}^k f \to Q^\star$.

> [!question]- How are $\mathcal{T}$ and $\mathcal{T}^\pi$ related, and why does $\mathcal{T}f = \mathcal{T}^{\pi_f}f$ hold?
> Both compute $R(s,a) + \gamma\,\mathbb{E}_{s'}[\,\cdot\,]$. $\mathcal{T}^\pi$ averages the next action under $\pi$, and $\mathcal{T}$ maximizes over it. An average over $a' \sim \pi(s')$ is at most $\max_{a'} f(s',a')$, so $\mathcal{T}^\pi f \leq \mathcal{T}f$. Equality holds when $\pi(s')$ puts all its mass on $\arg\max_{a'} f(s',a')$, which is the greedy policy $\pi_f$. Hence $\mathcal{T} = \max_\pi \mathcal{T}^\pi$ pointwise.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 4](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=4)
