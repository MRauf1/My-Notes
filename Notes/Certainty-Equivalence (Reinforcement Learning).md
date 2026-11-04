---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Certainty-Equivalence (Reinforcement Learning)[^1]
> A [[Model-Based Reinforcement Learning|model-based]] algorithm that estimates an MDP model from data and then plans in it as if it were true. Given a dataset of [[Trajectory|trajectories]] broken into tuples $(s, a, r, s')$, let $D_{s,a}$ be the tuples with first two entries $(s, a)$. With $\mathbf{e}_{s'}$ the unit vector for $s'$, the tabular estimates are
> $$
> \begin{align}
> \widehat{P}(s, a) = \frac{1}{|D_{s,a}|}\sum_{(r, s') \in D_{s,a}} \mathbf{e}_{s'}, \qquad \widehat{R}(s, a) = \frac{1}{|D_{s,a}|}\sum_{(r, s') \in D_{s,a}} r.
> \end{align}
> $$
> The algorithm outputs the [[Optimal Policy|optimal policy]] $\pi^\star_{\widehat{M}}$ of $\widehat{M} = (\mathcal{S}, \mathcal{A}, \widehat{P}, \widehat{R}, \gamma)$.

# Properties
- $\widehat{P}(s' \mid s, a)$ is the empirical frequency of observing $s'$ after taking $a$ in $s$. $\widehat{P}$ and $\widehat{R}$ are the maximum likelihood estimates of the [[Transition Function]] and [[Reward Function (Markov Decision Process)|reward function]] (compare [[Multinomial Distribution Maximum Likelihood Estimation]]).
- $\widehat{P}$ is well-defined only if $n(s, a) = |D_{s,a}| > 0$ for every $(s, a)$.
- To specify the algorithm, it suffices to specify the model estimation step. Planning in $\widehat{M}$ can use any exact method ([[Value Iteration]], [[Policy Iteration]], [[Linear Programming (Markov Decision Process)|LP]]).
- Its guarantees are analysed in [[Certainty-Equivalence Sample Complexity]].
- Can be run over a [[State Abstraction|state abstraction]] by converting each tuple to $(\phi(s), a, r, \phi(s'))$. This estimates the [[Abstract Model (State Abstraction)|abstract model]], with guarantees in [[State Abstraction Finite Sample Bound]].

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 1](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=1)
