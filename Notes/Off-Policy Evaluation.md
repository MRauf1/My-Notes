---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Off-Policy Evaluation[^1]
> The problem of estimating the value $J(\pi)$ of a target [[Policy|policy]] $\pi$ from data collected by a different (behavior) policy $\pi_b$, without deploying $\pi$.

# Properties
- The on-policy counterpart, [[Policy Evaluation]] from rollouts of $\pi$ itself, needs no correction. Off-policy, the data distribution must be reweighted ([[Importance Sampling]]) or modeled.
- Importance-weighted estimators need $\pi$ supported on $\pi_b$. The unknown context/state distribution and reward/transition models cancel in the importance ratio, leaving only policy ratios $\pi(a|s)/\pi_b(a|s)$.
- Estimators: [[Inverse Propensity Score Estimator]] (bandits), [[Per-Trajectory Importance Sampling]], [[Per-Step Importance Sampling]], [[Doubly Robust Estimator]], [[Self-Normalized Importance Sampling|weighted IS]]. Model-based alternatives regress Q-functions from the data (e.g. fitted Q-evaluation, the policy-evaluation analogue of [[Fitted Q-Iteration]]).
- Importance-weighted estimators have variance exponential in the horizon in the worst case, and this is unavoidable in general (Jiang & Li 2016).

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 1–4](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=1)
