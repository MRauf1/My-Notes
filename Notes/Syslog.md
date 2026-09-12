---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Syslog[^1]
> Syslog is the service to which most Linux system programs write their diagnostic output, so it can be filtered and routed to a file, the screen, users, or discarded.

# Properties
- Traditionally implemented by the syslogd daemon, which waits for messages and, depending on the type received, funnels the output to a destination or ignores it.[^1]
- One of the most important parts of the system: when something goes wrong and there is no obvious starting point, the system log files are usually the first place to check.[^2]
- Governed by [[Syslog Rule|rules]] that determine which messages are caught and where they are sent.[^3]
- Its configuration format has never had a true cross-Unix standard, and Linux system logging continues to change.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=175&annotation=Z2TCNB5Y)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=176&annotation=2ZR5PACB)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=176&annotation=CJEZ6673)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=178&annotation=9K4KB55L)
