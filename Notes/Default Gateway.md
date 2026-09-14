---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Default Gateway[^1]
> The default gateway is the [[Router|router]] address a host sends a message to whenever no more specific rule in its routing table matches the destination.

# Properties
- The kernel consults a routing table to decide, for each outgoing packet, where on the network it should be sent.[^2]
- Corresponds to the routing table's default route, which matches any address on the Internet.[^1]
- A host with no default gateway configured cannot reach hosts outside the destinations already listed in its routing table.[^1]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=221&annotation=355GUWZQ)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=221&annotation=MURC789R)
