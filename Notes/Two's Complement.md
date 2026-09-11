---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Two's Complement[^1]
> The convention used to represent signed binary numbers in most computer hardware: a leading 0 means the number is positive, and a leading 1 means it is negative. Recognizing the role of this sign bit, a signed 32-bit number can be written using the [[Positional Number System]] with a negated leading term,
> $$
> x = -x_{31}\cdot 2^{31} + \sum_{i=0}^{30} x_i \, 2^i.
> $$

# Properties
- All negative numbers have a 1 in the most significant bit (the sign bit), so hardware needs to test only that bit to determine the sign of a number, with 0 considered positive.
- To negate a two's complement number, invert every bit (0 to 1 and 1 to 0) and add one to the result.
- Sign extension converts an $n$-bit two's complement number to a wider representation by replicating the sign bit into the new, higher-order bits; see [[Sign Extension]].
- Arithmetic on two's complement numbers can overflow the hardware's capacity to represent the result, just as it can for unsigned numbers; see [[Arithmetic Overflow]].
- Alternative signed representations include [[One's Complement]] and [[Biased Notation]], but two's complement was chosen because it keeps the hardware simple.
- Memory addresses are inherently unsigned, since negative addresses make no sense; languages such as C distinguish signed integers from unsigned integers to reflect this.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=98&annotation=Q772ZK4J)
