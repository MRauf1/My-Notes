---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Variance Recursion of Per-Step Importance Sampling[^1]
> Let $v_{H-h+1} = \rho_h(r_h + \gamma v_{H-h})$ be the recursive [[Per-Step Importance Sampling]] estimator, with rewards a deterministic function of $(s,a)$. Let $\mathbb{V}_h, \mathbb{E}_h$ denote variance and expectation conditioned on $s_1, a_1, r_1, \dots, s_{h-1}, a_{h-1}, r_{h-1}$. Then
> $$
> \begin{align}
> \mathbb{V}_h[v_{H-h+1}] = \mathbb{V}_h[V^\pi(s_h)] + \mathbb{E}_h\big[\mathbb{V}_h[\rho_h Q^\pi(s_h, a_h) \mid s_h]\big] + \gamma^2\,\mathbb{E}_h\big[\rho_h^2\,\mathbb{V}_{h+1}[v_{H-h}]\big].
> \end{align}
> $$

> [!abstract] Bellman Equation for Variance[^1]
> On-policy ($\pi_b = \pi$) with $\pi$ deterministic, $\rho_h \equiv 1$ and the middle term vanishes:
> $$
> \begin{align}
> \mathbb{V}_h[v_{H-h+1}] = \mathbb{V}_h[V^\pi(s_h)] + \gamma^2\,\mathbb{E}_h\big[\mathbb{V}_{h+1}[v_{H-h}]\big].
> \end{align}
> $$
> Unrolling, the variance of the Monte Carlo return $v_H = \sum_h\gamma^{h-1}r_h$ is
> $$
> \begin{align}
> \mathbb{V}[v_H] = \sum_{h=1}^H\gamma^{2(h-1)}\,\mathbb{E}_{(s_{h-1}, a_{h-1})\sim d^\pi_{h-1}}\Big[\mathbb{V}_{s_h\sim P(s_{h-1}, a_{h-1})}\big[V^\pi(s_h)\big]\Big],
> \end{align}
> $$
> where the $h = 1$ term is $\mathbb{V}_{s_1\sim d_0}[V^\pi(s_1)]$.

# Properties
- It looks like the [[Bellman Equation (Policy Evaluation)]], with the "reward" replaced by the one-step conditional variance of $V^\pi$ and the discount squared.
- **Derivation.** Write $v_{H-h+1} = \rho_h Q^\pi(s_h, a_h) + \rho_h(r_h + \gamma v_{H-h} - Q^\pi(s_h, a_h))$. The cross term has zero conditional mean. Then split $\rho_h Q^\pi(s_h, a_h)$ around its conditional mean $V^\pi(s_h)$, using the [[Law of Total Variance]] at each step.
- **Pattern.** For each random variable $s_h$ in turn: (1) condition on everything up to $s_h$, giving $V^\pi(s_h)$; (2) take its variance with respect to the local randomness of $s_h$ given the past; (3) average over the past.
- **Total variance is not $H$ times the worst case.** A single $(s,a)$ can have $\mathbb{V}_{s'\sim P(s,a)}[V^\pi(s')] = \Theta(V_{max}^2)$, but the sum along $d^\pi$ equals the variance of a return in $[0, V_{max}]$, hence is $O(V_{max}^2)$, not $\Theta(HV_{max}^2)$. Hoeffding-based tabular analyses implicitly assume worst-case variance at every transition. Tight sample-complexity bounds use [[Bernstein's Inequality]] with this total-variance identity (Lattimore & Hutter 2012; Azar, Munos & Kappen 2013). See [[Certainty-Equivalence Sample Complexity]].

# Questions
> [!question]- Why does the on-policy variance recursion imply $\sum_h\gamma^{2(h-1)}\mathbb{E}_{d^\pi_{h-1}}[\mathbb{V}_{P}[V^\pi(s_h)]] = O(V_{max}^2)$, even though each term can be $\Theta(V_{max}^2)$?
> The unrolled identity says the weighted sum of one-step conditional variances equals $\mathbb{V}[v_H]$, the variance of the Monte Carlo return. The return lies in $[0, V_{max}]$, so its variance is at most $V_{max}^2/4$. Large one-step variances can therefore only occur on a small fraction of the occupancy, not at every step.

> [!question]- Where does the middle term $\mathbb{E}_h[\mathbb{V}_h[\rho_h Q^\pi(s_h,a_h) \mid s_h]]$ come from, and when does it vanish?
> It is the variance from the random action $a_h \sim \pi_b(\cdot|s_h)$, inflated by the importance weight. Given $s_h$, $\rho_h Q^\pi(s_h, a_h)$ has mean $V^\pi(s_h)$, and its spread around it is this term. It vanishes when $\rho_h Q^\pi(s_h, a_h)$ is constant given $s_h$, e.g. on-policy with a deterministic policy ($\rho_h = 1$, $a_h$ determined by $s_h$). On-policy with a stochastic policy, it remains as $\mathbb{V}_{a\sim\pi}[Q^\pi(s_h, a)]$.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 5–6](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=5)
