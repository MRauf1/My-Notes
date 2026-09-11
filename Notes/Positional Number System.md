---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Positional Number System[^1]
> In any number base $b$, the value of a number is the sum of each digit $d_i$ times a power of the base,
> $$
> \text{value} = \sum_i d_i \, b^i,
> $$
> where $i$ starts at 0 and increases from right to left. This gives an obvious way to number the bits of a binary word: bit $i$ contributes $d_i \times 2^i$.

# Properties
- Applied to unsigned 32-bit binary numbers, this gives $x = \sum_{i=0}^{31} x_i \, 2^i$ where $x_i$ is the $i$th bit of $x$; see [[Two's Complement]] for the analogous representation of signed numbers.
- Hexadecimal (base 16) is popular in computing because it is a power of 2: each group of four binary digits converts trivially to a single hexadecimal digit, avoiding long, tedious strings of binary numbers.
- The least significant bit is the rightmost bit (the $i=0$ term); the most significant bit is the leftmost bit.
- The first commercial computers experimented with representing decimal digits directly in binary, but decimal representation proved so inefficient that subsequent computers reverted to pure binary, converting to base 10 only for infrequent input/output events.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=96&annotation=5JENKWNU)
