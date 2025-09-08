---
tags: mathematics, pre_calculus
---

# Definition

> [!info] Definition 1 ([[Rational Number|Rational]] [[Function]])[^1]
> Function which is the [[Division]] of two [[Polynomial Function|polynomial functions]] ($p(x), q(x)$)
> $$
> \begin{align}
> r(x) &= \frac{p(x)}{q(x)}
> \end{align}
> $$

# [[Asymptote]]

While the asymptotes are generally lines, a rational function's end behavior may be approaching some other non-linear function, such as a quadratic.

## Hole/[[Vertical Asymptote]]
Suppose $r(x) = \frac{p(x)}{q(x)}$ is a rational function where $p(x), q(x)$ have no common zeros (they are simplified). Let $c$ be a [[Real Number]] not in the [[Domain]] of $r(x)$. Then
- If $q(c) \neq 0$, then the graph has a hole at $(c, r(c))$
- If $q(c) = 0$, then the [[Line]] $x = c$ is a [[Vertical Asymptote]]

## [[Horizontal Asymptote]]
Suppose $r(x) = \frac{p(x)}{q(x)}$ is a rational function where $p(x), q(x)$ have leading coefficients $a, b$ respectively. Then
- If $deg(p) = deg(q)$, then $y = \frac{a}{b}$ is a [[Horizontal Asymptote]]
- If $deg(p) < deg(q)$, then $y = 0$ is a horizontal asymptote
- If $deg(p) > deg(q)$, then there are no horizontal asymptotes

## [[Slant Asymptote]]
Suppose $r(x) = \frac{p(x)}{q(x)}$ is a rational function where $deg(p) - 1 = deg(q)$. Then
- $y = L(x)$ is the slant asymptote where $L(x)$ is the quotient obtained by [[Polynomial Division]] of $p(x)$ by $q(x)$

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=316)