---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Fitted Q-Iteration[^1]
> Let $M = (\mathcal{S}, \mathcal{A}, P, R, \gamma, d_0)$ be a [[Markov Decision Process]], $\mathcal{F} \subset \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ a Q-function class, and $D = \{(s,a,r,s')\}$ a batch dataset with $(s,a) \sim \mu$, $r \sim R(s,a)$, $s' \sim P(s,a)$. Define the squared loss and the empirical Bellman update
> $$
> \begin{align}
> \mathcal{L}_D(f; f') &:= \frac{1}{|D|}\sum_{(s,a,r,s') \in D}\big(f(s,a) - r - \gamma V_{f'}(s')\big)^2, \qquad V_{f'}(s') := \max_{a'} f'(s', a'), \\
> \widehat{\mathcal{T}}_{\mathcal{F}}f' &:= \arg\min_{f \in \mathcal{F}}\mathcal{L}_D(f; f').
> \end{align}
> $$
> Fitted Q-Iteration (FQI) starts from $f_0 \equiv 0$ and iterates $f_k := \widehat{\mathcal{T}}_{\mathcal{F}}f_{k-1}$, outputting the [[Greedy Policy]] $\pi_{f_k}$.

# Properties
- **Sample-based [[Value Iteration]].** Each step replaces $f_k = \mathcal{T}f_{k-1}$ by a least-squares regression ([[Empirical Risk Minimization]]) of the target $r + \gamma V_{f_{k-1}}(s')$ onto $\mathcal{F}$. Its population version is $\mathcal{L}_\mu(f; f') := \mathbb{E}_D[\mathcal{L}_D(f; f')]$.
- **Why it works.** The [[Regression Function|Bayes-optimal regressor]] of the target is $\mathcal{T}f'$. Under [[Bellman Completeness]] it lies in $\mathcal{F}$, so $\mathcal{L}_\mu(f; f') - \mathcal{L}_\mu(\mathcal{T}f'; f') = \|f - \mathcal{T}f'\|_\mu^2$, and the regression error controls the per-step Bellman update error.
- A batch (offline) [[Value-Based Reinforcement Learning|value-based]] method: it uses only $D$, never interacts with $M$.
- Guarantees: [[Fitted Q-Iteration Error Bound]] (with [[Concentrability Coefficient|concentrable]] data), sharpened by the [[Fitted Q-Iteration Fast Rate]]. Outputting a non-stationary policy instead gives [[Non-Stationary Fitted Q-Iteration]].

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), pp. 1–2](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=1)
