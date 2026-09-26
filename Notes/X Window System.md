---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] X Window System[^1]
> The X Window System (X) is the server at the core of most Linux desktops, acting as a kind of "kernel" of the desktop by managing window rendering, display configuration, and input from devices such as keyboards and mice.

# Properties
- Just a server: it does not dictate how anything should act or appear. X client programs instead handle the user interface, connecting to the X server to ask it to draw windows; the server decides where to place and how to render them, and channels input back to the client.[^2]
- The one desktop component that is not easily replaced.[^1]
- First developed in the 1980s; despite significant evolution since, its original architecture can only be pushed so far, which motivated the newer [[Wayland]] protocol.[^3]
- Normally started by a [[Display Manager|display manager]] rather than directly from the command line, since starting the server alone defines no clients and so produces only a blank screen.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=323&annotation=6WB7GA32)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=323&annotation=SP9R6LJN)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=330&annotation=THZEI4Z2)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=325&annotation=USYW9448)
