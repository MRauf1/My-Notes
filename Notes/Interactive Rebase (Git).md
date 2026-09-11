---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Interactive Rebase[^1]
> Interactive rebase is a mode of [[Rebasing (Git)|rebasing]] in which each commit being replayed can individually be edited — its message or content changed, or the commit reordered, squashed together with another, split apart, or dropped entirely — rather than simply being replayed unchanged.

# Properties
- Since Git has no dedicated tool for modifying a specific commit that is not the most recent one, interactive rebase is the general mechanism used to rewrite history further back than the last commit.
- Because each commit's identity depends on the content and hash of its parent (see [[Git Snapshot Model]]), editing, reordering, or removing any commit in the rebased range forces every commit after it to be rebuilt as well; the more commits lie after the one being changed, the more must be recreated, which can surface more merge conflicts to resolve.
- Like any [[Rebasing (Git)|rebase]], it should never be used on commits that have already been pushed and that other people may have based work on, per the [[Golden Rule of Rebasing]].

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=250&annotation=N765D8DB)
