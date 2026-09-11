---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git Snapshot Model[^1]
> Unlike delta-based version control systems, which store the changes made to each file over time, [[Git]] stores its data as a series of snapshots: every time a commit is made, Git records what all of the project's tracked files look like at that moment.

# Properties
- If a file has not changed between snapshots, Git does not store the file's content again but instead stores a link to the identical file it has already stored from a previous commit, so Git effectively thinks of its history as a stream of snapshots.
- Every object is checksummed with a SHA-1 hash before being stored, and Git subsequently refers to it by that hash rather than by its filename, making its object store content-addressable.
- Because content is retrieved by the hash of its own bytes, it is impossible to alter a file's or directory's content without Git detecting the change, so data cannot be corrupted or lost in transit undetected.
- This combination of snapshotting and content-addressed storage makes Git behave more like a small filesystem with powerful tools built on top of it than like a traditional [[Version Control System]]. At its core, this content-addressable filesystem is simply a key-value store: any content can be inserted into it, and Git hands back a unique key that can later be used to retrieve exactly that content — each such stored piece of content is a [[Git Object]].
- Although each commit conceptually records a full snapshot, near-duplicate objects across snapshots are later compacted together into a [[Packfile]], which stores most of them as deltas against each other rather than each in full, keeping the snapshot model space-efficient.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=21&annotation=XYVA9HSF)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=421&annotation=YKZGQCV5)
