---
tags: [mathematics, real_analysis]
---

# Definition

> [!info] Definition 1 (Darboux [[Integral]])[^1]
> Let $f$ be a [[Bounded Function]] on closed [[Interval Notation]] $[a, b]$. For $S \subseteq [a, b]$, let $M(f, S) = \sup\{f(x) | x \in S\}$, $m = \inf\{f(x) | x \in S\}$. The upper Darboux sum is $U(f, P) = \sum_{k=1}^n M(f, [t_{k-1}, t_k]) \cdot (t_k - t_{k-1})$, and the lower Darboux sum is $L(f, P) = \sum_{k=1}^n m(f, [t_{k-1}, t_k]) \cdot (t_k - t_{k-1})$. Note that $m(f, [a, b]) \cdot (b - a) \leq L(f, P) \leq U(f, P) \leq M(f, [a, b]) \cdot (b - a)$. Upper Darboux integral of $f$ over $[a, b]$ is $U(f) = \inf\{U(f, P) | P\ \text{is a partition of}\ [a, b]\}$, and lower Darboux integral of $f$ over $[a, b]$ is $L(f) = \sup\{L(f, P) | P\ \text{is a partition of}\ [a, b]\}$.
> $f$ is Darboux integrable on $[a, b]$ provided $U(f) = L(f)$ in which case,
> $$
> \begin{align}
> \int_a^b f(x) dx = L(f) = U(f)
> \end{align}
> $$

# Properties
- [[Darboux Sums of 2 Partitions Lemma]]
- [[Darboux Integrable Theorem]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=278)