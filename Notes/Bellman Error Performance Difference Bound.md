---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Bellman Error Performance Difference Bound[^1]
> For any $f \in \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$, any initial distribution $d_0$, and any [[Policy|policy]] $\pi$,
> $$
> \begin{align}
> J(\pi) - J(\pi_f) \leq \frac{1}{1-\gamma}\Big(\mathbb{E}_{d^\pi}[\mathcal{T}f - f] + \mathbb{E}_{d^{\pi_f}}[f - \mathcal{T}f]\Big),
> \end{align}
> $$
> where $J$ is the [[Expected Return (Markov Decision Process)|expected return]] from $d_0$, $\pi_f$ is the [[Greedy Policy]] of $f$, $\mathcal{T}$ is the [[Bellman Optimality Operator]], $d^\pi$ is the normalized discounted [[State-Action Occupancy]] of $\pi$ from $d_0$, and $\mathbb{E}_\mu[g] := \mathbb{E}_{(s,a)\sim\mu}[g(s,a)]$.

# Properties
- **Proof.** $J(\pi) - J(\pi_f) \leq J(\pi) - \mathbb{E}_{d_0, \pi}[f] + \mathbb{E}_{d_0, \pi_f}[f] - J(\pi_f)$, since $\mathbb{E}_{a\sim\pi}[f(s,a)] \leq \max_a f(s,a) = f(s, \pi_f)$. Apply the [[Bellman Residual Telescoping Identity]] to each pair:
$$
\begin{align}
= \frac{1}{1-\gamma}\mathbb{E}_{d^\pi}[\mathcal{T}^\pi f - f] + \frac{1}{1-\gamma}\mathbb{E}_{d^{\pi_f}}[f - \mathcal{T}^{\pi_f}f].
\end{align}
$$
  Finish with $\mathcal{T}^\pi f \leq \mathcal{T}f$ and $\mathcal{T}^{\pi_f}f = \mathcal{T}f$ ([[Bellman Evaluation Operator]]).
- **Corollary.** $\|V^\star - V^{\pi_f}\|_\infty \leq \frac{2}{1-\gamma}\|f - \mathcal{T}f\|_\infty$ (take $\pi = \pi^\star$ and $d_0$ a point mass). Chaining the [[Bellman Error]] bound $\|f - Q^\star\|_\infty \leq \frac{\|f - \mathcal{T}f\|_\infty}{1-\gamma}$ with the [[Approximate Greedy Policy Suboptimality Bound]] gives only $\frac{2}{(1-\gamma)^2}\|f - \mathcal{T}f\|_\infty$, so this saves a horizon factor.
- *Distribution-dependent*: only the Bellman errors under $d^\pi$ and $d^{\pi_f}$ matter, not the worst case over all $(s,a)$. This is useful for batch/offline analyses.
- For a sequence $f_0, \dots, f_k$ that is only consistent with its predecessor (as in [[Fitted Q-Iteration]]), use the [[Non-Stationary Bellman Error Performance Difference Bound]].
- Used in the large-sample analysis of [[Certainty-Equivalence Sample Complexity]] with $f = Q^\star_{\widehat{M}}$, giving $\|V^\star_M - V^{\pi^\star_{\widehat{M}}}_M\|_\infty \leq \frac{2}{1-\gamma}\|Q^\star_{\widehat{M}} - \mathcal{T}_M Q^\star_{\widehat{M}}\|_\infty$.
- A special case ($\hat{\pi} = \pi_f$) of the [[Performance Difference Bellman Error Decomposition]].

# Questions
> [!question]- What is the proof idea?
> Insert $\mathbb{E}_{d_0,\pi}[f]$ and $\mathbb{E}_{d_0,\pi_f}[f]$; dropping $\mathbb{E}_{d_0,\pi}[f] - \mathbb{E}_{d_0,\pi_f}[f] \leq 0$ (greediness) gives an upper bound. Each remaining difference "value of $f$ at the start minus true return" is converted by the telescoping identity into $\frac{1}{1-\gamma}$ times the expected Bellman residual under that policy's occupancy. Then compare $\mathcal{T}^\pi$ and $\mathcal{T}^{\pi_f}$ with $\mathcal{T}$.

> [!question]- Why does this lemma save a factor $1/(1-\gamma)$ compared with going through $\|f - Q^\star\|_\infty$?
> The two-step route first converts Bellman error into distance to $Q^\star$ (cost $\frac{1}{1-\gamma}$), then converts that into decision loss via the greedy-policy bound (another $\frac{2}{1-\gamma}$). This lemma goes from Bellman error to decision loss in one step: the residual is accumulated once along each occupancy, at cost $\frac{1}{1-\gamma}$ per term.

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 7](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=7)
