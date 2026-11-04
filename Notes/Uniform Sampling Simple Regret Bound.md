---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Uniform Sampling Simple Regret Bound[^1]
> In a [[Multi-Armed Bandit]] with $K$ arms and rewards in $[0, 1]$, let the learner pull each arm $T/K$ times (assume $T/K \in \mathbb{N}$), let $\hat{\mu}_i$ be the empirical mean reward of arm $i$, and output $\hat{i} = \arg\max_{i \in [K]} \hat{\mu}_i$. Then with probability at least $1 - \delta$, the [[Simple Regret]] satisfies
> $$
> \begin{align}
> \mu^\star - \mu_{\hat{i}} \leq 2\sqrt{\frac{K}{2T}\ln\frac{2K}{\delta}}.
> \end{align}
> $$
> Equivalently, $T = O\!\left(\frac{K}{\epsilon^2}\ln\frac{K}{\delta}\right)$ rounds guarantee $\mu^\star - \mu_{\hat{i}} \leq \epsilon$ with probability at least $1 - \delta$.

# Properties
- **Proof outline.**
  1. For each arm, [[Hoeffding's Inequality]] with $T/K$ samples in $[0, 1]$ gives $\Pr[|\hat{\mu}_i - \mu_i| \geq \epsilon] \leq 2e^{-2T\epsilon^2/K}$.
  2. The union bound ([[Boole's Inequality]]) over the $K$ arms gives $\Pr[\exists i : |\hat{\mu}_i - \mu_i| \geq \epsilon] \leq 2Ke^{-2T\epsilon^2/K}$. So with probability $1 - \delta$, $|\hat{\mu}_i - \mu_i| \leq \sqrt{\frac{K}{2T}\ln\frac{2K}{\delta}}$ for all $i$ simultaneously.
  3. With $i^\star = \arg\max_i \mu_i$: $\mu^\star - \mu_{\hat{i}} = \mu_{i^\star} - \hat{\mu}_{i^\star} + \hat{\mu}_{i^\star} - \mu_{\hat{i}} \leq (\mu_{i^\star} - \hat{\mu}_{i^\star}) + (\hat{\mu}_{\hat{i}} - \mu_{\hat{i}})$, using $\hat{\mu}_{i^\star} \leq \hat{\mu}_{\hat{i}}$. Each term is at most the uniform accuracy.
- The algorithm is likely suboptimal: it keeps sampling arms that are clearly bad. The linear dependence on $K$, however, matches the [[Best-Arm Identification Lower Bound]] up to the logarithmic factor.
- A template for analysing learning problems: concentration for each fixed candidate, a union bound for uniform accuracy, then a decision-loss decomposition. The [[Finite Hypothesis Class Generalization Bound]] follows the same steps.

# Questions
> [!question]- Why is the union bound needed? Why not apply Hoeffding's inequality directly to the selected arm $\hat{i}$?
> $\hat{i}$ is chosen *by looking at the data*, so $\hat{\mu}_{\hat{i}}$ is not an average of $T/K$ independent draws from a fixed distribution. The selection biases it upward (the arm with the luckiest sample tends to win). Hoeffding's inequality only holds for a fixed index. Requiring accuracy for every arm simultaneously covers whichever arm is selected, at the cost of $\ln(2K/\delta)$ instead of $\ln(2/\delta)$.

> [!question]- Where does the factor $2$ come from in the bound?
> The decomposition $\mu^\star - \mu_{\hat{i}} \leq (\mu_{i^\star} - \hat{\mu}_{i^\star}) + (\hat{\mu}_{\hat{i}} - \mu_{\hat{i}})$ has two estimation errors, one for the true best arm (underestimated) and one for the chosen arm (overestimated). Each is bounded by the uniform accuracy $\sqrt{\frac{K}{2T}\ln\frac{2K}{\delta}}$.

> [!question]- Convert the high-probability bound into the sample complexity $T = O(\frac{K}{\epsilon^2}\ln\frac{K}{\delta})$.
> Set $2\sqrt{\frac{K}{2T}\ln\frac{2K}{\delta}} \leq \epsilon$, i.e. $T \geq \frac{2K}{\epsilon^2}\ln\frac{2K}{\delta}$, which is $O(\frac{K}{\epsilon^2}\ln\frac{K}{\delta})$.

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), pp. 2–3](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=2)
