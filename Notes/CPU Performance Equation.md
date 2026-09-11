---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] CPU Performance Equation[^1]
> CPU time can be computed as the number of clock cycles required for a program multiplied by the clock cycle time, or equivalently divided by the clock rate:
> $$
> \text{CPU Time} = \text{Clock Cycles} \times \text{Clock Cycle Time} = \frac{\text{Clock Cycles}}{\text{Clock Rate}}.
> $$
> Since the number of clock cycles equals the instruction count times the average clock cycles per instruction (CPI), CPU time can be written in terms of instruction count, CPI, and clock cycle time:
> $$
> \text{CPU Time} = \text{Instruction Count} \times \text{CPI} \times \text{Clock Cycle Time} = \frac{\text{Instruction Count} \times \text{CPI}}{\text{Clock Rate}}.
> $$

# Properties
- A clock cycle (tick, clock period) is the time for one period of the processor clock, which runs at a constant rate; the clock rate (e.g. 4 GHz) is the inverse of the clock cycle time (e.g. 250 ps).
- Clock cycles per instruction (CPI) is the average number of clock cycles per instruction for a program or program fragment; its inverse, instructions per clock cycle (IPC), is used when a processor can fetch and execute multiple instructions per clock cycle.
- Instruction count is the number of instructions actually executed by the program, which depends on the instruction mix — the dynamic frequency of each instruction type across the program.
- The algorithm, programming language, [[Compiler]], [[Instruction Set Architecture]], and hardware implementation each affect one or more of instruction count, CPI, and clock cycle time.
- Feeds directly into [[Response Time and Throughput|execution time]], the only unimpeachable measure of performance.
- [[Amdahl's Law]] is used together with this equation to evaluate the effect of a proposed enhancement on overall execution time.
- Pitfall: using a subset of this equation, such as [[MIPS]], as a stand-alone performance metric.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=59&annotation=SUKAWDWM)
