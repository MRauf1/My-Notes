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
- Also called primary memory. It is volatile: it retains data only while receiving power, and typically consists of dynamic random access memory (DRAM) in today's computers.[^2]
- Sits above [[Secondary Memory]] and below [[Cache Memory]] in the [[Memory Hierarchy]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=46&annotation=4UAPI527)
