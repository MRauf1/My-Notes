---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Main Memory[^1]
> Main memory is the hardware storage area holding the bits that make up the running kernel, all processes, and all input/output passing through peripheral devices.

# Properties
- Composed of [[Bit|bits]]; a particular arrangement of these bits is called a [[State (Computing)|state]].
- A CPU only reads its instructions and data from, and writes data back out to, main memory.
- The [[Kernel (Operating System)|kernel]] subdivides main memory among [[Process (Computing)|processes]], tracking what is allocated, shared, or free.
- Partitioned into [[Kernel Space]], accessible only to the kernel, and [[User Space]], accessible to user processes.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
