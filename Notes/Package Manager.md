---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Package Manager[^1]
> A package manager is the tool that records a Linux system's installed [[Package (Software)|package]] state and coordinates changes across packages.

# Properties
- Installing from trusted distribution [[Package Repository|repositories]] usually provides consistent dependency resolution, signature verification, security updates, and clean removal; a manually copied binary or source installation can be appropriate, but it does not automatically enter that managed lifecycle.[^1]
- A cryptographically valid package proves association with a trusted signing key, not that arbitrary third-party software is safe or suitable; trust still depends on repository configuration and signing keys, so an external source should be assessed before being granted installation privileges.[^1]
- A dependency problem can arise from mixed repositories, interrupted operations, manually installed archives, held versions, removed files, or incompatible third-party software; the right response is to read the package manager's diagnostics, refresh only trusted repository metadata, inspect held or pinned versions, and review a proposed repair — never to delete package-database files or force an install blindly.[^1]
- A low-level package installer can unpack an archive without fetching all dependencies; a higher-level repository tool is usually safer for ordinary installation, since it resolves the complete transaction.[^1]
- Building from source can supply a version or feature unavailable in configured repositories, but it moves integration, update, and trust work from the distribution onto the user; a supported distribution package is preferable when it meets the requirement.[^1]

[^1]: [Linux Journey: Packages](https://labex.io/linuxjourney/courses/packages)
