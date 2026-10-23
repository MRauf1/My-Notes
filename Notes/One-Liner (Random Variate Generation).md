---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] One-Liner[^1]
> A one-liner is a sampling rule given by an expression in finitely many $\mathcal{U}(0,1)$ random variables $U_i$, the arithmetic operations $+, -, \times, \div$, and a menu of familiar functions ($\log$, $\exp$, $\sin$, $\cos$, $\lfloor \cdot \rfloor$, inverse trigonometric functions, ...), with each $U_i$ used once. A rule that reuses a value (e.g. $U_1 + U_1U_2$) must store and retrieve it and is called an extended one-liner.

The precise class depends on which functions are allowed on the menu.

# Properties
- Examples: [[Inverse Transform Sampling|inversion]] formulas such as $-\log(U)$ for [[Exponential Distribution|Exp(1)]] and $\tan(\pi(U - 1/2))$ for [[Cauchy Distribution|Cauchy]]; each output of the [[Box-Muller Transform]] is a one-liner, while delivering both from the same $U_1, U_2$ reuses them.
- One of the families of [[Non-Uniform Random Variate Generation|non-uniform random variate generation]] methods.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=18&annotation=98SBHL52)
