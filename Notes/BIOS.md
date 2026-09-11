---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] BIOS[^1]
> The Basic Input/Output System (BIOS) is the traditional PC firmware that a [[Boot Loader|boot loader]] uses to access disks, via Linear Block Addressing — a universal but comparatively low-performance mode of access.

# Properties
- Superseded by [[UEFI]].
- The kernel does not rely on the BIOS for disk access once running; it uses its own high-performance drivers instead, making boot loaders typically the BIOS's only user.
- After its Power-On Self-Test (POST), the BIOS loads and executes the small boot-code area of the [[Master Boot Record]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=122&annotation=IHG7VGQX)
