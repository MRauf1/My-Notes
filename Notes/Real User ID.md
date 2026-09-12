---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Real User ID[^1]
> The real user ID (ruid) is the [[Process User ID|process user ID]] that indicates who initiated a process — the "owner" that may interact with it.

# Properties
- Most significantly defines which user may kill or send signals to the running process.[^1]
- Kept as the original invoking user's ID when a setuid program sets the [[Effective User ID]] to the program owner during execution.[^1]
- `sudo` and other setuid programs explicitly change both the real and effective user IDs, so killing a process started with `sudo` still requires `sudo`, rather than the invoking user's own regular privileges.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=43BCA3IB)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=188&annotation=SI7EUE5I)
