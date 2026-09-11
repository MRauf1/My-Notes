---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Rounding)[^1]
> Rounding is the process of choosing a nearby [[Floating-Point Number System|floating-point number]] $fl(x)$ to approximate a given real number $x$ that is not a [[Machine Number]]. The error introduced by this approximation is [[Rounding Error]].

# Types
- **Chop** (round toward zero): the base-$\beta$ expansion of $x$ is truncated after the $(p-1)$st digit, so $fl(x)$ is the next floating-point number toward zero from $x$.
- **Round to nearest** (round to even): $fl(x)$ is the nearest floating-point number to $x$; ties are broken toward the floating-point number whose last stored digit is even.

Round to nearest is the most accurate and unbiased rule, though more expensive to implement correctly, and is the default rounding rule in IEEE standard systems. IEEE 754 defines four rounding modes: always round up (toward $+\infty$), always round down (toward $-\infty$), chop (truncate), and round to nearest even.

# Properties
- To round correctly, hardware keeps extra bits during intermediate calculations beyond the arithmetic that combines two significands: a guard bit and a round bit are kept immediately to the right of the significand, and a sticky bit is set whenever any nonzero bits fall to the right of the round bit, letting round-to-nearest-even distinguish an exact tie from a value merely close to one. With guard, round, and sticky bits, IEEE 754 guarantees a result within one-half a unit in the last place (ulp) of the exact answer, absent overflow or underflow.
- Units in the last place (ulp) measures rounding accuracy as the number of bits of error in the least significant bits of the significand between the true value and its rounded floating-point representation.
- A [[Fused Multiply-Add]] instruction rounds only once, after the add, rather than once after the multiply and again after the add, improving the precision of a multiply-accumulate compared with two separately rounded instructions.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=40)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=241&annotation=B5DIUZZQ)
