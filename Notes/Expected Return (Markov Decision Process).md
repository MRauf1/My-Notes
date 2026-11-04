---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Expected Return (Markov Decision Process)[^1]
> For a [[Markov Decision Process]] $M = (\mathcal{S}, \mathcal{A}, P, R, \gamma, d_0)$ with initial-state distribution $d_0 \in \Delta(\mathcal{S})$ and a [[Policy]] $\pi$, the expected return of $\pi$ is the scalar
> $$
> \begin{align}
> J(\pi) := \mathbb{E}_{s \sim d_0}\big[V^\pi(s)\big] = \mathbb{E}\left[\sum_{t=1}^{\infty} \gamma^{t-1} r_t \,\middle|\, s_1 \sim d_0,\ \pi\right],
> \end{align}
> $$
> the expected [[Discounted Return]] of running $\pi$ from a random start state.

# Properties
- **Scalar objective.** The [[Value Function]] $V^\pi$ is a vector with one score per start state, and two policies' value functions need not be comparable. $J(\pi)$ averages $V^\pi$ over $d_0$, so any two policies, including non-stationary ones, can be ranked. This is the objective in the [[Performance Difference Lemma]], the [[Bellman Error Performance Difference Bound]], and the analyses of [[Fitted Q-Iteration]].
- **Equivalent forms.** Let $d^\pi_t$ be the distribution of $(s_t, a_t)$ under $\pi$ from $d_0$, and $d^\pi = (1-\gamma)\sum_{t\geq1}\gamma^{t-1}d^\pi_t$ the normalized discounted [[State-Action Occupancy]]. Then
  $$
  \begin{align}
  J(\pi) = \mathbb{E}_{(s,a)\sim d^\pi_1}\big[Q^\pi(s,a)\big] = \sum_{t=1}^{\infty}\gamma^{t-1}\,\mathbb{E}_{(s,a)\sim d^\pi_t}\big[R(s,a)\big] = \frac{1}{1-\gamma}\,\mathbb{E}_{(s,a)\sim d^\pi}\big[R(s,a)\big],
  \end{align}
  $$
  where $d^\pi_1 = d_0 \times \pi_1$. The first form averages $V^\pi(s) = Q^\pi(s,\pi)$ over $d_0$, the second is linearity of expectation, and the third rescales by the normalization of $d^\pi$.
- **Recovering $V^\pi$.** With $d_0 = \delta_s$, a point mass at $s$, $J(\pi) = V^\pi(s)$. So a bound on $J(\pi) - J(\pi')$ that holds for every $d_0$ holds at every state, and hence in $\|\cdot\|_\infty$.
- **Range.** $J(\pi) \in [0, V_{\max}]$ with $V_{\max} = R_{\max}/(1-\gamma)$, since rewards lie in $[0, R_{\max}]$. Splitting at step $K$, $J(\pi) = \sum_{t=1}^{K}\gamma^{t-1}\mathbb{E}_{d^\pi_t}[r_t] + \mathbb{E}\big[\sum_{t>K}\gamma^{t-1}r_t\big]$, and the tail lies in $[0, \gamma^K V_{\max}]$ (cf. [[Truncated Value Function]]).
- Comparing $\mathbb{E}_{s\sim d_0, a\sim\pi}[f(s,a)]$ with $J(\pi)$ for an arbitrary $f$ gives the [[Bellman Residual Telescoping Identity]].

# Questions
> [!question]- Why does $J(\pi) = \frac{1}{1-\gamma}\mathbb{E}_{(s,a)\sim d^\pi}[R(s,a)]$, and how should it be read?
> By linearity, $J(\pi) = \sum_{t\geq1}\gamma^{t-1}\mathbb{E}_{d^\pi_t}[R(s,a)] = \mathbb{E}_{\sum_t \gamma^{t-1}d^\pi_t}[R]$, and $\sum_t \gamma^{t-1}d^\pi_t = \frac{1}{1-\gamma}d^\pi$ by the definition of the normalized occupancy. Read it as: return = (average reward under the discounted occupancy) × (effective horizon $\frac{1}{1-\gamma}$).

> [!question]- Why do performance bounds stated for $J$ with an arbitrary $d_0$ imply bounds in $\|\cdot\|_\infty$ on value functions?
> Taking $d_0 = \delta_s$ makes $J(\pi) = V^\pi(s)$. A bound valid for every $d_0$ therefore holds at every state $s$, and taking the maximum over $s$ gives the $\|\cdot\|_\infty$ bound. For example, the [[Bellman Error Performance Difference Bound]] gives $\|V^\star - V^{\pi_f}\|_\infty \leq \frac{2}{1-\gamma}\|f - \mathcal{T}f\|_\infty$.

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 3](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=3)
