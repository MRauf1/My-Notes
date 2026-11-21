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
- Absolutely continuous does **not** require a continuous pdf: $f_X$ only needs to be integrable (e.g. the uniform pdf jumps at the endpoints). The condition "$f_X$ continuous" is needed only for $F_X' = f_X$ *everywhere*. In general $F_X' = f_X$ [[Almost Everywhere|a.e.]] ([[Absolutely Continuous Function|FTC for Lebesgue integrals]]).
- $X$ is continuous $\iff$ $P_X(A) = 0$ for every countable $A$. $X$ is absolutely continuous $\iff$ $P_X(A) = 0$ for every Lebesgue-null $A$ ([[Absolutely Continuous Measure]]) $\iff$ $F_X$ is an [[Absolutely Continuous Function]].
- There exist continuous but not absolutely continuous random variables. The **Cantor distribution** has the [[Cantor Function]] as its cdf: $F$ is continuous, so there are no atoms, but $F' = 0$ a.e. A pdf would have to equal $F'$ a.e., so it would integrate to $0 \neq 1$, and no pdf exists. All of the mass lies on the [[Cantor Set]], which is uncountable but has length $0$, so the distribution is [[Mutually Singular Measures|singular]] with respect to Lebesgue measure.
- **Lebesgue decomposition.** Every distribution on $\mathbb{R}$ splits uniquely as $P_X = \alpha_d P_d + \alpha_{ac} P_{ac} + \alpha_{sc} P_{sc}$ with $\alpha_d + \alpha_{ac} + \alpha_{sc} = 1$: discrete (atoms), absolutely continuous (has a pdf), and singular continuous (no atoms, but concentrated on a Lebesgue-null set).[^2] Continuous means $\alpha_d = 0$, absolutely continuous means $\alpha_d = \alpha_{sc} = 0$, and a [[Mixture Random Variable]] in Hogg's sense has $\alpha_d, \alpha_{ac} > 0$.

# Distributions
- [[Continuous Probability Distribution]]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=65)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=119)
