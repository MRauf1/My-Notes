---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Plumbing and Porcelain[^1]
> [[Git]]'s commands are divided into low-level "plumbing" commands, which expose Git's internal data structures and operations directly, and high-level "porcelain" commands, which wrap plumbing commands into a friendlier interface for everyday use.

# Properties
- Plumbing commands are generally not used in day-to-day work, but remain useful for inspecting Git's internal state directly, such as seeing exactly which [[Reference (Git)|references]] a remote server exposes.
- This split reflects Git's origins: it began as a low-level toolkit for building a version control system, with subcommands meant to be chained together Unix-style or called from scripts, rather than as a complete, user-friendly VCS in itself; porcelain commands were layered on top afterward for everyday use.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=202&annotation=UNMS54BB)
[^2]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=420&annotation=YIN2MCDY)
