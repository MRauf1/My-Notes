---
tags: mathetatics, calculus
---

# Definition

> [!info] Definition 1 (Limit of Function)[^2]
> Let $f$ be a [[Function]] defined on some [[Interval Notation|open interval]] that contains the number $a$, except possibly at $a$ itself. Then the limit of $f(x)$ as $x$ approaches $a$ is $L$, written as $\lim_{x \rightarrow a} f(x) = L$ if for every number $\epsilon > 0$, there exists a number $\delta > 0$ such that
> $$
> \begin{align}
> 0 < |x - a| < \delta \implies |f(x) - L| < \epsilon
> \end{align}
> $$

Limit of a [[Function]] $f(x)$ as $x \rightarrow a$ is $L$ whenever $f(x)$ is arbitrarily close to $L$ for values of $x$ that are arbitrarily close to $a$ (but not $a$ itself).

The only thing that matters is how $f$ is defined near $a$, not at $x = a$.[^1] Even if $\lim_{x \rightarrow a} f(x) = L$, $f(a)$ might not be defined or might not be equal to $L$.

> [!abstract] Theorem 2 ([[Limit of Function]] and [[One-Sided Limit of Function]])
> $$
> \begin{align}
> \lim_{x \rightarrow a} f(x) = L \iff \lim_{x \rightarrow a^-} f(x) = L = \lim_{x \rightarrow a^+} f(x)
> \end{align}
> $$

# Types
- [[One-Sided Limit of Function]]
- [[Infinite Limit of Function]]
- [[Limit of Function at Infinity]]

# Properties
## Arithmetic Properties
- [[Limit of Function Addition Law]]
- [[Limit of Function Subtraction Law]]
- [[Limit of Function Scalar Product Law]]
- [[Limit of Function Product Law]]
- [[Limit of Function Quotient Law]]
- [[Limit of Function Power Law]]
- [[Limit of Function nth Root Law]]

## [[Polynomial Function]]/[[Rational Function]]
- [[Limit of Function Direct Substitution Property]]

## [[Equality]]/[[Inequality]]
- [[Limit of Function Equality]]
- [[Limit of Function Inequality]]
- [[Limit of Function Squeeze Theorem]]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=116)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=138)