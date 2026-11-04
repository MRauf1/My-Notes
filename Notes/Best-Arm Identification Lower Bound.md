---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Best-Arm Identification Lower Bound[^1]
> For any $K \geq 2$, $\epsilon \leq \sqrt{1/8}$, and any [[Multi-Armed Bandit]] algorithm, there exists an MAB instance in which $\mu^\star$ is $\epsilon$ better than every other arm, yet the algorithm identifies the best arm with probability at most $2/3$ unless
> $$
> \begin{align}
> T \geq \frac{K}{72\,\epsilon^2}.
> \end{align}
> $$

# Properties
- Stated for [[Best-Arm Identification]], it is also a lower bound for [[Simple Regret]] minimization: in the hard instance every other arm is $\epsilon$ worse than $\mu^\star$, so missing the best arm costs simple regret at least $\epsilon$.
- Formalizes the intuition that a learner must try each arm: $\Omega(K/\epsilon^2)$ rounds are necessary, matching the $O(\frac{K}{\epsilon^2}\ln\frac{K}{\delta})$ of the [[Uniform Sampling Simple Regret Bound]] up to the logarithmic factor.
- The proof is Theorem 2 of Krishnamurthy, Agarwal & Langford (2016). The source attributes the technique to Auer et al., and says the same technique also proves lower bounds on [[Pseudo-Regret]].

# Questions
> [!question]- Why does a lower bound for best-arm identification also lower bound simple regret?
> In the hard instance, the best arm beats every other arm by $\epsilon$. If the algorithm fails to output the best arm (probability $\geq 1/3$ when $T < \frac{K}{72\epsilon^2}$), its simple regret is at least $\epsilon$. So $\Pr[\mu^\star - \mu_{\hat{i}} \geq \epsilon] \geq 1/3$, and no algorithm can guarantee simple regret below $\epsilon$ with probability above $2/3$ using fewer rounds.

> [!question]- How tight is uniform sampling against this lower bound?
> At constant confidence ($\delta = 1/3$), uniform sampling needs $T = O(\frac{K}{\epsilon^2}\ln K)$, while the lower bound requires $\Omega(\frac{K}{\epsilon^2})$. The linear dependence on $K$ and the $1/\epsilon^2$ dependence are both necessary; only the $\ln K$ factor (from the union bound) is in question.

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 3](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=3)
