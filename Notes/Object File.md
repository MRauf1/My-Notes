---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Object File[^1]
> The output of an [[Assembler]]: a combination of machine language instructions, data, and information needed to place those instructions properly in memory.

# Properties
- Contains a symbol table matching the names of labels used in branches and data transfer instructions to the addresses of the memory words those instructions occupy, so that the assembler (and later the [[Linker]]) can resolve them.
- Independently assembled object files are combined and have their unresolved labels resolved by the linker into an [[Executable File]].
- Organized into segments matching a program's eventual [[Process Memory Layout]]: a text segment holding machine code, and a data segment holding a binary representation of the program's initialized (static) data.
- Carries relocation information identifying which instructions and data words depend on an absolute address — a variable's or routine's actual, final address in memory — so the linker knows what to rewrite once each module's location is fixed.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=148&annotation=KI64TPUY)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=610&annotation=9A88XAWE)
