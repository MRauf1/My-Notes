---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Machine Epsilon)[^1]
> The machine epsilon (also called the unit roundoff or machine precision), denoted $\epsilon_{mach}$, bounds the relative error in representing any nonzero real number $x$ within the normalized range of a [[Floating-Point Number System]]:
> $$
> \begin{align}
> \left|\frac{fl(x) - x}{x}\right| \le \epsilon_{mach}.
> \end{align}
> $$

Because this bound holds for any nonzero $x$ regardless of magnitude, machine epsilon can be used to determine when a quantity has become negligible relative to another quantity of similar or larger magnitude.

# Example
> [!example]- Summing a Divergent Series in Floating-Point Arithmetic
> The harmonic series $\sum_{n=1}^{\infty} 1/n$ diverges, yet it has a finite sum when computed in floating-point arithmetic. This is not simply because $1/n$ eventually underflows or the partial sum eventually overflows; rather, the partial sum stops changing once $1/n$ becomes negligible relative to the partial sum, i.e. once
> $$
> \begin{align}
> \frac{1}{n} < \epsilon_{mach}\sum_{k=1}^{n-1}\frac{1}{k},
> \end{align}
> $$
> which occurs well before either underflow or overflow.

# Properties
- Equivalent characterizations of $\epsilon_{mach}$ (which can differ from one another in detail, though they share the same intent):
	- The smallest number such that $fl(1 + \epsilon) > 1$.
	- The distance from $1$ to the next larger floating-point number.
- With rounding by chopping, $\epsilon_{mach} = \beta^{1-p}$; with rounding to nearest, $\epsilon_{mach} = \frac{1}{2}\beta^{1-p}$.
- For IEEE binary floating-point systems, $\epsilon_{mach} = 2^{-24} \approx 10^{-7}$ in single precision and $\epsilon_{mach} = 2^{-53} \approx 10^{-16}$ in double precision, giving about $7$ and $16$ decimal digits of precision, respectively.
- Not to be confused with the [[Underflow Level]]: $\epsilon_{mach}$ is determined by the width of the mantissa field, whereas $\text{UFL}$ is determined by the width of the exponent field. In all practical floating-point systems, $0 < \text{UFL} < \epsilon_{mach} < \text{OFL}$.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=41)
