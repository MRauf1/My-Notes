---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Device File[^1]
> A device file (or device node) is a representation of a device I/O interface as a file, letting user processes interact with most devices through regular file operations, and letting many devices be used directly with standard programs rather than only by programmers.

# Properties
- There is a limit to what a file interface can expose, so not all devices or device capabilities are accessible through standard file I/O.[^1]
- On Linux, as on other Unix flavors, device files reside in the `/dev` directory.[^2]
- The kernel assigns device files in the order its drivers encounter the corresponding devices, so a device's name in `/dev` reveals little about it and can change between reboots as hardware is reconfigured; modern Linux systems instead use persistent identifiers such as the [[Universally Unique Identifier (UUID)|UUID]] for reliable disk device access.[^3]
- The [[sysfs]] interface complements `/dev` by exposing devices according to their actual hardware attributes rather than discovery order.
- Categorized into [[Block Device|block]], [[Character Device|character]], [[Named Pipe|pipe]], and [[Unix Domain Socket|socket]] devices.
- Automatically configured and made usable by user-space programs through the [[Udev|udev]] system.[^4]
- Listed under `/dev` in the [[Linux Directory Hierarchy]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=71&annotation=9T5KUBIA)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=71&annotation=HF3ERZR6)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=72&annotation=ZV7VKDTX)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=70&annotation=Y7E295W9)
