---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Discounted State Occupancy[^1]
> For a [[Markov Decision Process]], [[Policy]] $\pi$, and starting state $s$, the (normalized) discounted state occupancy is the distribution $d^{\pi,s} \in \Delta(\mathcal{S})$ given by
> $$
> \begin{align}
> d^{\pi,s} = (1-\gamma)\sum_{t=1}^{\infty} \gamma^{t-1} d^{\pi,s}_t
> \end{align}
> $$
> where $d^{\pi,s}_t(s') = \mathbb{P}[s_t = s' \mid s_1 = s, \pi]$. It measures how often each state is visited along a [[Trajectory]] starting at $s$ and following $\pi$, with later visits discounted more heavily.

# Properties
- The unnormalized occupancy $\sum_{t=1}^{\infty} \gamma^{t-1} d^{\pi,s}_t = d^{\pi,s}/(1-\gamma)$ is the row of $(I_{|\mathcal{S}|} - \gamma P^\pi)^{-1}$ indexed by $s$, from [[Policy Evaluation]]; its entries sum to $1/(1-\gamma)$. Equivalently, $(1-\gamma)(I_{|\mathcal{S}|} - \gamma P^\pi)^{-1}$ is a row-stochastic matrix whose rows are the normalized occupancies.
- Geometric stopping interpretation: if $T$ follows the [[Geometric Distribution]] with success probability $1-\gamma$, counting trials up to and including the first success ($\mathbb{P}(T = t) = (1-\gamma)\gamma^{t-1}$ on $\{1, 2, \dots\}$), independent of the trajectory, then $d^{\pi,s}(s') = \mathbb{P}[s_T = s' \mid s_1 = s, \pi]$. That is, $d^{\pi,s}$ is the distribution of the state at which an episode terminated with per-step survival probability $\gamma$ ends, and the unnormalized total $1/(1-\gamma) = \mathbb{E}[T]$ is the expected episode length.
- Value as an average reward: exchanging the sum over $t$ with the sum over states (justified since rewards are bounded and $\gamma < 1$),
  $$
  \begin{align}
  V^\pi(s) = \frac{1}{1-\gamma}\, \mathbb{E}_{s' \sim d^{\pi,s}}\, \mathbb{E}_{a \sim \pi(s')}\big[R(s', a)\big],
  \end{align}
  $$
  so the [[Value Function|value]] is the expected episode length $1/(1-\gamma)$ times the average one-step reward under $d^{\pi,s}$. When the [[Reward Function (Markov Decision Process)|reward function]] depends only on the current state, the entries of $d^{\pi,s}/(1-\gamma)$ are the linear coefficients relating value to reward.
- Limits in $\gamma$ (for finite $\mathcal{S}$, with $d^{\pi,s}_t$ the row of $(P^\pi)^{t-1}$ indexed by $s$):
  - As $\gamma \to 0$, $d^{\pi,s} \to \delta_s$, the point mass at the starting state.
  - As $\gamma \to 1$, $d^{\pi,s}$ converges to row $s$ of the Cesàro limit $\Pi = \lim_{n \to \infty} \frac{1}{n}\sum_{k=0}^{n-1} (P^\pi)^k$, which exists for every finite Markov chain. This is the statement that Cesàro summability implies Abel summability (an extension of [[Abel's Theorem]]). If $P^\pi$ is irreducible, every row of $\Pi$ is its unique stationary distribution $\mu$, so $d^{\pi,s} \to \mu$ for every $s$ and the starting state is forgotten. Periodicity does not matter here, since only the Cesàro averages, not $(P^\pi)^k$ itself, need to converge.
  - In between, most of the mass lies on the first $O(1/(1-\gamma))$ steps, the effective horizon.
- When the trajectory instead starts with $s_1$ drawn from an initial distribution $d_0$, the notation $d^\pi$ is used, with $d_0$ often omitted.
- Generalizes to [[State-Action Occupancy]].
- The normalized occupancy $d^{\pi',s}$ appears in the [[Performance Difference Lemma]], expressing the value difference between two policies as an expectation of an [[Advantage Function|advantage]] under $d^{\pi',s}$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 3](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=3)
