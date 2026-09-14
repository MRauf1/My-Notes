---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Network Address Translation (NAT)[^1]
> NAT is the mechanism by which a [[Router|router]] lets many hosts on a private network share a single public [[IP Address]], transforming packets as it moves them between the private network and the Internet.

# Properties
- Needed because certain IP addresses are not actually visible to the whole Internet; they belong to private networks.[^1]
- Hosts on the Internet know only how to connect to the router; the private hosts behind it need no special configuration beyond using the router as their [[Default Gateway|default gateway]].[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=241&annotation=R9ZKQGRU)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=242&annotation=8L5L7PH6)
