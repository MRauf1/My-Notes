---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Bellman Residual Telescoping Identity[^1]
> For any $f \in \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$, any initial distribution $d_0 \in \Delta(\mathcal{S})$, and any [[Policy|policy]] $\pi$, let $J(\pi) = \mathbb{E}_{s\sim d_0}[V^\pi(s)]$ be the [[Expected Return (Markov Decision Process)|expected return]] and let $d^\pi \in \Delta(\mathcal{S}\times\mathcal{A})$ be the normalized discounted [[State-Action Occupancy|state-action occupancy]] of $\pi$ from $d_0$. Then
> $$
> \begin{align}
> \mathbb{E}_{s\sim d_0, a\sim\pi}[f(s,a)] - J(\pi) &= \frac{1}{1-\gamma}\mathbb{E}_{(s,a)\sim d^\pi}\big[f - \mathcal{T}^\pi f\big] \\
> &= \frac{1}{1-\gamma}\mathbb{E}_{(s,a)\sim d^\pi,\, r\sim R(s,a),\, s'\sim P(\cdot|s,a)}\big[f(s,a) - r - \gamma f(s', \pi)\big],
> \end{align}
> $$
> where $\mathcal{T}^\pi$ is the [[Bellman Evaluation Operator]].

# Properties
- **Proof.** The first line follows from the second by marginalizing out $r$ and $s'$. Since $J(\pi) = \frac{1}{1-\gamma}\mathbb{E}_{d^\pi, r}[r]$, the reward terms cancel, leaving
$$
\begin{align}
\frac{1}{1-\gamma}\mathbb{E}_{d^\pi, s'}[f(s,a) - \gamma f(s', \pi)] = \sum_{t=1}^\infty \gamma^{t-1}\mathbb{E}_{(s,a)\sim d^\pi_t,\, s'\sim P(\cdot|s,a),\, a'\sim\pi(\cdot|s')}[f(s,a) - \gamma f(s', a')].
\end{align}
$$
  Here $d^\pi_t$ is the law of $(s_t, a_t)$. The $-\gamma f(s',a')$ term at step $t$ cancels the $f(s,a)$ term at step $t+1$, since $(s', a') \sim d^\pi_{t+1}$. Only $\mathbb{E}_{d^\pi_1}[f] = \mathbb{E}_{s\sim d_0, a\sim\pi}[f(s,a)]$ survives.
- It is the [[Bellman Flow Equations]] for $d^\pi$, written with $f$ as a "test function" or discriminator.
- With $f = Q^\pi_{\widehat{M}}$, it gives the alternative proof of the [[Simulation Lemma]]. Applied twice, it gives the [[Bellman Error Performance Difference Bound]].
- Compare the [[Performance Difference Lemma]], which also measures a value gap through an expectation under an occupancy.

# Questions
> [!question]- What is the proof idea of the identity?
> Expand $\frac{1}{1-\gamma}\mathbb{E}_{d^\pi}$ as $\sum_t \gamma^{t-1}\mathbb{E}_{d^\pi_t}$. The rewards reproduce $J(\pi)$. For the $f$ terms, $\gamma^{t-1}\cdot\gamma f(s_{t+1}, a_{t+1})$ at step $t$ equals $\gamma^{t}f(s_{t+1}, a_{t+1})$, the $f$ term of step $t+1$ with opposite sign, because $(s_{t+1}, a_{t+1}) \sim d^\pi_{t+1}$ under $\pi$. The sum telescopes to the $t = 1$ term $\mathbb{E}_{d_0, \pi}[f]$.

> [!question]- What does the identity say when $f = Q^\pi$, and why is it called a test-function form of the Bellman flow equations?
> For $f = Q^\pi$, $f - \mathcal{T}^\pi f = 0$ and $\mathbb{E}_{d_0,\pi}[Q^\pi] = J(\pi)$, so both sides vanish. In general the identity holds for *every* $f$ exactly because $d^\pi$ satisfies the flow constraint $\sum_a d^\pi(s,a) = (1-\gamma)d_0(s) + \gamma\sum_{\tilde{s},\tilde{a}} P(s|\tilde{s},\tilde{a})d^\pi(\tilde{s},\tilde{a})$, paired against $f(s,\pi)$. Testing against all $f$ is equivalent to the flow equations, as with a weak formulation.

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 3](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=3)
