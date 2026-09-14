---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] MAC Address[^1]
> A Media Access Control (MAC) address, or hardware address, is the address that identifies a device on an Ethernet network, independent of and distinct from its [[IP Address|IP address]].

# Properties
- Unique to a host's own Ethernet network, but not necessarily to a larger software network such as the Internet.[^1]
- Ethernet devices send messages in frames, wrappers around the transmitted data that carry the origin and destination MAC addresses.[^1]
- A frame cannot leave its own physical network directly; a [[Router|router]] instead takes the data out of a frame, repackages it, and sends it to a host on a different physical network — exactly what happens on the Internet.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=224&annotation=F7QBYJ3G)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=224&annotation=BYUYR85T)
