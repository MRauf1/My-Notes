---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Approximate Bisimulation Abstract Model Loss Bound[^1]
> Let $\phi$ be an $(\epsilon_R, \epsilon_P)$-approximate [[Model-Irrelevant Abstraction|model-irrelevant abstraction]] of $M$ (rewards in $[0, R_{max}]$), and let $M_\phi$ be an [[Abstract Model (State Abstraction)|abstract model]] with arbitrary weights $\{p_x\}$. Then the lifted optimal policy of $M_\phi$ satisfies
> $$
> \begin{align}
> \left\|V^\star_M - V^{[\pi^\star_{M_\phi}]_M}_M\right\|_\infty \leq \frac{2\epsilon_R}{1-\gamma} + \frac{\gamma\,\epsilon_P\,R_{max}}{(1-\gamma)^2}.
> \end{align}
> $$

# Properties
- **Step 1 (evaluation error of abstract policies).** For any abstract policy $\pi : \mathcal{S}_\phi \to \mathcal{A}$,
$$
\begin{align}
\left\|[V^\pi_{M_\phi}]_M - V^{[\pi]_M}_M\right\|_\infty \leq \frac{\epsilon_R}{1-\gamma} + \frac{\gamma\,\epsilon_P\,R_{max}}{2(1-\gamma)^2}.
\end{align}
$$
  Proof: the contraction of the state-value [[Bellman Evaluation Operator]] $\mathcal{T}^{[\pi]_M}$ gives a factor $\frac{1}{1-\gamma}$ times $\|[\mathcal{T}^\pi_{M_\phi}V^\pi_{M_\phi}]_M - \mathcal{T}^{[\pi]_M}[V^\pi_{M_\phi}]_M\|_\infty$. Bound each entry by $\epsilon_R + \frac{\gamma\epsilon_P R_{max}}{2(1-\gamma)}$, as in the [[Simulation Lemma]], collapsing $P$ with $\Phi$ because $[V^\pi_{M_\phi}]_M$ is piecewise constant.
- **Step 2 (decision loss).** For any $s$,
$$
\begin{align}
V^\star_M(s) - V^{[\pi^\star_{M_\phi}]_M}_M(s) = V^\star_M(s) - V^\star_{M_\phi}(\phi(s)) + V^\star_{M_\phi}(\phi(s)) - V^{[\pi^\star_{M_\phi}]_M}_M(s) \leq \|Q^\star_M - [Q^\star_{M_\phi}]_M\|_\infty + \|[V^{\pi^\star_{M_\phi}}_{M_\phi}]_M - V^{[\pi^\star_{M_\phi}]_M}_M\|_\infty.
\end{align}
$$
  The first term is bounded by claim (1) of the [[State Abstraction Hierarchy Theorem]], the second by Step 1 (since $\pi^\star_{M_\phi}$ is an abstract policy). Each is at most $\frac{\epsilon_R}{1-\gamma} + \frac{\gamma\epsilon_P R_{max}}{2(1-\gamma)^2}$.
- Tighter by a horizon factor than chaining both claims of the hierarchy theorem, which gives $\frac{2\epsilon_R}{(1-\gamma)^2} + \frac{\gamma\epsilon_P R_{max}}{(1-\gamma)^3}$.

# Questions
> [!question]- Why can't Step 1 simply be combined with the [[Evaluation Error to Decision Loss Lemma]] ("underestimate $\pi^\star_M$, overestimate $\pi^\star_{M_\phi}$")?
> That lemma needs the evaluation error bound for *both* $\pi^\star_M$ and $\pi^\star_{M_\phi}$ as policies evaluated in both models. Step 1 only covers lifted abstract policies. When $\phi$ is not an exact bisimulation, $\pi^\star_M$ need not be constant on the classes of $\phi$, so it is not of the form $[\pi]_M$ and has no counterpart in $M_\phi$. The proof instead compares $V^\star_M$ with $V^\star_{M_\phi}$ through $Q^\star$ (hierarchy theorem, claim 1).

> [!question]- Where does the improvement over chaining the two hierarchy claims come from?
> Chaining converts the $Q^\star$ error $\epsilon_{Q^\star}$ into decision loss through the greedy-policy bound, which multiplies by $\frac{2}{1-\gamma}$. The direct proof never takes a greedy step with respect to an approximate $Q$. It bounds the loss as a sum of two value-function errors, each of the same order as $\epsilon_{Q^\star}$, so it pays $2\epsilon_{Q^\star}$ instead of $\frac{2\epsilon_{Q^\star}}{1-\gamma}$.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 7–8](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=7)
