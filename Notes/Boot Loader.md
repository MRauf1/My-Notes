---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Boot Loader[^1]
> A boot loader is the program a machine's firmware loads and runs first, whose task is to locate a kernel image, load it into memory, and start it with a set of [[Kernel Parameter|kernel parameters]].

# Properties
- Faces a "chicken-or-egg" problem: the kernel and its parameters typically reside on the root filesystem, but the kernel isn't yet running to traverse that filesystem, and the kernel's own high-performance disk drivers aren't yet available either.[^2]
- On PCs, boot loaders instead access disks through firmware ([[BIOS]] or [[UEFI]]) using Linear Block Addressing, a universal but comparatively low-performance mode of disk access; the kernel instead uses its own high-performance drivers once running.[^3]
- Most modern boot loaders can read partition tables and have built-in read-only filesystem support, letting them find and read files directly, which makes them far easier to dynamically configure.[^4]
- Core functionality: selecting among multiple kernels, switching between sets of kernel parameters, letting a user manually override or edit the kernel image and its parameters (e.g. to enter single-user mode), and booting other operating systems.[^5]
- [[GRUB]] is the boot loader in common use on Linux.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=122&annotation=PRLSTUAS)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=122&annotation=QZIMEIBX)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=122&annotation=IHG7VGQX)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=122&annotation=S3S99A3T)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=122&annotation=JNJBRCN9)
