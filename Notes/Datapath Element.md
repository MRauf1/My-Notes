---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Datapath Element[^1]
> A unit used to operate on or hold data within a processor. In a MIPS implementation, datapath elements include the instruction and data memories, the [[Register File]], the [[Arithmetic Logic Unit|ALU]], adders, and [[Multiplexor|multiplexors]].

# Types
- Combinational element — an operational element with no internal memory, such as an AND gate or an [[Arithmetic Logic Unit|ALU]]; its output is a pure function of its current inputs.
- State element — a memory element, such as a register or a memory, that stores a data value written on an earlier clock cycle and presents it as output until next written.

# Properties
- A state element has at least two inputs, the data value to write and the clock, and an output that reflects the value written on an earlier cycle; a clocking methodology determines when data is valid and stable relative to the clock. Under edge-triggered clocking, all state changes happen at a clock edge, which is what allows a state element to be read and written within the same clock cycle without ambiguity.
- A control signal directs multiplexor selection or a functional unit's operation, in contrast with a data signal, which carries the information a functional unit operates on; a signal is asserted when logically true (high) and deasserted when logically false (low).
- Buses — signals wider than one bit, or more generally any shared collection of lines with multiple sources and uses — are conventionally drawn as thicker lines than single-bit signals.
- A synchronous system reads its data signals only when the clock indicates they are stable; state elements are commonly built from the [[Latch and Flip-Flop|latches and flip-flops]] described in [[Sequential Logic Timing]], which also covers the timing constraints (setup time, hold time, clock skew) an edge-triggered design must satisfy.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=274&annotation=DRDEK5SV)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=727&annotation=2MHTEGKC)
