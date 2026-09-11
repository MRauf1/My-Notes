---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Biased Notation[^1]
> A signed-number notation that represents the most negative value as $00\ldots000_2$ and the most positive value as $11\ldots11_2$, with the value 0 typically stored as $10\ldots00_2$. The stored bit pattern equals the true value plus a fixed bias, chosen so that the stored representation is always non-negative.

# Properties
- An alternative to [[Two's Complement]] for representing signed quantities; unlike two's complement, biased values preserve numeric ordering under an unsigned integer comparison, which is why it is used to encode the exponent of an [[Floating-Point Number System|IEEE floating-point number]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=102&annotation=QHIGYCZ8)
