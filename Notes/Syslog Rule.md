---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Syslog Rule[^1]
> A traditional [[Syslog|syslog]] rule pairs a selector, which matches the facility and priority of log messages, with an action that determines where matching messages are sent.

# Properties
- The facility is a general category of message.[^2]
- The priority follows the facility after a dot (`.`); priorities are ordered from lowest to highest as debug, info, notice, warning, err, crit, alert, and emerg.[^3]
- Configuration extensions to the rule syntax are called directives, usually begin with `$`, and commonly include loading additional configuration files.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=176&annotation=CJEZ6673)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=177&annotation=J82WPAHS)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=177&annotation=S5GSTJAX)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=177&annotation=TZS7PS9M)
