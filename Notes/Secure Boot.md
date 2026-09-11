---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Secure Boot[^1]
> Secure boot is a [[UEFI]] mechanism that requires a boot loader to be digitally signed by a trusted authority before the firmware will run it.

# Properties
- Blocks unsigned boot loaders — which includes most Linux distributions by default — from loading.
- Can be worked around by disabling secure boot in the EFI settings (imperfect for dual-boot systems) or by using a distribution-provided signed boot loader.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=131&annotation=XNDKH7H4)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=131&annotation=G9Z2U7GG)
