---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] REINFORCE[^1]
> For differentiable [[Stochastic Policy|stochastic policies]] $\pi_\theta$, trajectories $\tau = (s_1, a_1, r_1, \dots, s_H, a_H, r_H)$ terminating within $H$ steps, and $R(\tau) = \sum_{h=1}^H\gamma^{h-1}r_h$,
> $$
> \begin{align}
> \nabla_\theta J(\pi_\theta) = \mathbb{E}_{\tau\sim\pi_\theta}\Big[R(\tau)\sum_{h=1}^H\nabla_\theta\log\pi_\theta(a_h|s_h)\Big].
> \end{align}
> $$
> REINFORCE estimates $\nabla_\theta J$ by rolling out $\tau \sim \pi_\theta$ and computing $R(\tau)\sum_h\nabla_\theta\log\pi_\theta(a_h|s_h)$, then takes a [[Stochastic Gradient Descent|stochastic gradient]] step.

# Properties
- **Derivation (log-derivative trick).** $\nabla J = \sum_\tau R(\tau)\nabla P^\pi(\tau) = \sum_\tau R(\tau)P^\pi(\tau)\nabla\log P^\pi(\tau)$, and
$$
\begin{align}
\log P^\pi(\tau) = \log d_0(s_1) + \sum_{h=1}^H\log\pi(a_h|s_h) + \sum_{h=1}^{H-1}\log P(s_{h+1}|s_h, a_h).
\end{align}
$$
  Only the policy terms depend on $\theta$, so the unknown dynamics drop out. The accuracy does not depend on $|\mathcal{S}|$.
- **Per-step version.** From the [[Policy Gradient Theorem]]: roll out $\tau \sim \pi$, draw a step $h$ with probability $(1-\gamma)\gamma^{h-1}$, and output $\nabla\log\pi(a_h|s_h)\sum_{t\geq h}\gamma^{t-h}r_t$. Its expectation is $(1-\gamma)\nabla J$ (the source says $\propto \gamma^h$, which is the same distribution), up to truncation at $H$. This has lower variance, as [[Per-Step Importance Sampling]] does compared with [[Per-Trajectory Importance Sampling]].
- **Relation to importance sampling.** The derivation mirrors per-trajectory IS. Conceptually, policy gradient uses IS to evaluate all policies in a small neighborhood of $\pi$ and differentiates those evaluations.
- A score-function (likelihood-ratio) gradient estimator, the alternative to pathwise gradients via the [[Reparameterization Trick]]. Its variance is reduced by baselines ([[Control Variates]]) and critics ([[Actor-Critic]]).

# Questions
> [!question]- Why do the transition dynamics disappear from the REINFORCE gradient, and what does that buy?
> $\nabla_\theta\log P^{\pi_\theta}(\tau)$ is a sum of log-factors, and $d_0$ and $P$ don't depend on $\theta$, so their gradients vanish, leaving $\sum_h\nabla\log\pi_\theta(a_h|s_h)$. The estimator needs only sampled trajectories and the policy's own score, with no model of $P$ or $R$. Its accuracy depends on the policy class and variance, not on $|\mathcal{S}|$.

> [!question]- Application (CS 598 Differentiable MC): compare REINFORCE with a pathwise (reparameterized) gradient of $J$. What does each require, and where does each struggle?
> REINFORCE differentiates the sampling density: it needs only $\nabla\log\pi_\theta$, and allows unknown, non-differentiable dynamics and discontinuous rewards. Its variance scales with $|R(\tau)|$ times a sum of $H$ score terms, which baselines/control variates mitigate. A pathwise gradient writes $a_h = g_\theta(s_h, \xi_h)$ and differentiates $R$ through the dynamics, so it needs a differentiable simulator and reward. It typically has lower variance for smooth integrands, but it is biased when the integrand has $\theta$-dependent discontinuities unless boundary terms are handled ([[Reparameterization (Differentiable Monte Carlo)]], edge sampling).

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 6–7](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=6)
