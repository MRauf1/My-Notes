---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Standard Model of Floating-Point Arithmetic)[^1]
> Rounding error analysis is usually based on the standard model for floating-point arithmetic:
> $$
> \begin{align}
> fl(x \text{ op } y) = (x \text{ op } y)(1 + \delta), \qquad |\delta| \le \epsilon_{mach},
> \end{align}
> $$
> where op is any of the standard arithmetic operations $+, -, \times, /$.

This model can be interpreted as a statement about relative [[Forward Error]]:
$$
\begin{align}
\frac{|fl(x \text{ op } y) - (x \text{ op } y)|}{|x \text{ op } y|} = |\delta| \le \epsilon_{mach},
\end{align}
$$
and can equivalently be interpreted as a statement about [[Backward Error]].

# Properties
- Ideally $fl(x \text{ op } y)$ is a correctly rounded result, an ideal achieved by IEEE-compliant systems whenever $x \text{ op } y$ is within the range of the floating-point system.
- Floating-point addition and multiplication are commutative but not associative.
- Adding or subtracting two floating-point numbers requires first aligning their exponents by shifting the mantissa of one operand, which can push trailing digits of the smaller-magnitude operand beyond the mantissa's field width and lose them; if the magnitudes differ enough, the smaller operand may be lost entirely.
- Multiplying two $p$-digit mantissas can produce up to $2p$ digits, so the product must generally be rounded; the exponents are simply summed.
- Division can likewise give a result that is not exactly representable.
- A result may also be unrepresentable because its exponent falls outside $[L, U]$, causing [[Overflow Level|overflow]] or [[Underflow Level|underflow]].

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=45)
