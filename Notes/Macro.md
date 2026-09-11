---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Macro[^1]
> A pattern-matching and replacement facility that provides a simple mechanism for naming a frequently used sequence of instructions, so that a program can refer to the whole sequence by one name.

# Properties
- Expanded by the [[Assembler]] before ordinary assembly, substituting a macro's formal parameters with the actual arguments supplied at each call site.
- Distinct from a [[Pseudoinstruction]]: a pseudoinstruction is a single assembler-recognized instruction expanded into a fixed, short machine-instruction sequence, while a macro is a programmer-defined, arbitrarily long named sequence expanded by simple textual substitution.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=601&annotation=D6PNHCXN)
