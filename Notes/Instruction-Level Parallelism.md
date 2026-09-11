---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Instruction-Level Parallelism (ILP)[^1]
> The parallelism among instructions that lets a processor overlap their execution.

# Properties
- Exploited by [[Pipelining]] and further increased by deepening the pipeline (more, shorter stages) or by [[Multiple Issue|multiple issue]] (launching more instructions per stage).
- [[Speculative Execution|Speculation]], performed by the compiler or the hardware, can expose more ILP by guessing an instruction's outcome to remove it as a dependence for other instructions.
- Ultimately bounded by true data and control dependences within a program, which set an upper limit on sustained performance regardless of how aggressively a processor pipelines or issues instructions, and further constrained in practice by memory-hierarchy stalls.
- Exploiting more ILP through deeper pipelines, [[Multiple Issue|dynamic multiple issue]], and speculation has historically come at a cost in energy efficiency, motivating a shift toward multiple, simpler cores per chip once designs became constrained by power rather than by transistor count; see [[Multicore Microprocessor]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=355&annotation=XL4KEW9R)
