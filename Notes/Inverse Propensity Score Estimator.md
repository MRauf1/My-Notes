---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Inverse Propensity Score Estimator[^1]
> In a [[Contextual Bandit]] with logged data $x \sim d_0$, $a \sim \pi_b(\cdot|x)$, $r \sim R(x,a)$, and a target policy $\pi$ supported on $\pi_b$, the inverse propensity score (IPS) estimate of $J(\pi)$ from one sample is
> $$
> \begin{align}
> \rho\, r, \qquad \rho = \frac{\pi(a|x)}{\pi_b(a|x)}.
> \end{align}
> $$
> It is unbiased, because the [[Importance Sampling|importance ratio]] of the joint laws of $(x,a,r)$ is $\frac{d_0(x)\pi(a|x)R(r|x,a)}{d_0(x)\pi_b(a|x)R(r|x,a)} = \rho$.

# Properties
- The unknown $d_0$ and $R$ cancel in the ratio, since they don't change when a different policy is deployed. Only the behavior propensities $\pi_b(a|x)$ must be known.
- **Variance.** With $\pi_b$ uniform over $K = |\mathcal{A}|$ actions and $\pi$ deterministic, $\rho = K\,\mathbb{I}[a = \pi(x)]$. For a constant reward $r$ (where on-policy Monte Carlo has zero variance),
$$
\begin{align}
\mathbb{V}[\rho r] = r^2(\mathbb{E}[\rho^2] - 1) = r^2(K - 1),
\end{align}
$$
  and for $r \in [0,1]$ in general, $\mathbb{V}[\rho r] \leq \mathbb{E}[\rho^2] = K$. Only a $1/K$ fraction of the data matches $\pi$, so the effective sample size is $K$ times smaller.
- **Concentration.** $\rho r \in [0, K]$ but $\mathbb{V}[\rho r] \leq K$: the variance is of the order of the range, not its square. [[Hoeffding's Inequality]] gives deviation $K\sqrt{\frac{1}{2n}\ln\frac{2}{\delta}}$. [[Bernstein's Inequality]] gives
$$
\begin{align}
\sqrt{\frac{2K}{n}\ln\frac{2}{\delta}} + \frac{2K}{3n}\ln\frac{2}{\delta} = O\Big(\sqrt{\tfrac{K}{n}\ln\tfrac{1}{\delta}}\Big),
\end{align}
$$
  which saves a factor $\sqrt{K}$.
- **Variance reduction.** Normalize by $\sum_i\rho_i$ ([[Self-Normalized Importance Sampling]]), or subtract a baseline. Running IPS on $r - c$ and adding $c$ back has variance $(r-c)^2(K-1)$ in the constant-reward case, which is $0$ for $c = r$. Generalizing the baseline to a reward model gives the [[Doubly Robust Estimator]].
- IPS is the one-step building block of [[Per-Step Importance Sampling]].

# Questions
> [!question]- Why is $\mathbb{V}[\rho r] = r^2(K-1)$ for a constant reward, uniform $\pi_b$, and deterministic $\pi$, and what does it say about effective sample size?
> $\rho = K\,\mathbb{I}[a = \pi(x)]$ with $P(a = \pi(x)) = 1/K$, so $\mathbb{E}[\rho] = 1$ and $\mathbb{E}[\rho^2] = K^2/K = K$, hence $\mathbb{V}[\rho r] = r^2(K - 1)$. IPS effectively keeps only the $\approx n/K$ matching samples, so averaging $n$ samples behaves like $n/K$ on-policy samples. And because it divides by $n/K$ rather than the realized count, the count's randomness shows up as variance even for constant rewards.

> [!question]- Why does Bernstein give a $\sqrt{K}$ better deviation bound than Hoeffding for IPS?
> Hoeffding uses only the range $[0, K]$, so its deviation scales with $K/\sqrt{n}$. Bernstein's leading term is $\sqrt{2\sigma^2\ln(2/\delta)/n}$ with $\sigma^2 \leq \mathbb{E}[\rho^2 r^2] \leq K$, i.e. $\sqrt{K/n}$. The range $K$ enters only the lower-order $K/n$ term. A variable that is large only with small probability has variance much smaller than its range squared.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 1–3](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=1)
