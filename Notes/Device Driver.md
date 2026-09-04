---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Device Driver[^1]
> A device driver is kernel software that acts as the interface between a hardware device and user processes, presenting a uniform programming interface even when different devices of the same kind do not share one.

# Properties
- Traditionally part of the [[Kernel (Operating System)|kernel]], because improper device access (such as a user process turning off the power) could crash the machine.
- Devices are typically accessible only in [[Kernel Mode]].
- One of the [[Kernel (Operating System)|kernel's]] four general responsibility areas, alongside [[Process Management]], memory, and [[System Call|system calls]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
