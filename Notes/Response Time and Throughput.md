---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Response Time and Throughput[^1]
> Response time (also called execution time) is the total time required for the computer to complete a task, including disk accesses, memory accesses, I/O activity, operating system overhead, and CPU execution time. Throughput (also called bandwidth) is the number of tasks completed per unit time. Performance is defined as the reciprocal of execution time,
> $$
> \text{Performance} = \frac{1}{\text{Execution Time}},
> $$
> so that computer $X$ is $n$ times as fast as computer $Y$ exactly when
> $$
> \frac{\text{Performance}_X}{\text{Performance}_Y} = \frac{\text{Execution Time}_Y}{\text{Execution Time}_X} = n.
> $$

# Properties
- Execution time is the only complete and reliable, unimpeachable measure of computer performance.
- Changing either execution time or throughput often affects the other in real computer systems, but they are not interchangeable measures.
- CPU execution time (CPU time) is the time the CPU spends computing a specific task, excluding time spent waiting for I/O or running other programs; it splits into user CPU time (spent in the program itself) and system CPU time (spent in the [[Operating System]] on the program's behalf).
- System performance refers to elapsed time on an unloaded system, while CPU performance refers to user CPU time.
- Feeds into the [[CPU Performance Equation]], which decomposes CPU execution time into instruction count, clock cycles per instruction, and clock cycle time.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=52&annotation=5NT46PJW)
