---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Hoeffding's Inequality[^1]
> Let $Y_1, \dots, Y_n$ be independent with $P(a_i \leq Y_i \leq b_i) = 1$. Then for $\epsilon > 0$
> $$
> \begin{align}
> P\left(\sum_{i=1}^n (Y_i - E(Y_i)) \geq \epsilon\right) &\leq \exp\left(-\frac{2\epsilon^2}{\sum_{i=1}^n (b_i - a_i)^2}\right) \\
> P\left(\sum_{i=1}^n (Y_i - E(Y_i)) \leq -\epsilon\right) &\leq \exp\left(-\frac{2\epsilon^2}{\sum_{i=1}^n (b_i - a_i)^2}\right)
> \end{align}
> $$

> [!abstract] Corollary (Guaranteed Sample Size)[^2]
> If $Y_1, \dots, Y_n$ are independent with mean $\mu$ and $a \leq Y_i \leq b$, $\hat{\mu} = \frac{1}{n}\sum_i Y_i$, and $\delta \in (0, 1)$, then for $\varepsilon > 0$
> $$
> \begin{align}
> P(|\hat{\mu} - \mu| \geq \varepsilon/2) \leq \delta \quad \text{when} \quad n \geq \frac{2(b - a)^2\log(2/\delta)}{\varepsilon^2}
> \end{align}
> $$

Proof of the corollary: apply both tails with $\epsilon = n\varepsilon/2$ and $\sum_i (b - a)^2 = n(b-a)^2$, giving $2\exp(-n\varepsilon^2/(2(b-a)^2)) \leq \delta$.

So $\hat{\mu} \pm \varepsilon/2$ has guaranteed confidence at least $100(1-\delta)\%$; for $99\%$ ($\delta = 0.01$) this needs $n \geq 10.6\,(b-a)^2/\varepsilon^2$.[^3]

# Properties
- Exponential tail bound, using only boundedness (no variance knowledge); compare the polynomial tail of [[Chebyshev's Inequality]] and the [[Chebyshev Confidence Interval]].
- Non-asymptotic, unlike the CLT-based [[Monte Carlo Confidence Interval]]; it also allows non-identical ranges $[a_i, b_i]$.
- Proved via the [[Moment Generating Function]] and [[Markov's Inequality]] (Chernoff method).

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=VXRRASD7); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=36&annotation=QDB932ND)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=36&annotation=2JV4C4YN)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=36&annotation=M57JP4TE)
