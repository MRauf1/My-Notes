---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Hypergeometric Distribution[^1]
> A lot of $N$ items contains $D$ defective ones. A sample of size $n$ is drawn at random without replacement, and $X$ is the number of defective items in it. Then
> $$
> \begin{align}
> p(x) = \frac{\binom{D}{x}\binom{N - D}{n - x}}{\binom{N}{n}}, \quad x = 0, 1, \dots, n
> \end{align}
> $$
> where a binomial coefficient is $0$ when its top value is less than its bottom value. $X$ has a hypergeometric distribution with parameters $(N, D, n)$.

Each of the $\binom{N}{n}$ samples is equally likely ([[Probability of Equally Likely Outcomes]]), and $\binom{D}{x}\binom{N-D}{n-x}$ of them contain exactly $x$ defectives ([[Combination]]). Sampling with replacement instead gives the [[Binomial Distribution]] $b(n, D/N)$.

# Properties
- $E(X) = n\frac{D}{N}$, the same as sampling with replacement.
- $\text{Var}(X) = n\frac{D}{N}\frac{N - D}{N}\frac{N - n}{N - 1}$: the binomial variance times the finite population correction $\frac{N-n}{N-1} \leq 1$, which is close to $1$ when $N \gg n$. Sampling without replacement reduces variance because the draws are negatively correlated.
- As $N \to \infty$ with $D/N \to p$ and $n$ fixed, it converges to $b(n, p)$.
- The multivariate version (several categories) relates to the [[Multinomial Distribution]] as this one relates to the binomial.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=178)
