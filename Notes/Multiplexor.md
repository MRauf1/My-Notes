---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Multiplexor (Data Selector)[^1]
> A device that selects one of several data inputs to pass through to its output, based on the setting of its control lines.

# Properties
- A [[Truth Table|combinational]] datapath element; see [[Datapath Element]].
- In a processor, its control lines are typically set by the [[Control Unit]] based on information taken from the [[Instruction]] being executed, or directly from a datapath signal such as the ALU's zero output when selecting the next [[Program Counter]] value for a [[Conditional Branch]].
- The control signal that picks which input becomes the output is called the selector value (control value).

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=269&annotation=IBB233Y5)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=689&annotation=NVTHSTUE)
