---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Cantor Function (Cantor–Lebesgue Function)[^1]
> Every $x$ in the [[Cantor Set]] $C$ has a base-3 expansion $x = \sum_1^\infty a_j 3^{-j}$ with all $a_j \in \{0, 2\}$. Define $f : C \to [0, 1]$ by
> $$
> \begin{align}
> f\left(\sum_{j=1}^\infty a_j 3^{-j}\right) = \sum_{j=1}^\infty \frac{a_j}{2}\, 2^{-j},
> \end{align}
> $$
> and extend $f$ to $[0, 1]$ by making it constant on each open interval removed in constructing $C$.

On $C$, $f$ is order preserving except that the two endpoints $x < y$ of a removed interval map to the same dyadic rational $p 2^{-k}$ (its two base-2 expansions), which is what makes the constant extension consistent.

# Properties
- [[Increasing Function|Increasing]] and maps $[0,1]$ onto $[0,1]$; an increasing function whose range is an interval has no [[Jump Discontinuity|jump discontinuities]], so $f$ is [[Continuous Function|continuous]].[^1]
- Constant on each removed interval, so $f' = 0$ on $[0,1] \setminus C$, a set of full Lebesgue measure; yet $f(0) = 0$ and $f(1) = 1$. It is continuous but not absolutely continuous.
- $f$ maps $C$ onto $[0,1]$, which proves $\operatorname{card}(C) = \mathfrak{c}$.
- As a [[Cumulative Distribution Function]], it defines the Cantor distribution: a [[Lebesgue-Stieltjes Measure]] with no atoms that is singular to [[Lebesgue Measure]] ([[Mutually Singular Measures]]).
- Used to exhibit Lebesgue measurable sets that are not Borel.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=52&annotation=QWGCYA78)
