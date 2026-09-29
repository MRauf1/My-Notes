---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Histogram Estimator[^1][^2]
> Let $X_1, \dots, X_n$ be a [[Random Sample]] on $X$, with no parametric form assumed.
> - Discrete $X$ with space $\{a_1, \dots, a_m\}$: the nonparametric estimate of the pmf is the [[Relative Frequency]]
> $$
> \begin{align}
> \hat{p}(a_j) = \frac{1}{n}\sum_{i=1}^n I_j(X_i), \qquad I_j(X_i) = \begin{cases} 1 & X_i = a_j \\ 0 & X_i \neq a_j \end{cases}
> \end{align}
> $$
> - Continuous $X$: choose classes $A_j = (a + (2j - 3)h, a + (2j - 1)h]$, $j = 1, \dots, m$, of width $2h$ covering the range of the sample, and set
> $$
> \begin{align}
> \hat{f}_h(x) = \frac{\#\{x_i \in A_j\}}{2hn}, \quad x \in A_j
> \end{align}
> $$
> and $\hat{f}_h(x) = 0$ outside the classes.
>
> The histogram is the bar plot of these estimates.

# Properties
- $\hat{p}(a_j)$ is an [[Unbiased Estimator]] of $p(a_j)$: each $I_j(X_i)$ is [[Bernoulli Distribution|Bernoulli]]$(p(a_j))$, so $E[\hat{p}(a_j)] = p(a_j)$.
- For a countably infinite space, the tail values are merged into one class $\tilde{a}_{m+1} = \{a_{m+1}, a_{m+2}, \dots\}$; a rule of thumb picks $m$ so the frequency of $a_m$ exceeds twice the combined frequency of the merged tail.
- Qualitative (nominal) categories are shown as a bar chart: non-abutting bars ordered by decreasing height. Ordinal categories are shown as abutting bars in their natural order.
- The continuous histogram is a genuine pdf: $\hat{f}_h \geq 0$ and $\int \hat{f}_h = \sum_j \frac{\#\{x_i \in A_j\}}{2hn} \cdot 2h = 1$.
- A discrete histogram is unique (unless classes are merged), but a continuous one depends on the choice of classes (origin $a$ and width $2h$), and the picture can change substantially; default bin-selection rules in software are usually preferred.
- It is a piecewise-constant [[Density Estimation|density estimate]]; the [[Kernel Density Estimation|kernel density estimate]] removes the dependence on the bin origin.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=246)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=250)
