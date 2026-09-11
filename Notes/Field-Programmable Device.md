---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Field-Programmable Device (FPD)[^1]
> An integrated circuit containing combinational logic — and possibly memory devices — that the end user, rather than the manufacturer, can configure after fabrication ("in the field").

# Types
- Programmable logic device (PLD) — an integrated circuit whose combinational logic function is configured by the end user.
- Simple programmable logic device (SPLD) — a PLD usually built from a single [[Structured Logic (PLA and ROM)|PLA]] or a programmable array logic (PAL), which fixes a programmable AND-plane followed by a fixed OR-plane.
- Field-programmable gate array (FPGA) — a configurable integrated circuit containing both combinational logic blocks and flip-flops (see [[Latch and Flip-Flop]]), so it can implement sequential as well as combinational designs.

# Properties
- An antifuse is a structure that, once programmed, permanently connects two wires — one mechanism used to fix a device's configuration.
- An FPGA's configurable cells are commonly called lookup tables (LUTs), since each consists of a small amount of logic together with a small RAM used to realize an arbitrary function of its inputs.
- The synthesized target for a [[Hardware Description Language]] design when the goal is a reconfigurable chip rather than a fixed, fabricated one.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=757&annotation=Z4TEP6AA)
