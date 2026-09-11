---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Word[^1]
> The natural unit of access in a computer, usually a group of 32 bits; corresponds to the size of a [[Register (Computer Architecture)|register]] in the MIPS architecture.

# Properties
- Since architectures typically address individual 8-bit bytes, the address of a word matches the address of one of its bytes, and addresses of sequential words differ by 4 (not 1) — a common pitfall in assembly-language programming.
- Many architectures, including MIPS, impose an [[Alignment Restriction]] requiring words to start at addresses that are multiples of 4.
- DRAM for [[Main Memory]] is sized in binary units (gebibytes $2^{30}$, tebibytes $2^{40}$) rather than decimal units (gigabytes $10^9$, terabytes $10^{12}$), since memory addresses used in loads and stores are binary numbers.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=89&annotation=SWTKGNLK)
