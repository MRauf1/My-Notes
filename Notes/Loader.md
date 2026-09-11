---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Loader[^1]
> A systems program that places an [[Executable File|object program]] in [[Main Memory]] so that it is ready to execute.

# Properties
- A type of [[Systems Software]], invoked by the [[Operating System]] once an executable file is on disk.
- Establishes a running program's [[Process Memory Layout]] (text, static data, heap, and stack segments) before transferring control to the program's entry point.
- Works alongside dynamic linking machinery when a program uses a [[Dynamically Linked Library]], since those library routines are not linked and loaded until the program actually runs.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=152&annotation=TJZRFSPI)
