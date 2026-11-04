---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Policy Improvement Theorem[^1]
> In [[Policy Iteration]], $V^{\pi_k}(s) \geq V^{\pi_{k-1}}(s)$ holds for all $k \geq 1$ and $s \in \mathcal{S}$, and the improvement is strictly positive in at least one state until $\pi^\star$ is found.

# Properties
- Follows from the [[Performance Difference Lemma]]: $V^{\pi_k}(s) - V^{\pi_{k-1}}(s)$ decomposes into a sum of nonnegative [[Advantage Function|advantage]] terms, nonnegative because $\pi_k$ is the [[Greedy Policy]] of $\pi_{k-1}$'s Q-value function.
- Alternative (classical) proof via monotonicity of the [[Bellman Evaluation Operator]]: $Q^{\pi_k} = \mathcal{T}^{\pi_k}Q^{\pi_k} \leq \mathcal{T}Q^{\pi_k} = \mathcal{T}^{\pi_{k+1}}Q^{\pi_k} \leq (\mathcal{T}^{\pi_{k+1}})^2 Q^{\pi_k} \leq \dots \leq (\mathcal{T}^{\pi_{k+1}})^\infty Q^{\pi_k} = Q^{\pi_{k+1}}$.

# Questions
> [!question]- What is the proof idea of the policy improvement theorem?
> Apply the [[Performance Difference Lemma]] with $\pi' = \pi_k$, $\pi = \pi_{k-1}$: $V^{\pi_k}(s) - V^{\pi_{k-1}}(s) = \frac{1}{1-\gamma}\mathbb{E}_{s' \sim d^{\pi_k, s}}[A^{\pi_{k-1}}(s', \pi_k)]$. Since $\pi_k$ is greedy for $Q^{\pi_{k-1}}$, $A^{\pi_{k-1}}(s', \pi_k) = \max_a Q^{\pi_{k-1}}(s', a) - V^{\pi_{k-1}}(s') \geq 0$ at every state.

> [!question]- Why must the improvement be strict at some state unless $\pi_{k-1}$ is already optimal?
> If $A^{\pi_{k-1}}(s, \pi_k) = 0$ for all $s$, then $V^{\pi_{k-1}}(s) = \max_a Q^{\pi_{k-1}}(s, a)$. With the [[Bellman Equation (Policy Evaluation)]], $Q^{\pi_{k-1}}$ then satisfies the [[Bellman Optimality Equation]], whose unique solution is $Q^\star$. So $\pi_{k-1}$ is optimal. Otherwise some $s_0$ has a positive advantage, and $d^{\pi_k, s_0}(s_0) \geq 1 - \gamma > 0$ puts weight on it, so $V^{\pi_k}(s_0) > V^{\pi_{k-1}}(s_0)$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 6](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=6)
