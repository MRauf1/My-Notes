---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Process Memory Layout[^1]
> The conventional division of a running program's address space into segments: the text segment holding its machine code, the static data segment holding constants and static variables, the heap for dynamically growing and shrinking data structures, and the stack for procedure calls.

# Types
- Text segment — holds the machine language code for the program's routines.
- Static data segment — holds constants and other statically sized variables, such as fixed-length arrays.
- Heap — holds data structures like linked lists that grow and shrink during execution.
- [[Call Stack]] — holds each active procedure's [[Procedure Frame]].

# Properties
- The stack is placed at the high end of memory and grows downward, while the heap grows upward from the low end, allowing the two segments to efficiently share the address space between them as they wax and wane.
- Managed by the [[Operating System]] and populated by the [[Loader]] when a program's [[Executable File]] is started; see also [[Virtual Memory]] and [[Process (Computing)]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=127&annotation=H63RM6T4)
