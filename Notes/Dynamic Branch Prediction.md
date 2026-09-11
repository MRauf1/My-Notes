---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Dynamic Branch Prediction[^1]
> Predicting the outcome of a [[Conditional Branch|branch]] at runtime using runtime information about that branch's own recent behavior, rather than a single rigid, compile-time rule applied uniformly to all branches.

# Types
- Branch prediction buffer (branch history table) — a small memory, indexed by the low-order bits of a branch's address, holding one or more bits that record whether that branch was recently taken.
- 2-bit predictor — requires a prediction to be wrong twice in a row before it is changed, avoiding the misprediction a simple 1-bit predictor would make on a single atypical iteration of an otherwise regular loop.
- Correlating predictor — combines a branch's own local history with the global history of recently executed branches, using the latter as extra index bits, to improve accuracy over either alone.
- Tournament predictor — runs multiple predictors (e.g. one local, one global) side by side per branch and uses a selector, itself updated like a simple predictor, to choose whichever has recently been more accurate.
- Branch target buffer — caches the destination PC or destination instruction for a branch, organized like a tagged cache, so the target is available without waiting for it to be recomputed.

# Properties
- Achieves over 90% prediction accuracy in practice, letting a processor speculatively fetch and execute down the predicted path; see [[Speculative Execution]].
- On a misprediction, the pipeline control must ensure the wrongly fetched instructions have no effect and must restart fetching from the correct address.
- Its relative cost has fallen as Moore's Law increases the transistors available per chip, contributing to delayed branching's decline in popularity relative to dynamic prediction.
- Conditional move instructions offer an alternative way to reduce the number of conditional branches altogether: they conditionally update a destination register instead of the [[Program Counter]], acting as a nop when the condition fails.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=344&annotation=LNLGANEF)
