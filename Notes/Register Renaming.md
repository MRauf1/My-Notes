---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Register Renaming[^1]
> The renaming of registers, by the compiler or the hardware, to remove antidependences.

# Properties
- An antidependence (name dependence) is an ordering forced merely by the reuse of a register name across two instructions, rather than by a true dependence carrying a value from one instruction to another; renaming one of the two conflicting uses to a different register eliminates the artificial ordering constraint.
- Frees [[Multiple Issue|multiple-issue]] and [[Dynamic Pipeline Scheduling|dynamically scheduled]] hardware to reorder or overlap instructions that would otherwise appear to conflict only because they happen to reuse the same architectural register.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=361&annotation=ZMTQ7ULA)
