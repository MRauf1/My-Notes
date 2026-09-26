---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Package Dependency[^1]
> A package dependency states that one [[Package (Software)|package]] needs another package, capability, or compatible version for installation or operation.

# Properties
- Repository-aware [[Package Manager|package managers]] use this metadata to calculate a consistent set of changes rather than treating each archive in isolation.[^1]
- Can express more than a simple required name, depending on the distribution's package format: minimum, maximum, or exact version constraints; alternatives, where any one of several providers satisfies a requirement; recommendations or suggestions with weaker semantics; conflicts, breaks, or replacements; and virtual capabilities supplied by more than one package.[^1]
- These rules let a solver choose a set of package versions compatible with the configured repositories, architecture, and installed state; a solution can require upgrades, removals, or a choice between providers, so the proposed transaction should be reviewed before it is approved.[^1]

[^1]: [Linux Journey: Packages](https://labex.io/linuxjourney/courses/packages)
