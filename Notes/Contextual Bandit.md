---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Contextual Bandit[^1]
> A contextual bandit has a context space $\mathcal{X}$, a context distribution $d_0 \in \Delta(\mathcal{X})$, a discrete action space $\mathcal{A}$, and a reward function $R : \mathcal{X}\times\mathcal{A} \to \Delta([0,1])$. In each round, a context $x \sim d_0$ is drawn, the learner picks $a \sim \pi(\cdot \mid x)$, and observes only $r \sim R(x,a)$. The value of a [[Policy|policy]] $\pi : \mathcal{X} \to \Delta(\mathcal{A})$ is $J(\pi) := \mathbb{E}[r \mid x \sim d_0, a \sim \pi(\cdot|x)]$.

# Properties
- Generalizes the [[Multi-Armed Bandit]] (one context) and is a [[Markov Decision Process]] with horizon 1 (the action does not affect the next context).
- Only the reward of the chosen action is observed (bandit feedback), so evaluating a different policy from logged data requires [[Off-Policy Evaluation]], e.g. the [[Inverse Propensity Score Estimator]].
- Each step of a multi-step MDP, viewed with $s_h$ as context and the random return-to-go as reward, is a contextual bandit. This is the view behind the recursive form of [[Per-Step Importance Sampling]].

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 1–2](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=1)
