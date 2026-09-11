---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Latch and Flip-Flop[^1]
> A latch is a [[Datapath Element|state element]] whose output equals its stored value and whose state changes whenever its inputs change while the clock is asserted (level-sensitive). A flip-flop is a state element whose output likewise equals its stored value, but whose internal state changes only on a clock edge (edge-triggered), not for as long as a level is asserted.

# Types
- D flip-flop — a flip-flop with a single data input, which stores that input's value into its internal memory at the clock edge.

# Properties
- The basic building blocks from which larger state elements, such as a [[Register (Computer Architecture)|register]] or a [[Register File]], are constructed.
- Correct operation requires respecting the timing constraints described in [[Sequential Logic Timing]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=730&annotation=8CFAJAU9)
