---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Mutually Independent Random Variables[^1]
> Let $X_1, \dots, X_n$ have joint pdf $f(x_1, \dots, x_n)$ [joint pmf $p(x_1, \dots, x_n)$] and marginal pdfs [pmfs] $f_1, \dots, f_n$ [$p_1, \dots, p_n$]. They are mutually independent if and only if
> $$
> \begin{align}
> f(x_1, \dots, x_n) \equiv \prod_{i=1}^n f_i(x_i) \qquad \left[p(x_1, \dots, x_n) \equiv \prod_{i=1}^n p_i(x_i)\right]
> \end{align}
> $$

This generalizes [[Independent Random Variable|independence of two random variables]], with the identity $\equiv$ read as before (it may fail only on a set of zero volume). Unless mutual and pairwise independence could be confused, "mutually" is usually dropped: "$X_1, \dots, X_n$ are independent" means mutually independent.[^2]

# Types
- [[Independent and Identically Distributed]] (iid) random variables.

# Properties
- Box probabilities factor:
$$
\begin{align}
P(a_1 < X_1 < b_1, \dots, a_n < X_n < b_n) = \prod_{i=1}^n P(a_i < X_i < b_i)
\end{align}
$$
  and conversely this for all boxes characterizes mutual independence, as does $F(\mathbf{x}) = \prod_i F_i(x_i)$ ([[Independent Random Variable Equivalent Conditions]]).
- Expectations of products factor: $E\left[\prod_{i=1}^n u_i(X_i)\right] = \prod_{i=1}^n E[u_i(X_i)]$, whenever each $E[u_i(X_i)]$ exists ([[Expectation of Product of Independent Random Variables]]).
- MGF criterion: if the joint mgf exists, mutual independence holds if and only if $M(t_1, \dots, t_n) = \prod_{i=1}^n M(0, \dots, 0, t_i, 0, \dots, 0)$ ([[Moment Generating Function of Random Vector]]).
- The mgf of a linear combination $\sum_i k_i X_i$ is $\prod_i M_i(k_i t)$ ([[Moment Generating Function Technique]]).
- Mutual independence implies pairwise independence (every sub-collection is mutually independent), but pairwise independence does not imply mutual independence (Bernstein's example); the same distinction as for [[Mutually Independent Events]].[^3]
- Equivalently, the events $\{X_1 \in A_1\}, \dots, \{X_n \in A_n\}$ are [[Mutually Independent Events|mutually independent]] for all sets $A_1, \dots, A_n$; functions of disjoint groups of the $X_i$ are again independent.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=153)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=156)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=155)
