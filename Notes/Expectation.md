---
tags: statistics, bayesian_statistics
---

# Definition

> [!info] Definition 1 (Expectation of [[Discrete Random Variable]])[^1]
> For a [[Discrete Random Variable|discrete RV]] $X$ with an [[Universe of Discourse|outcome space]] $S$, its expectation is
> $$
> \begin{align}
> E[X] = \mu = \sum_{x \in S} x f(x)
> \end{align}
> $$

> [!info] Definition 2 (Expectation of [[Continuous Random Variable]])[^1]
> For a [[Continuous Random Variable]] $X$ with an [[Universe of Discourse|outcome space]] $S$, its expectation is
> $$
> \begin{align}
> E[X] = \mu = \int_{-\infty}^{\infty} x f(x) dx
> \end{align}
> $$

The expectation is also known as the [[Mean|mean]] of the random variable.

Expectation measures the center of the distribution.

Expectation is a [[Linear Map|linear operator]].

# Properties

## Main

- $c$ is a [[Constant|constant]] $\implies E[c] = c$
- $g$ is a [[Function|function]] and $X$ is a discrete RV $\implies E[g(x)] = \sum_{x \in S} g(x) f(x)$ ([[Weighted Mean|Weighted mean]] of $g(x)$)
- $g$ is a [[Function|function]] and $X$ is a continuous RV $\implies E[g(x)] = \int_{x \in S} g(x) f(x)$ ([[Weighted Mean|Weighted mean]] of $g(x)$)

## Linearity of Expectation

- $c$ is a [[Constant|constant]] and $X$ is a RV $\implies E[cX] = c E[X]$
- $X_1$ and $X_2$ are [[Random Variable|RVs]] $\implies E[X + Y] = E[X] + E[Y]$

## [[Conditional Expectation]]
- [[Law of Total Expectation]]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=59)