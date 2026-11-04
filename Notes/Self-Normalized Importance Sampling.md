---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Self-Normalized Importance Sampling[^1]
> Given $x_1, \dots, x_n \sim q$ i.i.d. with importance weights $\rho_i = p(x_i)/q(x_i)$, the self-normalized (weighted) importance sampling estimate of $\mathbb{E}_p[f]$ is
> $$
> \begin{align}
> \frac{\sum_{i=1}^n \rho_i f(x_i)}{\sum_{i=1}^n \rho_i},
> \end{align}
> $$
> i.e. [[Importance Sampling]] normalized by the realized total weight instead of its expectation $n$. In RL it is called weighted importance sampling (WIS).

# Properties
- **Biased but consistent.** It is a [[Ratio Estimator]] of $\mathbb{E}_q[\rho f]/\mathbb{E}_q[\rho]$, and $\mathbb{E}_q[\rho] = 1$. It can even divide by zero when all $\rho_i = 0$ (e.g. no logged action matches the target policy). Since $\frac{1}{n}\sum_i\rho_i \to 1$, it is consistent.
- Only needs $p$ and $q$ up to normalizing constants, since these cancel in the ratio.
- **Why it reduces variance.** With uniform $q$ over $K$ actions and deterministic target $p$, plain IS sums the rewards of the matching subsample but divides by the *expected* size $n/K$. Its variance for a constant reward comes entirely from the random subsample size. WIS divides by the realized size, so it has zero variance in that case.
- Extends to multi-step [[Off-Policy Evaluation]]: weighted [[Per-Step Importance Sampling]] and weighted [[Doubly Robust Estimator|doubly robust]] estimators (Precup 2000; Thomas & Brunskill 2016).

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 3](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=3)
