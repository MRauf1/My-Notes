---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Unix Domain Socket[^1]
> A Unix domain socket is a special-purpose [[Device File]], frequently used for interprocess communication, represented by a socket file that is often found outside the `/dev` directory.

# Properties
- Behaves almost exactly like a network [[Socket (Unix)|socket]]: it can listen for and accept connections, and different socket types can make it act like TCP or UDP.[^2]
- Not itself a network socket — there is no actual network behind one, and no networking needs to be configured to use it.[^3]
- Need not be bound to a socket file: a process can instead create an unnamed Unix domain socket and share its address directly with another process.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=72&annotation=JQAKAHJP)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=272&annotation=3P5G8FPC)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=272&annotation=DEPPLKTN)
