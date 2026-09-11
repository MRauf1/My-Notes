---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Initial RAM Filesystem (Initrd)[^1]
> The initial RAM filesystem (initrd) is a filesystem image that a [[Boot Loader|boot loader]] loads into memory before loading and executing the kernel, supplying files — such as [[Loadable Kernel Module|loadable kernel modules]] — that the kernel may need before it can mount the true root filesystem.

# Properties
- Specified to [[GRUB]] via its `initrd` command.
- Implemented as initramfs: since the kernel does not talk to PC firmware ([[BIOS]]/[[UEFI]]) to read disks, it needs a driver — often a [[Loadable Kernel Module|loadable module]], hence a file — for whatever hardware holds the true root filesystem; the boot loader loads a small archive of driver modules and utilities, the kernel unpacks that archive into a temporary RAM filesystem (initramfs) mounted at `/`, and hands off to init there so those utilities can load the needed driver modules, mount the real root filesystem, and start the true init.[^2][^3]
- Can be omitted from the boot loader configuration if the kernel already has every driver it needs to mount the real root filesystem, typically saving a couple of seconds of boot time — though features such as mount-by-UUID may depend on it with generic distribution kernels.[^4]
- Built by distribution-supplied utilities such as `dracut` or `mkinitramfs`, rather than by hand.[^5]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=134&annotation=4EV2ELLS)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=170&annotation=SMIDHQCX)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=170&annotation=V3GEGR2K)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=171&annotation=PLWHLJE8)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=171&annotation=ZN939LJS)
