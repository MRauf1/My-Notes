---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Pipelining[^1]
> An implementation technique in which multiple instructions are overlapped in execution, much like an assembly line, by dividing the datapath into successive stages and letting a different instruction occupy each stage every clock cycle. Under ideal conditions, with perfectly balanced stages, the time between instructions on a pipelined processor is
> $$
> \text{Time between instructions}_{pipelined} = \frac{\text{Time between instructions}_{nonpipelined}}{\text{Number of pipe stages}},
> $$
> so the ideal speed-up from pipelining approaches the number of pipeline stages as the number of instructions executed grows large.

# Properties
- One of the [[Great Ideas in Computer Architecture]], and a specific realization of performance via parallelism.
- Improves instruction throughput — the rate at which instructions are started and completed — rather than the latency (execution time) of any individual instruction: a five-stage pipeline still takes 5 clock cycles to complete one instruction, but can have up to 5 instructions in flight simultaneously.
- Real speed-up falls short of the ideal because pipeline stages are rarely perfectly balanced in length and because pipelining itself introduces overhead.
- Depends on properties of the [[Instruction Set Design Principles|instruction set]]: MIPS's fixed instruction length simplifies fetch and decode, its regular placement of source register fields across formats lets decoding and register read proceed together, its restriction of memory operands to loads and stores lets address calculation and memory access occur in separate stages, and its [[Alignment Restriction|alignment restriction]] simplifies memory access itself.
- Instruction latency is the inherent execution time of a single instruction — the number of pipeline stages (or stages between two instructions) it passes through — and is unaffected by pipelining even as throughput improves.
- Its full benefit can be undermined by [[Pipeline Hazard|pipeline hazards]], which prevent an instruction from executing in its otherwise-scheduled clock cycle.
- Deepening the pipeline (adding more, shorter stages) and [[Multiple Issue|multiple issue]] (launching several instructions per stage) are the two primary ways to exploit more [[Instruction-Level Parallelism]].
- Pitfall: pipelining is not as easy as the ideal formula suggests, and its ideas cannot be implemented independent of the underlying technology, since hazards, stage balance, and control complexity are highly sensitive to implementation details.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=295&annotation=H46CL9GN)
