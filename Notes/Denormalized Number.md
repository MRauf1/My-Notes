---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Denormalized Number (Subnormal)[^1]
> An IEEE 754 floating-point number represented in unnormalized form: it shares the reserved zero exponent with zero itself, but has a nonzero fraction. Denormalized numbers fill the gap between zero and the smallest [[Normalized Floating-Point System|normalized]] number, letting a value degrade gradually in significance down to zero (gradual underflow) instead of jumping straight from the [[Underflow Level]] to zero.

# Properties
- Squeezes extra precision out of values near the [[Underflow Level]] at the cost of complicating floating-point hardware; many implementations instead raise an exception on a denormalized operand and let software complete the operation, at a performance cost, which has limited how widely denorms are relied upon in portable floating-point software.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=245&annotation=QP946MZ9)
