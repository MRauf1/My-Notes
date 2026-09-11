---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Process Memory Layout[^1]
> The conventional division of a running program's address space into segments: the text segment holding its machine code, the static data segment holding constants and static variables, the heap for dynamically growing and shrinking data structures, and the stack for procedure calls.

# Types
- Text segment — holds the machine language code for the program's routines; readable (for function pointers) but not writable, and by default the only executable section of the program.[^2]
- Data segment — holds constants and other statically sized variables, such as fixed-length arrays; in practice split into an initialized part, readable and writable, holding globals and statics with explicit initial values, and an uninitialized part (the BSS), whose globals and static-duration variables are implicitly zeroed, both for security and to speed up process startup. Starts at the end of the text segment and is fixed in size, since the number of globals is known at compile time; its end is the [[Program Break]], extendable via `brk` / `sbrk`.[^2]
- Heap — holds data structures like linked lists that grow and shrink during execution, and is the segment to use for an object whose lifetime is manually controlled or whose size cannot be determined at compile time; writable but not executable. Starts at the top of the text segment and grows upward as `malloc` pushes the [[Program Break]] up, and can be exhausted if the system is constrained or the program runs out of addresses.[^2] Managed on the program's behalf by a [[Heap Allocator]].
- [[Call Stack]] — holds each active procedure's [[Procedure Frame]]; writable but not executable, and statically allocated by default with only a fixed amount of space available to write into.[^2]

# Properties
- The stack is placed at the high end of memory and grows downward, while the heap grows upward from the low end, allowing the two segments to efficiently share the address space between them as they wax and wane.
- Managed by the [[Operating System]] and populated by the [[Loader]] when a program's [[Executable File]] is started; see also [[Virtual Memory]] and [[Process (Computing)]].
- Segment start addresses are randomized by [[Address Space Layout Randomization]] as a security measure, though this can be disabled (for instance by compiling with a DEBUG flag) to keep addresses constant while debugging.[^2]

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=127&annotation=H63RM6T4)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=91&annotation=7UJU3A3P)
