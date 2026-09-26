---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Package Repository[^1]
> A package repository publishes packages together with indexes and release metadata that describe available package names, versions, architectures, checksums, dependencies, and repository sections.

# Properties
- A [[Package Manager|package manager]] downloads those indexes, selects versions compatible with its configured distribution and architecture, verifies repository authentication, and retrieves the required package files; the client caches a local catalog so it can search and resolve packages without downloading every archive first.[^1]
- Can install packages and lifecycle scripts with system privileges, so adding a new repository extends the system's software trust boundary. Before doing so: prefer the distribution repository when it meets the requirement, confirm the publisher, supported release, architecture, and signing-key fingerprint, use a dedicated source file and scoped keyring, inspect package and dependency changes before installing, and document how to disable the source and remove its packages later.[^1]
- Should never be added by disabling signature checks or piping an unaudited remote script into a privileged shell.[^1]

[^1]: [Linux Journey: Packages](https://labex.io/linuxjourney/courses/packages)
