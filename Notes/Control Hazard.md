---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Control Hazard (Branch Hazard)[^1]
> A type of [[Pipeline Hazard]] in which the proper instruction cannot execute in the proper pipeline cycle because the instruction fetched is not the one needed: the flow of instruction addresses, typically because of an unresolved [[Conditional Branch|branch]], is not what the pipeline expected.

# Types
- Stall — fetch nothing new until the branch outcome and target are known; simple but slow, and worse the later in the pipeline the branch is resolved.
- Predict not taken (or predict taken) — guess a fixed outcome and keep fetching sequentially, flushing (discarding, by clearing control signals so the instruction becomes a nop) the fetched instructions if the guess turns out wrong; see [[Dynamic Branch Prediction]] for guessing based on runtime history instead of a fixed rule.
- Delayed branch — always execute the next sequential instruction (the branch delay slot) before the branch actually takes effect, so the compiler can fill that slot with a useful, branch-independent instruction; used by the MIPS architecture, but limited to a single delay slot and has lost favor as pipelines have grown longer and issue multiple instructions per cycle.

# Properties
- Moving branch resolution earlier in the pipeline reduces the number of instructions that must be flushed on a taken branch, at the cost of added hardware complexity to compute the branch target and evaluate the condition sooner.
- Longer pipelines worsen every solution to control hazards, since either the stall grows longer or a misprediction discards more in-flight instructions.
- An [[Exception (Computer Architecture)|exception]] is handled as a form of control hazard in a pipelined processor.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=304&annotation=MR623GR3)
