---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Linker (Link Editor)[^1]
> A systems program that combines independently assembled [[Object File|object files]] with library routines and resolves all undefined labels into a single [[Executable File]].

# Properties
- A type of [[Systems Software]], letting each procedure be compiled and assembled independently so that changing one line requires reprocessing only that procedure, rather than the whole program.
- Follows three steps: it places code and data modules symbolically in memory, determines the addresses of data and instruction labels using each object file's symbol table and relocation information, and relocates absolute (non-register-relative) references to reflect a module's true location in memory — much like a text editor finding old addresses and replacing them with new ones.
- Its output can itself be only partially linked, as with library routines that still have unresolved addresses, producing further object files rather than a final executable.
- Static linking (performed before a program runs) is the fastest way to call library routines but wastes disk and memory space when many programs link the same library, and requires re-linking if a library changes; see [[Dynamically Linked Library]] for the alternative.
- Enables separate compilation: splitting a program across many files, each of which can be compiled or assembled without knowledge of the others' contents, so that changing one file requires reprocessing only that file before the linker re-merges the results.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=149&annotation=D6J7XZFR)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=615&annotation=2FPL9DI4)
