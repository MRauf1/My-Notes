---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Numeric Type Coercion (Python)[^1]
> In a mixed-type numeric expression, Python first converts (coerces) all operands up to the type of the most complex operand present, then performs the operation on same-type operands.

# Properties
- Python ranks numeric complexity as integers < floating-point numbers < complex numbers, so mixing an integer with a float converts the integer up to a float first, and mixing in any complex operand converts everything up to complex[^2].
- Equality and magnitude comparisons perform the same up-conversion, so `3 == 3.0` is true even though the operands started as different types[^2].
- Coercion applies only across numeric type boundaries: Python does not automatically convert between numbers and other types, such as strings, so adding a digit string to an integer is an error unless one operand is converted manually[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=149&annotation=DXPGE4WG)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=150&annotation=PHDTYWC2)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=150&annotation=VBG4Y4GT)
