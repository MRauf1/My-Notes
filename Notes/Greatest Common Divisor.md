---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Greatest Common Divisor)[^1]
> [[Natural Number|Natural number]] $d$ is the greatest common divisor of non-zero [[Integer|integers]] $m, n$ if
> 1) $d | m \land d | n$
> 2) $\forall x \in \mathbb{N}, (x | m \land x | n) \implies x | d$

Think of it as the [[Greatest Common Factor|GCF]], but for numbers. It is unique. It is denoted as $gcd(m, n)$. Alternatively, think of it as the [[Largest Common Divisor]] except for the case of $gcd(0, 0)$, which equals to $0$. This can be extended to the GCD of $n$ non-zero integers.

Some definitions exclude $0$, some include it. Including it may result in some slightly anomalous results, but it still works. In particular, if $0$ is included, then

1) Without loss of generality, $gcd(m, 0) = |m|$
2) $gcd(0, 0) = 0$

GCD is computed using the [[Euclidean Algorithm]]

# Properties

- Let $m, n$ be non-zero integers. $\forall d \in \mathbb{N}, (d | m \land d | n \land (\forall x \in I(m, n), d | x)) \implies d = gcd(m, n)$ ($I(m, n)$ is the [[Integer Span|integer span]])[^1]R

[^1]: [Algebra - Abstract and Concrete](zotero://open-pdf/library/items/IQ3GJ7PV?page=41)