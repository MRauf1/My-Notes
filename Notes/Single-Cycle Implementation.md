---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Single-Cycle Implementation[^1]
> An implementation in which every instruction executes in exactly one clock cycle. It is easy to understand and design but too slow to be practical.

# Properties
- Because the clock cycle must be long enough to cover the worst-case delay across all instructions, no instruction can finish faster than the slowest one — techniques that reduce the delay of the common case but not the worst-case cycle time yield no benefit.
- Directly violates [[Make the Common Case Fast]], one of the [[Great Ideas in Computer Architecture]].
- Contrasted with [[Pipelining]], which lets instructions of differing natural latency overlap in execution instead of forcing every instruction into one uniformly long cycle.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=293&annotation=X9A9H8TJ)
