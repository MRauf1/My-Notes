---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Continuous]] [[Random Variable|Random Variable]])[^1]
> A random variable $X$ is continuous if its [[Cumulative Distribution Function]] $F_X(x)$ is a [[Continuous Function]] for all $x \in \mathbb{R}$.

> [!info] Definition 2 (Absolutely Continuous Random Variable)[^1]
> $X$ is absolutely continuous if there is a function $f_X$, its [[Probability Density Function]], such that
> $$
> \begin{align}
> F_X(x) = \int_{-\infty}^x f_X(t)\,dt
> \end{align}
> $$

Since $P(X = x) = F_X(x) - F_X(x^-)$ ([[Cumulative Distribution Function Basic Properties]]), a continuous random variable has no points of discrete mass: $P(X = x) = 0$ for all $x \in \mathbb{R}$. Most continuous random variables met in practice are absolutely continuous, and "continuous" is often used to mean absolutely continuous. An uncountable range is necessary for continuity but not sufficient.

# [[Probability|Probability]] [[Function|Functions]]
- [[Probability Density Function]]
- [[Cumulative Distribution Function]]

# Properties
- [[Expectation]]
- [[Continuous Random Variable Probability Inequality Theorem]]
- $P(a < X \leq b) = F_X(b) - F_X(a) = \int_a^b f_X(t)\,dt$
- There exist continuous but not absolutely continuous random variables (singular distributions, e.g. the Cantor distribution), whose cdf is continuous yet has no density.

# Distributions
- [[Continuous Probability Distribution]]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=65)
