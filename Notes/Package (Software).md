---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Package (Software)[^1]
> A package is a unit of Linux software distribution that groups installable files together with metadata, so a [[Package Manager|package manager]] can track its versions, dependencies, ownership, checksums, and lifecycle actions.

# Properties
- A binary package can contain executables, libraries, documentation, default configuration, service definitions, and other resources, alongside metadata such as its name and version, target architecture and distribution context, declared [[Package Dependency|dependencies]] and conflicts, file lists and integrity information, and optional scripts or triggers used during lifecycle operations.[^1]
- Not every package is an interactive application: a package can instead provide a library, kernel component, language data, fonts, debug symbols, or metadata that depends on a collection of other packages.[^1]

[^1]: [Linux Journey: Packages](https://labex.io/linuxjourney/courses/packages)
