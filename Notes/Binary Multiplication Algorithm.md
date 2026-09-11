---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Binary Multiplication Algorithm[^1]
> Ignoring sign, the product of an $n$-bit multiplicand and an $m$-bit multiplier is $n+m$ bits long. The basic shift-and-add algorithm repeats three steps once per multiplier bit: if the current least-significant bit of the multiplier is 1, add the multiplicand into the product register; shift the multiplicand register left one bit; and shift the multiplier register right one bit to expose its next bit.

# Types
- Sequential shift-and-add — the basic algorithm above, refined to take one clock cycle per step by shifting the multiplier and multiplicand in parallel with a conditional add, and by halving the width of the adder and registers to drop their unused portions.
- Parallel-tree multiplication — instead of one adder reused $n$ times, uses one 32-bit adder per multiplier bit (each adding the multiplicand ANDed with that bit to the output of a prior adder) arranged in a parallel tree, so only $\log_2 n$ add times are needed instead of $n$; carry-save adders can push performance further and are easy to pipeline.

# Properties
- For signed operands, the simplest approach converts the multiplier and multiplicand to positive numbers, runs the algorithm ignoring sign, then negates the product if the original signs disagreed; a variant instead runs the algorithm directly on [[Two's Complement]] operands by [[Sign Extension|sign-extending]] the product at each shift.
- MIPS multiply instructions ignore [[Arithmetic Overflow]], leaving it to software to check whether the product fits in 32 bits.
- A [[Compiler]] applies the strength reduction optimization of replacing a multiply by a power of 2 with a left shift, since shifting left by $i$ bits is equivalent to multiplying by $2^i$.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=206&annotation=YJD7DAWL)
