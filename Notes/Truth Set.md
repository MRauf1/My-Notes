---
tags: mathematics, discrete_mathematics
---

# Definition

> [!info] Definition 1 (Truth Set)
> For a [[Proposition|statement]] $P(x)$ with [[Free Variable|free variable]] $x$
> $$
> \begin{align}
> \text{Truth Set of } P(x) = \{x | P(x)\}
> \end{align}
> $$

The [[Set|set]] of all values of $x$ that make the statement $P(x)$ true.[^1]

This extends to more than $1$ free variable by using the [[Cartesian Product|cartesian product]].[^2]

# Truth Sets for Logic Operations

> [!info] Definition 2 (Truth Set of $\land$)
> If $A$ is the truth set of $P(x)$ and $B$ is the truth set of $Q(x)$, then
> $$
> \begin{align}
> P(x) \land Q(x) = A \cap B
> \end{align}
> $$

> [!info] Definition 3 (Truth Set of $\lor$)
> If $A$ is the truth set of $P(x)$ and $B$ is the truth set of $Q(x)$, then
> $$
> \begin{align}
> P(x) \lor Q(x) = A \cup B
> \end{align}
> $$

> [!info] Definition 4 (Truth Set of $\neg$)
> If $A$ is the truth set of $P(x)$ and $U$ is the [[Universe of Discourse|universe of discourse]], then
> $$
> \begin{align}
> \neg P(x) = U \setminus A
> \end{align}
> $$

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=44)
[^2]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=183)
