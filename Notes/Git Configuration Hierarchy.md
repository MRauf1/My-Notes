---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Git Configuration Hierarchy[^1]
> The variables that control how [[Git]] looks and operates can be configured at several different scopes, each stored in its own file, where values set at a narrower, more specific scope override values set at a broader one.

# Properties
- When the same configuration key is defined in more than one of these files, Git uses whichever value it read last, i.e. the value from the most specific applicable file.
- Because the same setting can be defined in multiple files, the value in effect is not always obvious; Git can report which specific configuration file ultimately determined a given value.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=27&annotation=C9DB9AZM)
