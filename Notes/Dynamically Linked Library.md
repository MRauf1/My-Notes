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
- On ELF-based Linux systems, an executable can record a needed library name, such as a SONAME; the dynamic linker locates a matching installed library when the program starts, and package metadata usually represents this requirement as a [[Package Dependency|dependency]] on the package or capability providing the compatible library.[^2]
- Having a file with a similar library name is not sufficient: the required [[Application Binary Interface|ABI]], architecture, symbols, and sometimes minimum version must all match, so replacing a distribution library manually can break every dependent program even if the filename appears correct.[^2]
- Package maintainers encode these library relationships and coordinate transitions when an ABI changes; native libraries should stay under [[Package Manager|package-manager]] control, with supported parallel-installation, container, environment, or build mechanisms used instead for software that needs a conflicting version.[^2]

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=152&annotation=L45EKFZG)
[^2]: [Linux Journey: Packages](https://labex.io/linuxjourney/courses/packages)
