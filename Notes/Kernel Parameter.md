---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Kernel Parameter[^1]
> A kernel parameter is a text-based parameter that a [[Boot Loader|boot loader]] passes to the kernel at startup, describing how the kernel should start — for instance, its diagnostic output verbosity or driver-specific options.

# Properties
- The `root` parameter is critical: it names the location of the root filesystem, without which the kernel cannot find [[Init Process|init]] and so cannot perform the user space start.[^2]
- The root filesystem can be named either as a [[Device File|device file]] or, more commonly on modern desktop systems, by [[Universally Unique Identifier (UUID)|UUID]].[^3]
- A parameter the kernel does not recognize is simply saved and later passed on to init during the user space start.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=121&annotation=36TQP2V8)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=121&annotation=LFUIEWJ2)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=121&annotation=Z7C22RSZ)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=121&annotation=9QIHCIH2)
