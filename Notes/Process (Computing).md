---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Process (Computing)[^1]
> A process (or user process) is a running program managed by the kernel, regardless of whether a user directly interacts with it. All processes running on a system collectively make up user space.

# Properties
- Runs in [[User Mode]] and occupies [[User Space]].
- Is, in essence, a [[State (Computing)|state]] (or image) residing in memory.
- Created via [[Fork and Exec|fork() and exec()]].
- Has a user owner and is said to run as that owner (see [[User (Unix)]]).
- Managed by [[Process Management]], including [[Context Switch|context switching]] between processes sharing a CPU.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
