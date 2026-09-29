---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Poisson [[Probability Distribution]])[^1][^2]
> Denoted as $Poisson(\lambda)$, where $\lambda > 0$ is the expected/average number of events in a given interval.
> $$
> \begin{align}
> P(x) &= \frac{e^{-\lambda} \lambda^x}{x!}, x \in \{0, 1, 2, \dots\}
> \end{align}
> $$

Distribution for a number of events/counts occurring randomly in a given period of time/space. There isn't a fixed amount of trials.

Events are [[Independent Events]] and identical so the distribution is [[i.i.d.]].

**Intuition.** The Poisson distribution counts how many times a rare event happens in a fixed window (of time, length, area, or volume) when events occur independently of each other at a constant average rate $\lambda$ per window: tornado touchdowns per year, typos per page, photons hitting a pixel during an exposure. It is the limit of $\text{Binomial}(n, \lambda/n)$ as $n \to \infty$: split the window into many tiny slots, each holding an event with a tiny probability ([[Binomial Distribution Poisson Approximation]]). The axioms making this precise define the [[Poisson Process]], whose count in $(0, t]$ is $Poisson(\lambda t)$.[^3]

# Properties
## Basic Statistical Properties
- [[Poisson Distribution Expectation]]
- [[Poisson Distribution Variance]]
- [[Moment Generating Function|mgf]]:[^4] $M(t) = \sum_x e^{tx}\frac{\lambda^x e^{-\lambda}}{x!} = e^{\lambda(e^t - 1)}$ for all real $t$, giving $\mu = \sigma^2 = \lambda$.

## [[Probability Distribution Skewness]]
- [[Poisson Distribution Skewness]]

## [[Operation]]
- [[Poisson Distribution Addition]]

## [[Approximation]]
- [[Poisson Distribution Normal Approximation]]

## [[Probability Distribution Overdispersion]]
- [[Poisson Distribution Overdispersion]]: when counts vary more than their mean, a gamma-mixed Poisson ([[Negative Binomial Distribution]]) is used.

## [[Multinomial Distribution]]
- [[Poisson Distribution and Multinomial Distribution Connection]]

## Waiting Times
- The waiting time until the $k$th event of the underlying [[Poisson Process]] is [[Gamma Distribution|gamma]]$(k, 1/\lambda)$, and the interarrival times are [[Exponential Distribution|exponential]].

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=24)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=183)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=184)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=185)
