---
tags:
  - mathematics
  - calculus
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

> [!info] Definition 2 (Limit of [[Real-Valued Function]])[^3]
> For a [[Real-Valued Function]] $f: \mathbb{R}^n \rightarrow \mathbb{R}$ whose [[Domain]] includes [[Point]] arbitrarily close to $(a_1, \dots, a_n)$, then $\lim_{(x_1, \dots, x_n) \rightarrow (a_1, \dots, a_n)} f(x_1, \dots, x_n) = L$ if for every $\epsilon > 0$ there is a number $\delta > 0$ such that
> $$
> \begin{align}
> 0 &< dist(\mathbf{x}, \mathbf{a}) \\
> &= \sqrt{(x_1 - a_1)^2 + \dots + (x_n - a_n)^2} < \delta \implies |f(x_1, \dots, x_n) - L| < \epsilon
> \end{align}
> $$

> [!info] Definition 3 ([[Limit of Function]] on [[Metric Space]])[^4]
> Let $(X, d_X), (Y, d_Y)$ be [[Metric Space|metric spaces]], $E \subseteq X$, $f: E \rightarrow Y$, and $p$ a [[Limit Point]] of $E$. Then $\lim_{x \rightarrow p} f(x) = q$ (or $f(x) \rightarrow q$ as $x \rightarrow p$) if there is a point $q \in Y$ such that for every $\epsilon > 0$ there exists $\delta > 0$ such that
> $$
> \begin{align}
> d_Y(f(x), q) < \epsilon \quad \text{for all } x \in E \text{ with } 0 < d_X(x, p) < \delta
> \end{align}
> $$

Definitions 1 and 2 are special cases: in $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{R}^k$, the distances $d_X, d_Y$ are replaced by absolute values or [[Vector Norm|norms]] of differences. $p \in X$ need not be a point of $E$, and even if $p \in E$, we may have $f(p) \neq \lim_{x \rightarrow p} f(x)$.[^4]

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
- [[Limit of Function Composition Law]]

## [[Polynomial Function]]/[[Rational Function]]
- [[Limit of Function Direct Substitution Property]]

## [[Equality]]/[[Inequality]]
- [[Limit of Function Equality]]
- [[Limit of Function Inequality]]
- [[Limit of Function Squeeze Theorem]]
- [[Limit of Function and One-Sided Limit of Function Theorem]]

## Indeterminate Forms
- [[L'Hospital's Rule]]

## General
- [[Limit of Function Sequential Characterization]] (including uniqueness of the limit)
- [[Limit of Function in Extended Real Number System]]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=116)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=138)
[^3]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=936)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=92)
