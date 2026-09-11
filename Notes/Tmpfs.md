---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Tmpfs[^1]
> Tmpfs is the [[Virtual Filesystem|virtual filesystem]], typically mounted on `/run` and other locations, that uses physical memory and [[Swap Space]] as temporary file storage.

# Properties
- Its maximum size is controlled via mount options.
- Overfilling a tmpfs can exhaust system memory and crash programs, so it must be used carefully.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=109&annotation=6RPW33C4)
