---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Thrashing[^1]
> Thrashing is the condition in which the kernel rapidly swaps processes' memory to and from disk because the system is low on memory.

# Properties
- Causes many processes to become ready to run without their memory actually being available, so they remain in the ready-to-run state — and contribute to the [[Load Average]] — for much longer than they normally would.[^1]
- Checking how much real memory is used for caches and buffers, e.g. with the `free` command or `/proc/meminfo`, is one of the simplest ways to assess whether a memory shortage is responsible for a performance problem.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=206&annotation=XSM7ZS86)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=206&annotation=VSDZYPUA)
