---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Data Hazard[^1]
> A type of [[Pipeline Hazard]] in which a planned instruction cannot execute in its proper clock cycle because data it needs has not yet been produced by an earlier instruction still in the pipeline.

# Properties
- Resolved where possible by forwarding (bypassing): retrieving the missing value directly from internal pipeline buffers as soon as it is computed, rather than waiting for it to reach the programmer-visible registers or memory.
- A load-use data hazard is a data hazard specifically caused by an instruction trying to use data immediately after a load instruction that produces it; forwarding alone cannot resolve this case, since the loaded value is not available until after the instruction that would need to consume it, so a pipeline stall (bubble) — a stall inserted specifically to resolve a hazard — must delay the dependent instruction by one cycle even with forwarding in place.
- A hazard-detection unit checks for this load-use condition (during instruction decode) and, when found, stalls the dependent instruction and its successors while injecting a nop — an instruction that performs no operation and changes no state — into the following pipeline stage.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=301&annotation=T2VM3QFW)
