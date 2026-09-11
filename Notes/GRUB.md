---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] GRUB[^1]
> GRUB (GRand Unified Bootloader) is the [[Boot Loader]] in common use on Linux, providing filesystem navigation for kernel image and configuration selection.

# Properties
- Starts the Linux kernel rather than using it: its own configuration language, its own "kernel," and its own `insmod` module-loading command are entirely internal to GRUB and independent of the Linux kernel, despite the borrowed terminology.[^2]
- Only the `root` [[Kernel Parameter|kernel parameter]] (passed to the `linux` command) names the actual root filesystem; every other "root" in a GRUB configuration refers to the separate GRUB root — the filesystem GRUB itself searches for kernel and RAM filesystem images.[^3]
- Its `linux` command names the kernel image file (e.g. `/boot/vmlinuz-...`), and its `initrd` command names the [[Initial RAM Filesystem (Initrd)|initial RAM filesystem]] file, both loaded from the GRUB root.[^4]
- Boot sequence: firmware finds and executes boot code → the GRUB core loads and initializes, gaining disk and filesystem access → GRUB locates its boot partition and loads a configuration there → the user may edit that configuration → GRUB executes it, loading any further modules it needs → GRUB boots the kernel named by the configuration's `linux` command.[^5]
- The GRUB core can reside partly between the [[Master Boot Record|MBR]] and the first partition, in a regular partition, or in a special boot partition such as a GPT boot partition or an [[EFI System Partition]].[^6]
- Can load and run a separate, independent boot loader installed on a specific disk partition, a technique called [[Chainloading]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=123&annotation=3WW5DWZG)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=125&annotation=DXACUH39)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=125&annotation=Z3YRBRFV)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=125&annotation=KEW75Z67)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=134&annotation=3NAFWILK)
[^6]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=134&annotation=3HP8PFCP)
