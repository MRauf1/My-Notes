---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Long-Running Branch[^1]
> A long-running branch is a [[Branch (Git)|branch]] that persists for an extended period at its own level of stability; as work on it reaches a more stable level, it is merged into the branch representing the next level of stability above it.

# Properties
- Maintaining multiple long-running branches at different stability levels is not strictly necessary, but is often helpful for very large or complex projects.
- A common two-level instance of this pattern keeps one long-running branch reserved for stable releases and a second where new work is integrated on an ongoing basis; the stable branch is fast-forwarded to the development branch's tip only when a release is cut, so that cloning developers can choose between building on the latest stable release or tracking the more cutting-edge, in-progress content.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=89&annotation=PYP7UBWB)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=163&annotation=TGB2JM5J)
