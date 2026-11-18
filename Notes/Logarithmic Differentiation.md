---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Logarithmic Differentiation)[^1]
> To differentiate $y = f(x)$:
> 1. Take natural logarithms of both sides and simplify with the [[Logarithm Product Rule]], [[Logarithm Quotient Rule]] and [[Logarithm Power Rule]].
> 2. Differentiate implicitly with respect to $x$ ([[Implicit Differentiation]]), using $\frac{d}{dx}\ln y = \frac{y'}{y}$ ([[Derivative of Logarithmic Function]]).
> 3. Solve for $y'$.
>
> If $f(x) < 0$ for some $x$, apply it to $|y| = |f(x)|$, since $\frac{d}{dx}\ln|x| = \frac{1}{x}$.

# Properties
- Turns products, quotients and powers into sums, so it simplifies derivatives of complicated products.
- Necessary for variable bases and exponents, $y = f(x)^{g(x)}$, where neither the [[Derivative Power Rule]] nor the [[Derivative of Exponential Function]] applies: $y' = y\left(g'\ln f + g\frac{f'}{f}\right)$.
- Proves the general Power Rule $\frac{d}{dx}x^n = nx^{n-1}$ for any real $n$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=253)
