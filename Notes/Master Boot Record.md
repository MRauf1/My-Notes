---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Master Boot Record[^1]
> The Master Boot Record (MBR) is the traditional PC [[Partition Table|partition table]] format, whose small boot-code area (441 bytes) the [[BIOS]] loads and executes after its Power-On Self-Test.

# Properties
- Too small to hold a full boot loader, so this area typically just loads the rest of the boot loader's code — a multi-stage boot loader — whose remaining pieces are stuffed into the space between the MBR and the disk's first partition.[^1]
- Not very secure, since that space between the MBR and the first partition can be overwritten by anything, yet most boot loaders (including most GRUB installations) still use it.[^2]
- Incompatible with GPT-partitioned disks under BIOS booting, since GPT's own table data occupies the space right after the MBR; GPT otherwise leaves the MBR itself untouched for backward compatibility.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=132&annotation=27I99C5D)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=132&annotation=PWPEAKHH)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=133&annotation=RN9L3A78)
