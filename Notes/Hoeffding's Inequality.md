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
- Using the variance as well gives [[Bernstein's Inequality]], which is sharper when the variance is much smaller than the squared range.
- Non-asymptotic, unlike the CLT-based [[Monte Carlo Confidence Interval]]; it also allows non-identical ranges $[a_i, b_i]$.
- Proved via the [[Moment Generating Function]] and [[Markov's Inequality]] (Chernoff method).
- Two-sided form, by the union bound ([[Boole's Inequality]]): $P(|S_n - E[S_n]| \geq t) \leq 2\exp\!\left(-2t^2/\sum_{i=1}^n (b_i - a_i)^2\right)$, where $S_n = \sum_i Y_i$. Dividing by $n$: when all $Y_i \in [a, b]$, with probability at least $1 - \delta$, $\left|\frac{S_n}{n} - \frac{E[S_n]}{n}\right| \leq (b - a)\sqrt{\frac{1}{2n}\ln\frac{2}{\delta}}$.[^4]
- The $Y_i$ need only be independent, not identically distributed.[^4]
- The number of variables $n$ must be a constant. If $n$ is random, it must not depend on the realizations of $Y_1, \dots, Y_n$. For example, counting the visits to a state along a fixed-length Markov chain path makes $n$ depend on the outcomes; martingale bounds such as Azuma's inequality handle such cases.[^4]
- Combined with a union bound, it gives simultaneous guarantees over many quantities, the template behind the [[Uniform Sampling Simple Regret Bound]] and the [[Finite Hypothesis Class Generalization Bound]].

# Questions
> [!question]- Derive the high-probability form $\left|\frac{S_n}{n} - \frac{E[S_n]}{n}\right| \leq (b-a)\sqrt{\frac{1}{2n}\ln\frac{2}{\delta}}$ for $Y_i \in [a, b]$.
> Both tails with $t = n\epsilon$ and $\sum_i (b_i - a_i)^2 = n(b-a)^2$ give $P(|S_n/n - E[S_n]/n| \geq \epsilon) \leq 2e^{-2n\epsilon^2/(b-a)^2}$. Setting the right side to $\delta$ and solving gives $\epsilon = (b-a)\sqrt{\frac{1}{2n}\ln\frac{2}{\delta}}$.

> [!question]- Does Hoeffding's inequality need the $Y_i$ to be identically distributed? Where is independence used?
> No identical distribution is needed. In the Chernoff argument, $P(S_n - E[S_n] \geq t) \leq e^{-\lambda t}\,E[e^{\lambda(S_n - E[S_n])}]$ by [[Markov's Inequality]]. Independence factors the [[Moment Generating Function]], $E[e^{\lambda(S_n - E S_n)}] = \prod_i E[e^{\lambda(Y_i - E Y_i)}]$. Each factor is bounded separately by Hoeffding's lemma, $e^{\lambda^2(b_i - a_i)^2/8}$, using only that $Y_i \in [a_i, b_i]$. Optimizing over $\lambda$ gives the bound.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=VXRRASD7); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=36&annotation=QDB932ND)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=36&annotation=2JV4C4YN)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=36&annotation=M57JP4TE)
[^4]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 1](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=1)
