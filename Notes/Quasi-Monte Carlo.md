---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Quasi-Monte Carlo[^1]
> Quasi-Monte Carlo replaces the pseudo-random samples of a [[Monte Carlo Estimator]] on $[0,1]^d$ by a deterministic low-discrepancy sequence $x_1, \dots, x_N$ (e.g. Halton or Sobol sequences). Its error obeys the Koksma–Hlawka inequality
> $$
> \begin{align}
> \left|\frac{1}{N}\sum_{i=1}^N f(x_i) - \int_{[0,1]^d} f(x)\,dx\right| \le V_{\mathrm{HK}}(f)\, D_N^*(x_1, \dots, x_N)
> \end{align}
> $$
> where $V_{\mathrm{HK}}(f)$ is the Hardy–Krause variation of $f$ and $D_N^*$ is the star discrepancy of the point set, which is $O\big((\log N)^d / N\big)$ for low-discrepancy sequences.

# Properties
- Converges at nearly $O(N^{-1})$ for integrands of bounded variation, versus the $O(N^{-1/2})$ [[Monte Carlo Convergence Rate]].
- The $(\log N)^d$ factor means the advantage requires smooth integrands and moderate effective dimension; discontinuous integrands (unbounded $V_{\mathrm{HK}}$) lose the bound.
- Deterministic, so it has no variance and no error bars; randomized QMC (e.g. random shifts or scrambling) restores unbiasedness and error estimation.
- Generalizes the evenness of [[Stratified Sampling]] and [[Latin Hypercube Sampling]] to every prefix of the sequence.

[^1]: Monte Carlo Methods — Q&A Overview
