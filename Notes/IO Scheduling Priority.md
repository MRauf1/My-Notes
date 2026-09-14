---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] I/O Scheduling Priority[^1]
> The I/O priority (PRIO) is a value, analogous to a process's CPU [[Scheduling Priority (Linux)|scheduling priority]], that determines how quickly the kernel schedules a process's I/O reads and writes.

# Properties
- Written as a scheduling class and a priority level, such as `be/4`, where `be` is the scheduling class and the number is the priority level within it.[^1]
- Lower numbers are more important, just as with CPU priorities: the kernel gives more time for I/O to a process with `be/3` than one with `be/4`.[^1]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=212&annotation=CDSSYFTI)
