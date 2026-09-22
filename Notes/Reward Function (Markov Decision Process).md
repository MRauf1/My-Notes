---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Reward Function (Markov Decision Process)
> In a [[Markov Decision Process]], the function $R: \mathcal{S} \times \mathcal{A} \to [0, R_{max}]$, where $R_{max} > 0$ is a constant. $R(s, a)$ is the immediate reward associated with taking action $a$ in state $s$.

# Properties
- Immediate rewards $r_t = R(s_t, a_t)$ along a [[Trajectory]] are nonnegative and bounded above by $R_{max}$, which bounds the [[Discounted Return]] in $[0, R_{max}/(1-\gamma)]$.
- Distinct from the general [[Reward Function|reward function]] of learning, which measures the quality of a learned function's output; here the reward is specifically a function of the state-action pair the agent occupies.
- More generally, $r_t$ may also depend on $s_{t+1}$ and contain independent noise (special cases include reward depending only on state, as in inverse RL, or on state/action plus independent noise, as in contextual bandits). Defining $R(s,a) = \mathbb{E}[r_t \mid s_t = s, a_t = a]$, marginalizing out $s_{t+1}$ and the independent noise, gives an equivalent state-action reward function under which $V^\pi$ and $Q^\pi$ are unchanged for every $\pi$; the extra randomness can still add noise to sampled trajectories and affect learning efficiency.
- Assuming $R(s,a) \in [0, R_{max}]$ is without loss of generality in the infinite-horizon discounted setting: for any constant $c > 0$, $R$ and $R + c\mathbf{1}$ are equivalent up to shifting the value of every policy, at every initial state, by the constant $c/(1-\gamma)$. So a reward range $R(s,a) \in [-a, b]$ ($a, b > 0$) can be shifted by $c = a$ to obtain a nonnegative reward with $R_{max} = a + b$.
