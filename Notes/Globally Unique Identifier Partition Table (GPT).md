---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Globally Unique Identifier Partition Table (GPT)[^1]
> GPT is a [[Partition Table|partition table]] standard, part of [[UEFI]], whose own table information resides in the disk area immediately after the [[Master Boot Record|MBR]] — leaving the MBR itself untouched for backward compatibility.

# Properties
- Incompatible with the multi-stage boot-loader trick used to boot MBR-formatted disks via [[BIOS]], since a boot loader's code would otherwise occupy the very space GPT uses for its own table.[^2]
- Worked around by a small, specially tagged BIOS boot partition that gives a full boot loader somewhere to reside when booting a GPT disk via BIOS.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=133&annotation=RN9L3A78)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=133&annotation=AN52QGH8)
