---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Policy Gradient Theorem[^1]
> Let $\{\pi_\theta : \theta \in \Theta\}$ be [[Stochastic Policy|stochastic policies]] with $\pi_\theta(a|s)$ differentiable in $\theta$ for all $(s,a)$, and let $d^\pi \in \Delta(\mathcal{S}\times\mathcal{A})$ be the normalized discounted [[State-Action Occupancy|state-action occupancy]] of $\pi = \pi_\theta$ from $d_0$. Then
> $$
> \begin{align}
> \nabla_\theta J(\pi) = \frac{1}{1-\gamma}\,\mathbb{E}_{(s,a)\sim d^\pi}\big[\nabla_\theta\log\pi(a|s)\,Q^\pi(s,a)\big].
> \end{align}
> $$
> For any $f : \mathcal{S} \to \mathbb{R}$ (a **baseline**), also
> $$
> \begin{align}
> \nabla_\theta J(\pi) = \frac{1}{1-\gamma}\,\mathbb{E}_{(s,a)\sim d^\pi}\big[\nabla_\theta\log\pi(a|s)\,(Q^\pi(s,a) - f(s))\big].
> \end{align}
> $$

# Properties
- **Proof (Sutton et al. 1999).** Differentiate $V^\pi(s) = \sum_a\pi(a|s)Q^\pi(s,a)$, using $\nabla\pi = \pi\nabla\log\pi$ and $\nabla Q^\pi(s,a) = \gamma\,\mathbb{E}_{s'\sim P(s,a)}[\nabla V^\pi(s')]$ (the reward does not depend on $\theta$):
$$
\begin{align}
\nabla V^\pi(s) = \sum_a\pi(a|s)\Big(\nabla\log\pi(a|s)\,Q^\pi(s,a) + \gamma\,\mathbb{E}_{s'\sim P(s,a)}[\nabla V^\pi(s')]\Big).
\end{align}
$$
  Average over $s \sim d^\pi_t$ and unroll: $\nabla\mathbb{E}_{d^\pi_t}[V^\pi] = \sum_{t'\geq t}\gamma^{t'-t}\,\mathbb{E}_{d^\pi_{t'}}[\nabla\log\pi\,Q^\pi]$. At $t = 1$ the left side is $\nabla J(\pi)$, and $d^\pi = (1-\gamma)\sum_{t'}\gamma^{t'-1}d^\pi_{t'}$.
- **Baseline.** $\mathbb{E}_{a\sim\pi(s)}[\nabla\log\pi(a|s)] = \sum_a\nabla\pi(a|s) = \nabla\sum_a\pi(a|s) = 0$, the RL instance of [[Score Function Expectation|zero mean of the score]]. So subtracting any $f(s)$ keeps the gradient unbiased while changing its variance. The usual choice is $f = V^\pi$, giving the [[Advantage Function]] $A^\pi$. A baseline is a [[Control Variates|control variate]].
- Gives the per-step form of [[REINFORCE]]. Replacing $Q^\pi$ by a learned estimate gives [[Actor-Critic]] methods.
- Compare the [[Performance Difference Lemma]]: both are expectations under an occupancy of an advantage-type quantity. The gradient is the first-order version of the performance difference to a nearby policy.

# Questions
> [!question]- What is the proof idea of the policy gradient theorem?
> Differentiate the Bellman identity $V^\pi = \sum_a\pi Q^\pi$. The product rule gives a "local" term $\sum_a\nabla\pi\,Q^\pi = \mathbb{E}_{a\sim\pi}[\nabla\log\pi\,Q^\pi]$ and a "future" term $\gamma\,\mathbb{E}[\nabla V^\pi(s')]$, because only the future values depend on $\theta$ through $Q^\pi$. The future term has the same form one step later, so unrolling along the per-step distributions $d^\pi_t$ sums the local terms with weights $\gamma^{t-1}$, which is $\frac{1}{1-\gamma}$ times the expectation under $d^\pi$.

> [!question]- Which state-dependent baseline $b(s)$ minimizes $\mathbb{E}_{a\sim\pi(s)}\big[\|\nabla\log\pi(a|s)\,(Q^\pi(s,a) - b(s))\|^2\big]$ at a fixed $s$?
> Since the mean $\mathbb{E}_a[\nabla\log\pi\,(Q^\pi - b)]$ does not depend on $b$, minimizing the second moment minimizes the (trace of the) variance. Setting the derivative in $b$ to zero gives $\mathbb{E}_a[\|\nabla\log\pi\|^2(Q^\pi - b)] = 0$, so $b^\star(s) = \frac{\mathbb{E}_a[\|\nabla\log\pi(a|s)\|^2\,Q^\pi(s,a)]}{\mathbb{E}_a[\|\nabla\log\pi(a|s)\|^2]}$. This is a score-weighted average of $Q^\pi$, and equals $V^\pi(s)$ only when the score norm is constant in $a$.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 7–8](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=7)
