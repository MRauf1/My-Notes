---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] MIPS (Million Instructions Per Second)[^1]
> A measurement of program execution speed based on the number of millions of instructions executed, computed as
> $$
> \text{MIPS} = \frac{\text{Instruction Count}}{\text{Execution Time} \times 10^6}.
> $$

# Properties
- Pitfall: using MIPS as a performance metric has three problems. It specifies the instruction execution rate without accounting for the capabilities of the instructions, so it cannot compare computers with different [[Instruction Set Architecture|instruction sets]]. It varies between programs run on the same computer, so a computer has no single MIPS rating. Most importantly, if a new program executes more instructions but each instruction runs faster, MIPS can vary independently of actual performance.
- Contrast with the [[CPU Performance Equation]] and [[Response Time and Throughput|execution time]], which remain the only reliable performance measures.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=74&annotation=77Y6BAFT)
