---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] SHA-1 Hash Collision[^1]
> A SHA-1 hash collision occurs when two different pieces of content hash to the same 160-bit SHA-1 value that [[Git Snapshot Model|Git uses to identify its stored objects]].

# Properties
- If an object is ever committed that happens to hash identically to a different, previously stored object, Git treats them as the same object: it assumes the content was already written and reuses what is already stored, so checking out that hash will always return the first object's content rather than the second.
- Because a commit or object can be referred to by any prefix of its hash that is at least four characters long and still unambiguous within the repository's object database, this same uniqueness property is also what makes short, abbreviated hash references practical.
- Purely random collisions are astronomically unlikely, given SHA-1's 160-bit output space, but deliberately engineered collisions have been demonstrated in practice using significant computing power, which is why Git has been moving toward SHA-256, a hash function much more resistant to such deliberate collision attacks, as its default.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=225&annotation=PUVF6Z8M)
