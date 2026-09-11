---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Dynamically Linked Library (DLL)[^1]
> Library routines that are linked to a program during execution rather than by the [[Linker]] before the program runs. Both the program and the library keep extra information about the location and names of nonlocal procedures so that this linking can happen at run time.

# Properties
- Avoids the disadvantages of static linking (wasted disk and memory space from duplicated library copies, and the need to re-link whenever a library changes) at the cost of extra space for dynamic-linking information and run-time linking overhead.
- Under lazy procedure linkage, each library routine is linked only the first time it is called, paying a one-time overhead followed thereafter by only a single indirect jump per call, with no extra overhead on return.
- Loaded by the [[Loader]] together with the calling program.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=152&annotation=L45EKFZG)
