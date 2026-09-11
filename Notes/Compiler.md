---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Compiler[^1]
> A program that translates statements in a [[High-Level Programming Language]] into [[Assembly Language]] statements.

# Properties
- A type of [[Systems Software]].
- Sits above the [[Assembler]] in the translation chain from a high-level program down to [[Machine Language]]: high-level language → (compiler) → assembly language → (assembler) → machine language.
- A [[Just-In-Time Compilation|just-in-time compiler]] performs this translation at runtime instead of fully ahead of time.
- Can instead generate [[Machine Language]] directly, skipping the intermediate assembly step and its [[Assembler]]; doing so compiles faster but forces the compiler to absorb tasks — resolving addresses, encoding binary instructions — an assembler would otherwise handle, trading compiler simplicity for compilation speed.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=37&annotation=Y836ELWU)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=607&annotation=VDP8CMU8)
