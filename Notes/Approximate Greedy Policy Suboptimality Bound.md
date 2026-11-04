---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Approximate Greedy Policy Suboptimality Bound[^1]
> For any $f \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$, the [[Greedy Policy]] $\pi_f$ satisfies
> $$
> \begin{align}
> \|V^\star - V^{\pi_f}\|_\infty \leq \frac{2\|f - Q^\star\|_\infty}{1-\gamma}
> \end{align}
> $$

# Properties
- Bounds the suboptimality (or loss) of acting greedily with respect to an approximate Q-value function $f$, rather than the true $Q^\star$.
- Applied to $f = Q^{\star,H}$ from [[Value Iteration]], together with its convergence rate, bounds the suboptimality of the resulting greedy policy.
- Chained with the [[Bellman Error]] bound, it gives decision loss $\frac{2}{(1-\gamma)^2}\|f - \mathcal{T}f\|_\infty$. The [[Bellman Error Performance Difference Bound]] improves this to $\frac{2}{1-\gamma}\|f - \mathcal{T}f\|_\infty$. Its model-based analogue is the [[Evaluation Error to Decision Loss Lemma]].

# Questions
> [!question]- What is the proof idea, and where does the factor $2$ come from?
> Write $V^\star(s) - V^{\pi_f}(s) = [Q^\star(s, \pi^\star(s)) - Q^\star(s, \pi_f(s))] + [Q^\star(s, \pi_f(s)) - Q^{\pi_f}(s, \pi_f(s))]$. Greediness, $f(s, \pi_f(s)) \geq f(s, \pi^\star(s))$, bounds the first bracket by $[Q^\star - f](s, \pi^\star(s)) + [f - Q^\star](s, \pi_f(s)) \leq 2\|f - Q^\star\|_\infty$. That's one error at each of the two actions, hence the $2$. The second bracket is $\gamma\,\mathbb{E}_{s' \sim P(s, \pi_f(s))}[V^\star(s') - V^{\pi_f}(s')] \leq \gamma\|V^\star - V^{\pi_f}\|_\infty$. Taking the sup over $s$ and rearranging divides by $1 - \gamma$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 8](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=8)
