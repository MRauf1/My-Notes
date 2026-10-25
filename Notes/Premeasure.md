---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Premeasure[^1]
> Let $\mathcal{A} \subseteq \mathcal{P}(X)$ be an [[Algebra of Sets|algebra]]. A function $\mu_0 : \mathcal{A} \to [0, \infty]$ is a premeasure if
> 1. $\mu_0(\emptyset) = 0$,
> 2. if $\{A_j\}_1^\infty$ is a sequence of disjoint sets in $\mathcal{A}$ **such that** $\bigcup_1^\infty A_j \in \mathcal{A}$, then $\mu_0\left(\bigcup_1^\infty A_j\right) = \sum_1^\infty \mu_0(A_j)$.
>
> Finite and $\sigma$-finite premeasures are defined as for measures.

A premeasure is the "blueprint" that assigns exact sizes to simple building blocks (e.g. finite unions of intervals). It differs from a [[Measure (Measure Theory)|measure]] only in its domain: an algebra need not contain countable unions, so countable additivity is demanded only when the union happens to land back in $\mathcal{A}$.

| | Premeasure $\mu_0$ | [[Outer Measure]] $\mu^*$ | Measure $\mu$ |
| --- | --- | --- | --- |
| Domain | [[Algebra of Sets\|algebra]] $\mathcal{A}$ | all of $\mathcal{P}(X)$ | [[Sigma-Field\|$\sigma$-algebra]] $\mathcal{M}$ |
| Additivity | countable, when the union is in $\mathcal{A}$ | countable subadditivity | countable additivity |
| Role | exact size of simple sets | outside approximation of any set | final consistent measure |

# Properties
- Finitely additive, by taking $A_j = \emptyset$ for large $j$.[^1]
- **Induced outer measure**:[^2]
$$
\begin{align}
\mu^*(E) = \inf\left\{\sum_{j=1}^\infty \mu_0(A_j) : A_j \in \mathcal{A},\ E \subseteq \bigcup_{j=1}^\infty A_j\right\}. \tag{1.12}
\end{align}
$$

> [!abstract] Proposition 1.13[^3]
> If $\mu_0$ is a premeasure on $\mathcal{A}$ and $\mu^*$ is defined by (1.12), then
> 1. $\mu^*|_\mathcal{A} = \mu_0$;
> 2. every set in $\mathcal{A}$ is [[Carathéodory Measurable Set|$\mu^*$-measurable]].

- Extends to a measure on the generated $\sigma$-algebra ([[Carathéodory Extension Theorem]]).
- For increasing right-continuous $F$, $\mu_0\left(\bigcup_1^n (a_j, b_j]\right) = \sum_1^n [F(b_j) - F(a_j)]$ is a premeasure on the algebra of finite disjoint unions of h-intervals ([[Lebesgue-Stieltjes Measure]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=43&annotation=UMSP68S7)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=44&annotation=QALV457K)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=44&annotation=G7BWGBVU)
