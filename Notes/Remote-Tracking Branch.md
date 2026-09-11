---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Remote-Tracking Branch[^1]
> A remote-tracking branch is a local reference that records the state of a branch in a [[Remote Repository (Git)|remote repository]] as of the last time the two were synchronized; it takes the form `<remote>/<branch>`.

# Properties
- Remote-tracking branches cannot be moved directly by the user; [[Git]] moves them automatically during network communication with the remote, so they act as bookmarks recalling where each remote branch stood the last time it was contacted.
- Synchronizing with a remote looks up that remote's location, downloads any data not yet present locally, and updates the corresponding remote-tracking branch pointers to reflect the remote's current state, without altering any local branch.
- Downloading a new remote-tracking branch does not create a local, editable branch from it; until a [[Tracking Branch (Git)|tracking branch]] is created from it, it remains only an unmovable pointer.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=92&annotation=U7ZJGL5Y)
