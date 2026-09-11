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

IEEE 754 lays a floating-point word out as a sign bit, followed by the exponent field, followed by the fraction field, e.g. `s | exponent | fraction`. Since a [[Normalized Floating-Point System|normalized]] binary mantissa always has a leading 1 bit, that bit is left implicit rather than stored: the stored $(p-1)$-bit pattern is called the fraction, while the full $p$-bit value of 1 followed by the fraction is called the significand. The reserved exponent value of all 0s is used for zero (and, with a nonzero fraction, for denormalized numbers) so that hardware never attaches a leading 1 to it; see [[Denormalized Number]].[^2]

- [[Normalized Floating-Point System]]
- [[Machine Number]]
- [[Rounding]]
- [[Machine Epsilon]]
- [[Underflow Level]]
- [[Overflow Level]]
- The exponent $E$ is stored in hardware using [[Biased Notation]] so that its encoding preserves numeric ordering under unsigned comparison.
- [[Standard Model of Floating-Point Arithmetic]]
- [[Catastrophic Cancellation]]
- [[IEEE Floating-Point Special Values]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=38)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=221&annotation=DSNI3DWD)
