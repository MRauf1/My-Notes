---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] UEFI[^1]
> UEFI (Unified Extensible Firmware Interface) is the modern successor to the [[BIOS]], a PC firmware standard with features such as a built-in shell and the ability to read partition tables and navigate filesystems directly.

# Properties
- The [[Globally Unique Identifier Partition Table (GPT)|GPT]] partitioning scheme is part of the UEFI standard.[^1]
- Boots from a dedicated [[EFI System Partition]] rather than from boot code stashed outside any filesystem.
- Supports [[Secure Boot]].
- Makes it easy to support loading other operating systems, since multiple boot loaders can be installed side by side in the EFI partition.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=133&annotation=UNVW3V3X)
