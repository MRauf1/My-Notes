---
tags: statistics, categorical_variable_prediction
---

# Definition

[[Contingency Table]] with 3 [[Random Variable]] $X, Y, Z$, where we are interested in how the relationship of $X, Y$ changes with the variable $Z$. In other words, we are interested in the [[Probability Distribution]] $(X, Y)$ [[Conditional Probability|conditional]] on $Z$.

$Z$ may be called a [[Stratification Variable]]. In [[Observational Study]], $Z$ may be a [[Confounding Variable]].

Each $Z$ category defines a partial table for $X, Y$, which represent the conditional associations.

![[Pasted image 20250913150802.png]]

The marginal table sums the partial tables across the $Z$ categories, which represent the marginal association (ignoring $Z$).

![[Pasted image 20250913150811.png]]

There can be conditional associations, but not marginal ones, and vice versa. In the worst case, there is [[Simpson's Paradox]]

> [!info] Definition 1 ([[Conditional Probability|Conditional]] [[Independent Random Variable|Independence]])
> $X, Y$ are conditionally independent given $Z = k$ if
> $$
> \begin{align}
> \theta_{XY(k)} = 1
> \end{align}
> $$
> If this is true for all $k$, $X, Y$ are conditionally independent given $Z$.

> [!info] Definition 2 (Homogeneous Association)
> $X, Y$ have homogeneous association over $Z$ if
> $$
> \begin{align}
> \theta_{XY(1)} = \dots = \theta_{XY(K)}
> \end{align}
> $$
> Conditional independence is a special case of this.
> Even under homogeneous association, conditional and marginal associations may be different.

# Measurements
- [[Conditional Odds Ratio]]
- [[Marginal Odds Ratio]]