---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Write-Back Caching (Disk)[^1]
> Write-back caching is Unix's practice of buffering writes to disk in RAM, rather than performing them immediately, until the kernel can conveniently make the actual change on disk.

# Properties
- Transparent to the user and improves performance.
- Flushed automatically by the kernel whenever a filesystem is unmounted with `umount`.
- Can be forced at any other time with the `sync` command; should be run before powering off a system if a filesystem could not be unmounted first.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=102&annotation=9M9BTEE6)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=102&annotation=9GS9DDRE)
