---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Binary Division Algorithm[^1]
> Since a binary digit is only 0 or 1, at each step a division algorithm need only decide whether the divisor goes into the remaining dividend 0 or 1 times, unlike decimal long division. Restoring division decides this by first subtracting the (appropriately shifted) divisor from the remainder: if the result is non-negative, the divisor fit, so the quotient bit is 1 and the subtraction stands; if the result is negative, the divisor did not fit, so the quotient bit is 0 and the divisor is added back to restore the remainder. The divisor is then shifted and the process repeats.

# Types
- Restoring division — the algorithm above; can be refined for speed and cost by shifting the operands and quotient simultaneously with the subtraction and halving the adder and register widths.
- Nonperforming division — a variant of restoring division that does not save a subtraction's result when it is negative, instead adding the dividend into the next step's shifted remainder; averages one-third fewer arithmetic operations than restoring division.
- SRT division — predicts several quotient bits per step (typically 4) via a table lookup on the upper bits of the remainder and divisor, relying on later steps to correct any wrong predictions; used together with Newton's iteration (recasting division as finding the zero of a reciprocal function) to accelerate division using fast multiplication hardware.

# Properties
- For signed operands, the dividend and divisor are treated as positive for the iteration, and the quotient is negated if their original signs disagreed; the sign of a nonzero remainder is set to match the dividend's sign, regardless of the signs of the divisor or quotient, since programming languages expect $(a/b) \times b + (a \bmod b) = a$.
- MIPS divide instructions ignore [[Arithmetic Overflow]] and do not trap on division by zero, leaving both checks to software.
- Fallacy: a right shift is not equivalent to signed integer division by a power of 2 unless the shift is an arithmetic right shift, which extends the sign bit into the vacated high-order bits instead of filling them with 0s; for unsigned integers, an ordinary (logical) right shift by $n$ bits is equivalent to division by $2^n$.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=212&annotation=IKZ8XKX8)
