---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Jump Address Table (Jump Table)[^1]
> A table of addresses of alternative instruction sequences, stored as an array of words containing addresses that correspond to labels in the code.

# Properties
- An efficient way to implement a switch statement: the program indexes into the table, loads the appropriate address into a register, and performs an unconditional jump to the address held in that register (a register-indirect jump, as with the MIPS `jr` instruction), rather than testing a chain of [[Conditional Branch|conditional branches]].
- Becomes more advantageous relative to a chain of if-then-else tests as the number of alternatives grows.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=118&annotation=6929VTKH)
