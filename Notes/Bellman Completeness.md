---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Completeness[^1]
> A function class $\mathcal{F} \subset \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ is Bellman complete (closed under the [[Bellman Optimality Operator]] $\mathcal{T}$) if
> $$
> \begin{align}
> \forall f \in \mathcal{F}: \quad \mathcal{T}f \in \mathcal{F}.
> \end{align}
> $$
> The analogous condition for policy evaluation replaces $\mathcal{T}$ by the [[Bellman Evaluation Operator]] $\mathcal{T}^\pi$.

# Properties
- **Implies realizability for finite $\mathcal{F}$**: completeness gives [[Realizability (Reinforcement Learning)|realizability]] $Q^\star \in \mathcal{F}$. The converse fails.
- **Role in regression-based RL.** For data $(s,a) \sim \mu$, $r \sim R(s,a)$, $s' \sim P(s,a)$ and any $f'$, the [[Regression Function|Bayes-optimal regressor]] of the target $r + \gamma V_{f'}(s')$ on $(s,a)$ is $\mathbb{E}[r + \gamma V_{f'}(s') \mid s,a] = (\mathcal{T}f')(s,a)$. Completeness says this regressor lies in $\mathcal{F}$, so every squared-loss regression step of [[Fitted Q-Iteration]] is well specified. It is the key assumption of the [[Fitted Q-Iteration Error Bound]].
- Unlike realizability, completeness is **not monotone** in $\mathcal{F}$: enlarging $\mathcal{F}$ can break it, since new members $f$ bring new requirements $\mathcal{T}f \in \mathcal{F}$.
- **Examples.** The tabular class $\mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ is complete. The class of functions piecewise constant on the blocks of a [[Model-Irrelevant Abstraction|bisimulation]] $\phi$ is complete: within a block, $R(s,a)$ and $\sum_{x'}(\Phi P(s,a))(x')V_f(x')$ coincide because $V_f$ is constant on blocks. A linear class $\{\Phi w\}$ is complete for $\mathcal{T}^\pi$ iff $R^\pi \in \operatorname{span}\Phi$ and $\operatorname{span}\Phi$ is invariant under $P^\pi$.

# Questions
> [!question]- Why does Bellman completeness imply realizability when $\mathcal{F}$ is finite?
> Take any $f_0 \in \mathcal{F}$ and set $f_k = \mathcal{T}^k f_0$. By completeness all $f_k \in \mathcal{F}$, and by the $\gamma$-contraction of $\mathcal{T}$ in $\|\cdot\|_\infty$, $f_k \to Q^\star$. A sequence in a finite set takes some value $g$ infinitely often, so $g$ is the limit of a subsequence, i.e. $g = Q^\star \in \mathcal{F}$. (For infinite $\mathcal{F}$, one needs $\mathcal{F}$ closed instead.)

> [!question]- Give a class that is realizable but not Bellman complete.
> $\mathcal{F} = \{Q^\star, 0\}$ in any MDP with $R \neq 0$ and $R \neq Q^\star$ (e.g. $\gamma > 0$ and reward reachable after the first step). Then $\mathcal{T}0 = R \notin \mathcal{F}$. Realizability alone constrains one function; completeness constrains the image of every member.

> [!question]- Application: in the CS 542 LSTD project, when is $\operatorname{span}\{\phi_1, \dots, \phi_K\}$ of graph-Laplacian eigenvectors Bellman complete for $\mathcal{T}^\pi$?
> Completeness for $\mathcal{T}^\pi$ needs $R^\pi \in \operatorname{span}\Phi$ and $P^\pi\operatorname{span}\Phi \subseteq \operatorname{span}\Phi$. If $P^\pi$ commutes with the (symmetric) Laplacian, $P^\pi$ maps each Laplacian eigenspace into itself, so the span of the bottom $K$ eigenvectors is invariant provided the cutoff $K$ doesn't split an eigenspace. This is the commutation criterion: $[P^\pi, \Delta] = 0$ makes $\Phi^{-1}P^\pi\Phi$ block-diagonal. When they don't commute, the off-diagonal block of $P^\pi$ (from $\operatorname{span}\Phi$ into its complement) measures how far completeness fails.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), p. 1](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=1)
