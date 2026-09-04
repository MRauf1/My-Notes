---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Floating-Point Number System)[^1]
> A floating-point number system $F$ is characterized by four integers: a base or radix $\beta$, a precision $p$, and an exponent range $[L, U]$. Any floating-point number $x \in F$ has the form
> $$
> \begin{align}
> x = \pm\left(d_0 + \frac{d_1}{\beta} + \frac{d_2}{\beta^2} + \cdots + \frac{d_{p-1}}{\beta^{p-1}}\right)\beta^E,
> \end{align}
> $$
> where each $d_i$ is an integer with $0 \le d_i \le \beta - 1$, and $E$ is an integer with $L \le E \le U$.

The string of $p$ base-$\beta$ digits $d_0 d_1 \cdots d_{p-1}$ is called the mantissa or significand, $E$ is called the exponent or characteristic, and $d_1 d_2 \cdots d_{p-1}$ (the mantissa without the leading digit) is called the fraction.

A floating-point number system is finite and discrete: it contains exactly $2(\beta-1)\beta^{p-1}(U-L+1)+1$ [[Normalized Floating-Point System|normalized]] numbers. Floating-point numbers are also not uniformly distributed throughout their range — they are equally spaced only between successive powers of $\beta$, so the gap between consecutive floating-point numbers grows with magnitude.

# Properties
| System  | $\beta$ | $p$ | $L$     | $U$    |
| ------- | ------- | --- | ------- | ------ |
| IEEE SP | 2       | 24  | $-126$  | $127$  |
| IEEE DP | 2       | 53  | $-1022$ | $1023$ |

- [[Normalized Floating-Point System]]
- [[Machine Number]]
- [[Rounding]]
- [[Machine Epsilon]]
- [[Underflow Level]]
- [[Overflow Level]]
- [[Standard Model of Floating-Point Arithmetic]]
- [[Catastrophic Cancellation]]
- [[IEEE Floating-Point Special Values]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=38)
