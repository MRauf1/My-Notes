---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Per-Trajectory Importance Sampling[^1]
> In an MDP whose trajectories $\tau = (s_1, a_1, r_1, \dots, s_H, a_H, r_H)$ terminate within $H$ steps, given trajectories from a behavior policy $\pi_b$ and a target policy $\pi$ supported on $\pi_b$, let $\rho_h := \pi(a_h|s_h)/\pi_b(a_h|s_h)$ and $\rho_{1:h} := \prod_{h'=1}^h\rho_{h'}$. The per-trajectory IS estimate of $J(\pi)$ is
> $$
> \begin{align}
> \rho_{1:H}\sum_{h=1}^H\gamma^{h-1}r_h.
> \end{align}
> $$
> It is unbiased, because the [[Importance Sampling|importance ratio]] of the trajectory laws is
> $$
> \begin{align}
> \frac{P^\pi(\tau)}{P^{\pi_b}(\tau)} = \frac{d_0(s_1)\pi(a_1|s_1)R(r_1|s_1,a_1)P(s_2|s_1,a_1)\cdots\pi(a_H|s_H)R(r_H|s_H,a_H)}{d_0(s_1)\pi_b(a_1|s_1)R(r_1|s_1,a_1)P(s_2|s_1,a_1)\cdots\pi_b(a_H|s_H)R(r_H|s_H,a_H)} = \rho_{1:H}.
> \end{align}
> $$

# Properties
- The unknown dynamics $d_0, P, R$ cancel, as in the [[Inverse Propensity Score Estimator]]. Only action propensities are needed (Precup, Sutton & Singh 2000).
- **Exponential variance.** With $\pi_b$ uniform over $K$ actions, $\pi$ deterministic, and a nonzero constant reward only at the end, $\rho_{1:H} = K^H\,\mathbb{I}[\text{all actions match}]$, so the variance is proportional to $K^H$. This is unavoidable in the worst case for unbiased [[Off-Policy Evaluation]] (Jiang & Li 2016).
- Improved by [[Per-Step Importance Sampling]], which weights each reward only by the ratios of the actions before it.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 4](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=4)
