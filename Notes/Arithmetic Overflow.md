---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Arithmetic Overflow[^1]
> The condition where the true result of an arithmetic operation cannot be represented within the fixed number of bits the hardware provides for the result.

# Properties
- Can occur for both unsigned numbers and [[Two's Complement]] numbers, since both use a fixed-width bit pattern.
- Distinct from the [[Overflow Level]] of a [[Floating-Point Number System]], which bounds representable exponents rather than fixed-width integer results.
- For addition of two's complement numbers, overflow is impossible when the operands have different signs, since the sum can be no larger in magnitude than the larger operand; overflow occurs exactly when two operands of the same sign produce a sum of the opposite sign, meaning a carry out occurred into the sign bit.
- For subtraction of two's complement numbers, overflow is impossible when the operands have the same sign; overflow occurs exactly when subtracting a negative number from a positive one yields a negative result, or subtracting a positive number from a negative one yields a positive result, meaning a borrow occurred from the sign bit.
- Detected in hardware by raising an [[Exception (Computer Architecture)|exception]]; a computer designer must provide separate arithmetic instructions for when overflow should be recognized versus ignored (as when arithmetic is known to operate on unsigned addresses).
- [[Saturating Arithmetic]] is an alternative to exception-based overflow handling, common in media processing.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=97&annotation=NLMRW574)
