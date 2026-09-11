---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Assembler[^1]
> A program that translates a symbolic version of instructions ([[Assembly Language]]) into the binary version ([[Machine Language]]).

# Properties
- A type of [[Systems Software]].
- Historically the first program pioneers wrote to use the computer to help program the computer, translating from symbolic notation to binary.
- Sits below the [[Compiler]] in the translation chain: high-level language → (compiler) → assembly language → (assembler) → machine language.
- Translates in two major steps: first finding the memory location of every label so that symbolic names are known before instructions using them are translated, then translating each statement by combining the numeric equivalents of opcodes, register specifiers, and labels into a legal instruction; a label used before it is defined (a forward reference) is commonly resolved by backpatching — building an incomplete binary encoding on a first pass, then returning to fill in labels once every definition is known.
- Recognizes a [[Macro]] as well as assembler directives — pseudo-operations, conventionally beginning with a period, that guide translation (such as declaring a data segment) without themselves producing machine instructions.
- Produces an [[Object File]] as output; since it processes each source file individually, it can only fully resolve local labels (usable only within their own file) and must pass along a list of external (global) labels and other unresolved references — ones needing more information from outside the file — for the [[Linker]] to resolve.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=37&annotation=3GCC68XY)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=607&annotation=IBFZNYBA)
