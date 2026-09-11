---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] EFI System Partition[^1]
> The EFI System Partition (ESP) is the special filesystem that [[UEFI]] firmware boots from, containing an `efi` directory with one vendor-named subdirectory per boot loader (e.g. `efi/grub`), each holding that loader's `.efi` file and supporting files.

# Properties
- A boot loader placed here must be built specifically for UEFI rather than reused from a BIOS build, and must be "announced" to the firmware once installed.[^2]
- The firmware can navigate the ESP directly and execute any operating system loader it contains.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=133&annotation=J93QZDDI)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=133&annotation=DI3B7S54)
