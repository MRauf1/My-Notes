---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Port (Networking)[^1]
> A port is a number that, together with a host's [[IP Address|IP address]], identifies a particular application's connection on that host — a further subdivision, much like a mailbox number subdivides a postal address.

# Properties
- The process initiating a connection is the client; the process listening for it is the server.[^2]
- A connection is identified by the pair of IP addresses and port numbers on each end — a local port and a remote port.[^2]
- The client picks an unused port on its own side, called an ephemeral port when dynamically assigned, but almost always connects to some well-known port on the server side.[^3]
- On Linux, only the superuser may use ports 1 through 1023; any user process may listen on or connect from ports 1024 and up.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=235&annotation=WWVN6DG2)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=235&annotation=EN46LP65)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=236&annotation=7V5HMPDE)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=236&annotation=5DDMB7SG)
