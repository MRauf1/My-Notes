---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Per-Step Importance Sampling[^1]
> With the notation of [[Per-Trajectory Importance Sampling]], the per-step IS estimate of $J(\pi)$ is
> $$
> \begin{align}
> \sum_{h=1}^H\gamma^{h-1}\rho_{1:h}\,r_h,
> \end{align}
> $$
> which weights $r_h$ only by the ratios of the actions $a_{1:h}$ that precede it. Equivalently, with $v_0 := 0$ and
> $$
> \begin{align}
> v_{H-h+1} := \rho_h\big(r_h + \gamma v_{H-h}\big), \qquad h = H, H-1, \dots, 1,
> \end{align}
> $$
> the estimate is $v_H$.

# Properties
- **Unbiasedness by induction (bandit view).** Suppose $v_{H-h}$ is unbiased for $V^\pi(s_{h+1})$ given the observed $s_{h+1}$ (trivial for $v_0$ at $h = H$). Then $r_h + \gamma v_{H-h}$ is unbiased for $Q^\pi(s_h, a_h)$. Step $h$ is then a [[Contextual Bandit]] with context $s_h$, arm $a_h \sim \pi_b$, and random reward of mean $Q^\pi(s_h, a_h)$. So the [[Inverse Propensity Score Estimator]] $\rho_h(r_h + \gamma v_{H-h})$ is unbiased for $Q^\pi(s_h, \pi) = V^\pi(s_h)$ ([[Bellman Equation (Policy Evaluation)]]).
- Rewards are additive, and actions $a_{h+1:H}$ don't affect $r_h$, so dropping their ratios removes variance without bias.
- Applying the bandit [[Doubly Robust Estimator]] at each step of the recursion gives multi-step DR (Jiang & Li 2016). Weighted versions: [[Self-Normalized Importance Sampling]].
- Its variance satisfies a Bellman-type recursion, the [[Bellman Equation for Variance]].

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 4–5](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=4)
