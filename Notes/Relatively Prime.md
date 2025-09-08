---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Relatively [[Prime Number|Prime]])[^1]
> Non-zero [[Integer|integers]] $m, n$ are relatively prime if
> $$
> \begin{align}
> gcd(m, n) = 1
> \end{align}
> $$
> where $gcd(m, n)$ is the [[Greatest Common Divisor|GCD]] of $m, n$

This can be extended to $n$ non-zero integers if every pair has this property. Two distinct non-zero integers within the sequence are pairwise relatively prime if the two of them are relatively prime.

A list of integers are pairwise relatively prime if each distinct pair is relatively prime.

# Properties

- Two non-zero integers $m, n$ are relatively prime $\iff \exists s, t \in \mathbb{Z}, 1 = sm + tn$[^1]
- Let $a, b$ be relatively prime [[Natural Number|natural numbers]]. $\forall x \in \mathbb{Z}, (a | x \land b | x) \implies ab | x$
- If $p$ is a [[Prime Number|prime number]] and $a$ is any non-zero integer, then either $p | a$ or $p$ and $a$ are relatively prime

## List of Relatively Prime

Let $a_1, \dots, a_k$ be pairwise relatively prime

- Then $a_k, b = a_1 \cdot \dots \cdot a_{k-1}$ are relatively prime
- $a_i | n$ for all $i$ $\implies$ $(a_1 \cdot \dots \cdot a_k) | n$

#TODO 
- Does the second property hold true for negative numbers too?

[^1]: [Algebra - Abstract and Concrete](zotero://open-pdf/library/items/IQ3GJ7PV?page=43)