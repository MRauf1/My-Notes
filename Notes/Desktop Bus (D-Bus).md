---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Desktop Bus (D-Bus)[^1]
> D-Bus is a message-passing system that serves as an [[Inter-Process Communication|interprocess communication]] mechanism letting desktop applications talk to each other, and letting most Linux systems notify processes of system events, such as inserting a USB drive.

# Properties
- Itself just a library standardizing IPC with a protocol and supporting functions for any two processes to talk to each other; alone it offers little more than a fancier version of normal IPC facilities such as [[Unix Domain Socket|Unix domain sockets]].[^2]
- Made useful by a central hub, `dbus-daemon`: processes that need to react to events connect to it and register for certain kinds of events, while other processes create the events, which `dbus-daemon` retransmits to the interested applications.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=330&annotation=NB7VUQ4K)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=331&annotation=URSNBZCT)
