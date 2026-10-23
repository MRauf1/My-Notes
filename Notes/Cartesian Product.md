---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Cartesian Product)[^1]
> For two [[Set|sets]] $A, B$, their cartesian product is
> $$
> \begin{align}
> A \times B = \{(a, b) | a \in A \land b \in B\}
> \end{align}
> $$

The set of all [[Ordered Pair|ordered pairs]] where the first coordinate is the element of the first set and the second coordinate is the element of the second set.

> [!info] Definition 2 (Cartesian Product of $n$ Same Sets)
> For a set $A$, its $n$th cartesian product is
> $$
> \begin{align}
> A^n = \{(a_1, a_2, \dots, a_n) | a_1, a_2, \dots, a_n \in A\}
> \end{align}
> $$
> Note that for $X \times Y \times Z$, the resulting elements are $(x, y, z)$; for $(X \times Y) \times Z$, it is $((x, y), z)$; for $X \times (Y \times Z)$, it is $(x, (y, z))$.

> [!info] Definition 3 (Cartesian Product of an Indexed Family)[^2]
> For an indexed family of sets $\{X_\alpha\}_{\alpha \in A}$,
> $$
> \begin{align}
> \prod_{\alpha \in A} X_\alpha = \left\{ f: A \to \bigcup_{\alpha \in A} X_\alpha \;\middle|\; f(\alpha) \in X_\alpha \text{ for all } \alpha \in A \right\}
> \end{align}
> $$
> For $\alpha \in A$, the $\alpha$th projection or coordinate map $\pi_\alpha: \prod_{\beta \in A} X_\beta \to X_\alpha$ is $\pi_\alpha(f) = f(\alpha)$. One usually writes $x$ and $x_\alpha$ instead of $f$ and $f(\alpha)$, and calls $x_\alpha$ the $\alpha$th coordinate of $x$.

> [!info] Definition 4 (Power of a Set)[^3]
> If $X_\alpha = Y$ for all $\alpha \in A$, then $\prod_{\alpha \in A} X_\alpha$ is denoted $Y^A$, the set of all mappings from $A$ to $Y$. If $A = \{1, \dots, n\}$, $Y^A$ is denoted $Y^n$ and is identified with the set of ordered $n$-tuples of Definition 2.

Definition 3 is the general case: Definitions 1 and 2 are recovered by taking $A = \{1, 2\}$ or $A = \{1, \dots, n\}$ and identifying a function on $A$ with its list of values. Nonemptiness of an infinite product is precisely the [[Axiom of Choice]].

# Properties
- [[Cartesian Product Basic Properties]]
- [[Cartesian Product Set Cardinality]]

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=178)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=17&annotation=RHSZ55ZB)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=17&annotation=2P448AIV)
