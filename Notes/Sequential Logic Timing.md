---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Sequential Logic Timing[^1]
> The set of timing constraints that a clocked [[Datapath Element|state element]] such as a [[Latch and Flip-Flop|flip-flop]] must satisfy for its stored value to be sampled and updated correctly.

# Types
- Setup time — the minimum time the input must be valid before the triggering clock edge.
- Hold time — the minimum time the input must remain valid after the clock edge.
- Propagation time — the time required for a flip-flop's input to propagate through to its output.
- Clock skew — the difference in absolute time between when two different state elements see the same nominal clock edge, since the clock signal does not reach every element simultaneously.

# Properties
- Edge-triggered clocking, in which all state changes occur exactly at a clock edge, is the alternative to level-sensitive clocking, in which state can change throughout a high or low clock level rather than instantaneously.
- Metastability occurs if a signal is sampled outside its required setup and hold window, leaving the sampled value in an indeterminate region between a logical 0 and 1; a synchronizer failure results if different downstream logic blocks reading that unsettled flip-flop output disagree about whether it is a 0 or a 1.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=732&annotation=VQQNN5M8)
