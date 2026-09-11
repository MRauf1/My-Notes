---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Hardware Description Language (HDL)[^1]
> A programming language for describing hardware, used both to simulate a hardware design and, via hardware synthesis tools (computer-aided design software that generates a gate-level design from a behavioral description), as input for actually generating the hardware itself. Verilog and VHDL are the two most common HDLs.

# Types
- Behavioral specification — describes how a digital system operates functionally, without committing to a particular structural implementation.
- Structural specification — describes how a digital system is organized as a hierarchical connection of lower-level elements.

# Properties
- In Verilog, `wire` names a combinational signal and `reg` names a register; a sensitivity list specifies which signals must change before an `always` block is re-evaluated.
- Verilog assignments are either blocking, which completes before the next statement executes, or nonblocking, which evaluates every right-hand side first and only then updates every left-hand side — a distinction that matters for correctly modeling [[Datapath Element|sequential logic]] update order.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=699&annotation=Z9JL9HPQ)
