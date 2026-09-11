---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Rebasing[^1]
> Rebasing is an alternative to merging in [[Git]] that integrates one branch's changes into another by taking the patch introduced by each commit on the first branch and replaying those patches, one by one, on top of the second branch, rather than combining the two branches' endpoints directly.

# Properties
- Mechanically, Git locates the common ancestor of the two branches, computes the diff introduced by each commit made on the branch being rebased since that ancestor, resets that branch to point at the branch it is being rebased onto, and then reapplies each saved diff in turn as a new commit.
- The final snapshot produced is identical to the snapshot a [[Three-Way Merge]] of the same two branches would produce — only the recorded history differs: rebasing yields a linear history in which the work appears to have happened in series, even though it originally happened in parallel, whereas merging preserves the branches' original, divergent history via a [[Merge Commit]].
- Because rebasing recreates each replayed commit with a new [[Version Control System|checksum]], Git additionally computes a [[Patch-ID (Git)|patch-id]] — a checksum of just the patch a commit introduces — which lets it recognize when a rebased commit reintroduces a change that already exists elsewhere in the target branch's history.
- Some teams prefer rebasing over merging because it produces a clean, curated, linear narrative of a project's development for future readers, rather than preserving a literal, and possibly messy, record of exactly how the work was carried out; other teams treat unaltered history as a valuable historical record and avoid rewriting it for this reason, so neither approach is universally "better."
- See the [[Golden Rule of Rebasing]] for when rebasing is safe to perform.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=102&annotation=RR8W34H9)
