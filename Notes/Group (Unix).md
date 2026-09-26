---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Group (Unix)[^1]
> A group is a set of users, used primarily to let its members share file access with one another.

# Properties
- Composed of [[User (Unix)|users]].
- An account normally has one primary group and can additionally belong to supplementary groups; group membership lets administrators grant access to a whole set of users without assigning permissions to each account individually.[^2]
- Recorded in the [[Group File|group file]] (`/etc/group`), which maps group names to numeric GIDs and lists each group's explicit members.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Linux Journey: User Management](https://labex.io/linuxjourney/courses/user-management)
