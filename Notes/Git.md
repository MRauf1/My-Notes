---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git[^1]
> Git is a [[Distributed Version Control System]] created by the Linux kernel development community, and in particular Linus Torvalds, based on lessons learned from their prior use of BitKeeper.

# Properties
- Stores project history as a series of complete snapshots rather than as accumulated per-file differences — see [[Git Snapshot Model]].
- Does not explicitly record when a file is renamed — see [[Git Rename Detection]].
- Nearly all operations only require local files and resources to run — see [[Locality of Git Operations]].
- Tracked files move between the working tree, staging area, and Git directory as they pass through the modified, staged, and committed states — see [[Git File States]].
- Behavior is controlled by configuration variables that can be set at multiple overriding scopes — see [[Git Configuration Hierarchy]].
- A file matching a pattern listed in a [[Gitignore|gitignore file]] is excluded from tracking and from untracked-file reporting.
- Each commit records both an author and a committer — see [[Author and Committer (Git)|Author and Committer]].
- The last commit on a branch can be replaced entirely rather than edited in place — see [[Amending a Commit]].
- A project's history can be synchronized with a [[Remote Repository (Git)|remote repository]], another copy of the project hosted elsewhere, over one of several [[Git Transfer Protocol|transfer protocols]].
- Specific commits can be marked with a [[Git Tag]] for later reference, such as to denote a release.
- Work can diverge from the main line of development on a [[Branch (Git)|branch]], a lightweight, movable pointer to a commit; [[HEAD (Git)|HEAD]] records which branch is currently checked out.
- Two diverged branches can be integrated either by [[Three-Way Merge|merging]] them together into a new [[Merge Commit]], or by [[Rebasing (Git)|rebasing]] one branch's commits on top of the other to produce a linear history.
- Because its operations almost always only add data to its database rather than remove or overwrite it, a committed snapshot — even one on a deleted branch or one superseded by amending — is very difficult to make unrecoverable, especially once it has been pushed to another repository; by contrast, changes that were never committed, or that are overwritten by restoring a tracked file to its last staged or committed version, are easily and often permanently lost.[^2]

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=20&annotation=M7QQYERU)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=55&annotation=PRI3E9DK)
