---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Pipeline Hazard[^1]
> A situation in which the next instruction cannot execute in its normally scheduled clock cycle of a pipelined processor.

# Types
- Structural hazard — the hardware does not support the particular combination of instructions scheduled to execute simultaneously in a given clock cycle.
- [[Data Hazard]] — an instruction needs data that is not yet available because an earlier instruction still in the pipeline has not produced it.
- [[Control Hazard]] — the instruction that was fetched is not the one actually needed, because the flow of instruction addresses (typically due to a branch) was not what the pipeline expected.

# Properties
- A hazard is commonly resolved either by forwarding needed values internally, or by inserting a [[Data Hazard|pipeline stall]] that delays later instructions until the hazard clears.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=300&annotation=KNI6IATP)
