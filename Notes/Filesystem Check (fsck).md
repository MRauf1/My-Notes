---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Filesystem Check (fsck)[^1]
> fsck is the program that checks a [[Filesystem]] for internal consistency and repairs it, walking the [[Inode]] table and directory structure to regenerate link counts and a block allocation map (such as a [[Block Bitmap]]) and comparing them against what is actually recorded on disk.

# Properties
- Necessary because the kernel must be able to trust that a mounted filesystem is free of errors; if errors exist, data loss and system crashes can result.[^2]
- Errors typically arise from an unclean shutdown, when the in-memory filesystem cache can fall out of sync with the on-disk data mid-write.[^3]
- Journaling filesystems make this kind of corruption far less common, but do not eliminate the periodic need for a filesystem check.[^3]
- Most distributions run an automatic variant at boot (e.g. `e2fsck -p`, or `fsck -a`), which fixes ordinary problems without prompting and aborts on serious errors; a check that asks many questions in manual mode signals a deeper problem.[^4]
- Data or inodes it cannot reattach to the directory structure ("orphans") are typically placed in the filesystem's `lost+found` directory.[^5]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=115&annotation=3VSZBN79)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=107&annotation=6C2LM393)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=107&annotation=FFH4WGXL)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=108&annotation=GAKPSNXB)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=115&annotation=3VSZBN79)
