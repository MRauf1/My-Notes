---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Evaluation Error to Decision Loss Lemma[^1]
> For [[Markov Decision Process|MDPs]] $M$ and $\widehat{M}$ with the same $\mathcal{S}, \mathcal{A}, \gamma$, and for all $s \in \mathcal{S}$,
> $$
> \begin{align}
> V^\star_M(s) - V^{\pi^\star_{\widehat{M}}}_M(s) \leq 2\sup_{\pi : \mathcal{S} \to \mathcal{A}}\|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty,
> \end{align}
> $$
> where $\pi^\star_{\widehat{M}}$ is the [[Optimal Policy|optimal policy]] of $\widehat{M}$.

# Properties
- **Proof.**
$$
\begin{align}
V^\star_M(s) - V^{\pi^\star_{\widehat{M}}}_M(s) &= V^{\pi^\star_M}_M(s) - V^{\pi^\star_M}_{\widehat{M}}(s) + V^{\pi^\star_M}_{\widehat{M}}(s) - V^{\pi^\star_{\widehat{M}}}_M(s) \\
&\leq V^{\pi^\star_M}_M(s) - V^{\pi^\star_M}_{\widehat{M}}(s) + V^{\pi^\star_{\widehat{M}}}_{\widehat{M}}(s) - V^{\pi^\star_{\widehat{M}}}_M(s) \\
&\leq \|V^{\pi^\star_M}_M - V^{\pi^\star_M}_{\widehat{M}}\|_\infty + \|V^{\pi^\star_{\widehat{M}}}_{\widehat{M}} - V^{\pi^\star_{\widehat{M}}}_M\|_\infty.
\end{align}
$$
  The inequality uses that $\pi^\star_{\widehat{M}}$ maximizes values in $\widehat{M}$.
- Translates *policy evaluation* error (controlled by the [[Simulation Lemma]]) into the suboptimality of the policy that [[Certainty-Equivalence (Reinforcement Learning)|certainty-equivalence]] outputs.
- The value-function analogue of the [[Approximate Greedy Policy Suboptimality Bound]], and of the decision-loss step in the [[Uniform Sampling Simple Regret Bound]]: two estimation errors, one for the truly optimal choice and one for the chosen one.

# Questions
> [!question]- What is the proof idea, and why does the bound have the factor $2$?
> Add and subtract the values of $\pi^\star_M$ and $\pi^\star_{\widehat{M}}$ in $\widehat{M}$, and use $V^{\pi^\star_M}_{\widehat{M}} \leq V^{\pi^\star_{\widehat{M}}}_{\widehat{M}}$ (optimality in $\widehat{M}$). What remains is two evaluation errors, for $\pi^\star_M$ and for $\pi^\star_{\widehat{M}}$, hence the $2$.

> [!question]- Only two policies appear in the proof. Why is the bound stated with a supremum over all policies?
> $\pi^\star_{\widehat{M}}$ is computed from the data, so it is a random policy. A guarantee for each *fixed* policy does not apply to it directly. Bounding the evaluation error uniformly over all deterministic policies covers whichever policy $\widehat{M}$ selects. The [[Simulation Lemma]] gives such a uniform bound for free, since its right side depends only on $\epsilon_R, \epsilon_P$.

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 4](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=4)
