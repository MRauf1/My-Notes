---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Absolutely Continuous Function[^1]
> A function $F : \mathbb{R} \to \mathbb{C}$ is absolutely continuous if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for any finite set of disjoint intervals $(a_1, b_1), \dots, (a_N, b_N)$,
> $$
> \begin{align}
> \sum_{j=1}^N (b_j - a_j) < \delta \implies \sum_{j=1}^N |F(b_j) - F(a_j)| < \varepsilon
> \end{align}
> $$
> $F$ is absolutely continuous on $[a, b]$ if this holds whenever all the intervals lie in $[a, b]$.

The difference from [[Uniformly Continuous Function|uniform continuity]] is that $\delta$ must control many small intervals *at once*: their total length being small must force the total change of $F$ to be small. Uniform continuity is the case $N = 1$. A function can concentrate all of its increase on a set that is covered by intervals of arbitrarily small total length, which uniform continuity cannot detect and absolute continuity forbids.

# Properties
- Absolutely continuous $\Rightarrow$ [[Uniformly Continuous Function|uniformly continuous]] (take $N = 1$).[^1]
- [[Lipschitz Continuity|Lipschitz]] $\Rightarrow$ absolutely continuous. In particular, if $F$ is differentiable everywhere with $F'$ bounded, then $|F(b_j) - F(a_j)| \leq (\sup |F'|)(b_j - a_j)$ by the [[Mean Value Theorem]].[^1]
- Absolutely continuous on $[a, b]$ $\Rightarrow$ of bounded variation on $[a, b]$.[^2]
- **Fundamental Theorem of Calculus for Lebesgue Integrals.** For $F : [a, b] \to \mathbb{C}$ with $-\infty < a < b < \infty$, the following are equivalent:[^2]
	1. $F$ is absolutely continuous on $[a, b]$.
	2. $F(x) - F(a) = \int_a^x f(t)\,dt$ for some $f \in L^1([a, b], m)$.
	3. $F$ is differentiable [[Almost Everywhere|a.e.]] on $[a, b]$, $F' \in L^1([a, b], m)$, and $F(x) - F(a) = \int_a^x F'(t)\,dt$.

  So absolutely continuous functions are exactly the functions that are [[Lebesgue Integral (Measure Theory)|Lebesgue integrals]] of their derivatives. This generalizes the [[Fundamental Theorem of Calculus]], which needs a continuous integrand.
- **Link to measures.** For $F$ increasing, right-continuous, with $F(-\infty) = 0$ (more generally $F$ in NBV), $F$ is absolutely continuous if and only if its Lebesgue–Stieltjes measure $\mu_F$ is [[Absolutely Continuous Measure|absolutely continuous]] with respect to [[Lebesgue Measure]] $m$.[^1] Applied to a cdf, $F_X$ is absolutely continuous exactly when $X$ has a pdf ([[Continuous Random Variable]]).
- Continuous and of bounded variation does not imply absolutely continuous. The [[Cantor Function]] is continuous and increasing, but $F' = 0$ a.e., so $\int_0^1 F' = 0 \neq 1 = F(1) - F(0)$, contradicting condition 3. Its measure is singular continuous.[^2]

# Questions
> [!question]- Why is the Cantor function uniformly continuous but not absolutely continuous? Which intervals witness the failure?
> It is continuous on the compact set $[0, 1]$, hence uniformly continuous. At stage $n$ of the construction, the [[Cantor Set]] is covered by $2^n$ disjoint closed intervals of length $3^{-n}$ each, so of total length $(2/3)^n \to 0$. $F$ is constant on every removed middle third, so its whole increase from $0$ to $1$ happens on these intervals: $\sum_j |F(b_j) - F(a_j)| = 1$. (Slightly enlarging the intervals to make them open and disjoint keeps the total length small.) So no $\delta$ works for $\varepsilon = 1$.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=118)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=119)
