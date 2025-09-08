---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Integer Span)[^1]
> For non-zero [[Integer|integers]] $m, n$, the [[Set|set]] is
> $$
> \begin{align}
> I(m, n) = \{am + bn | a, b \in \mathbb{Z}\}
> \end{align}
> $$

Think of it as a [[Span|span]], but for (non-zero) integers. It is a set of [[Integer Combination|integer combinations]].

# Properties

- $\forall x, y \in I(m, n), x + y \in I(m, n) \land -x \in I(m, n)$
- $\forall x \in \mathbb{Z}, xI(m, n) \subseteq I(m, n)$
- $\forall b \in \mathbb{Z}, (b | m \land b | n) \implies \forall x \in I(m, n), b | x$
- $I(a, b) = \mathbb{Z}d$, where $d = gcd(a, b)$
- $d = gcd(m, n) \in I(m, n)$
- $a, b \in I(c, d) \implies I(a, b) \subseteq I(c, d)$
- $F(m, n) = (a, b) \implies I(m, n) = I(a, b)$, where $F$ is from [[Euclidean Algorithm]]

[^1]: [Algebra - Abstract and Concrete](zotero://open-pdf/library/items/IQ3GJ7PV?page=41)