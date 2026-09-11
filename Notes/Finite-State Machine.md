---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Finite-State Machine (Sequential Logic)[^1]
> A sequential logic function consisting of a set of inputs and outputs, a next-state function that maps the current state and the inputs to a new state, and an output function that maps the current state (and possibly the inputs) to a set of asserted outputs.

# Properties
- The general hardware model underlying sequential [[Datapath Element|state elements]] such as a [[Control Unit]] or a hardware predictor: a 2-bit branch predictor, for instance, is naturally specified as a small finite-state machine over its prediction states; see [[Dynamic Branch Prediction]].
- The next-state function is itself a combinational function of the current state and inputs, computed anew each clock cycle; the machine's state is held in [[Datapath Element|state elements]] that are updated on each clock edge.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=486&annotation=AW45GZ3C)
