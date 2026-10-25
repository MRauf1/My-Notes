---
tags:
  - computer_science
  - monte_carlo_methods
  - mathematics
  - measure_theory
---

# Definition
> [!info] Borel Measure[^1]
> The measure $\mu_B$ on $\mathbb{R}$ that assigns to the interval $[a,b)$ its length. One-dimensional [[Riemann Integral|Riemann integrals]] are [[Lebesgue Integral (Measure Theory)|Lebesgue integrals]] taken with respect to $\mu_B$.

> [!info] Borel Measure (General Definition)[^2]
> A Borel measure on $\mathbb{R}$ is any [[Measure (Measure Theory)|measure]] whose domain is the [[Borel Sigma-Algebra]] $\mathcal{B}_\mathbb{R}$.

In this general sense, the $\mu_B$ above is one particular Borel measure: [[Lebesgue Measure]] restricted to $\mathcal{B}_\mathbb{R}$.

# Properties
- An instance of a [[Measure (Measure Theory)|measure]].
- Borel measures on $\mathbb{R}$ that are finite on bounded sets correspond exactly to increasing right-continuous functions $F$, modulo constants, via $\mu((a,b]) = F(b) - F(a)$ ([[Lebesgue-Stieltjes Measure]]).

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=46&annotation=LYQ8MDCY)
