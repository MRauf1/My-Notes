---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Latin Hypercube Sampling[^1]
> To draw $N$ samples in $[0,1]^d$, split each axis into $N$ equal intervals and choose independent random permutations $\pi_1, \dots, \pi_d$ of $\{1, \dots, N\}$. The $i$-th sample has coordinates
> $$
> \begin{align}
> X_i^{(j)} = \frac{\pi_j(i) - U_i^{(j)}}{N}, \qquad U_i^{(j)} \sim \mathcal{U}[0,1] \text{ i.i.d.}, \quad j = 1, \dots, d
> \end{align}
> $$
> so that every one of the $N$ intervals of every axis contains exactly one sample.

# Properties
- Stratifies every one-dimensional marginal with only $N$ samples, whereas full [[Stratified Sampling]] of the $d$-dimensional cube with $k$ strata per axis needs $k^d$ samples — avoiding the [[Curse of Dimensionality]].
- Removes the variance contributed by the additive (main-effect) part of the integrand; it does not stratify interactions between coordinates.
- Unbiased, and its variance never exceeds that of $N$ i.i.d. samples by more than a factor $N/(N-1)$.

[^1]: Monte Carlo Methods — Q&A Overview
