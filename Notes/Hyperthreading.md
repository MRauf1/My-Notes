---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Hyperthreading[^1]
> Intel's implementation of [[Hardware Multithreading|simultaneous multithreading]], which lets a single physical [[Central Processing Unit|core]] appear to the [[Operating System]] as several virtual cores. The [[Operating System]] schedules [[Process (Computing)|processes]] or [[Thread|threads]] onto these virtual cores, while the physical core interleaves the execution of each.

# Properties
- Not full parallel execution: while the core is stalled waiting for one memory access to complete, it executes a few instructions of another process or thread instead of idling, so the gain comes from overlapping stalls rather than truly running multiple threads simultaneously.
- Increases the number of instructions executed in a given amount of time without adding physical cores, which can reduce the number of cores needed to power smaller devices.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=23&annotation=T6R867VD)
