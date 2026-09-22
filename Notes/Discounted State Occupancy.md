---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Discounted State Occupancy
> For a [[Markov Decision Process]], [[Policy]] $\pi$, and starting state $s$, the (unnormalized) discounted state occupancy is the expected number of times each state is visited along a [[Trajectory]] starting at $s$ and following $\pi$, with later visits discounted more heavily. It is given by the rows of $(I_{|\mathcal{S}|} - \gamma P^\pi)^{-1}$ from [[Policy Evaluation]], and equivalently by
> $$
> \begin{align}
> d^{\pi,s} = (1-\gamma)\sum_{t=1}^{\infty} \gamma^{t-1} d^{\pi,s}_t
> \end{align}
> $$
> where $d^{\pi,s}_t(s') = \mathbb{P}[s_t = s' \mid s_1 = s, \pi]$, normalized so that its entries sum to $1$.

# Properties
- Entries of the unnormalized vector sum to $1/(1-\gamma)$; multiplying by $(1-\gamma)$ gives the normalized version.
- Arises when the [[Reward Function (Markov Decision Process)|reward function]] depends only on the current state, in which case it gives the linear coefficients relating [[Value Function|value]] to reward.
- When the trajectory instead starts with $s_1$ drawn from an initial distribution $d_0$, the notation $d^\pi$ is used, with $d_0$ often omitted.
- Generalizes to [[State-Action Occupancy]].
- The normalized occupancy $d^{\pi',s}$ appears in the [[Performance Difference Lemma]], expressing the value difference between two policies as an expectation of an [[Advantage Function|advantage]] under $d^{\pi',s}$.
