---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Character Encoding[^1]
> A representation mapping characters to fixed-size bit patterns, most commonly 8-bit bytes. The American Standard Code for Information Interchange (ASCII) is the representation nearly every architecture follows for the alphabets of English-like languages; Unicode is a universal encoding covering the alphabets of most human languages.

# Properties
- MIPS provides dedicated data-transfer instructions for characters (load/store byte) and for 16-bit halfwords, since forcing every character or short string into a full [[Word (Computer Architecture)|word]] would waste space; a `char` variable on the [[Call Stack]] is nonetheless often padded to a full word for stack-alignment convenience.
- A string, a variable-length sequence of characters, can be represented in one of three ways: reserving its first position for its length, storing its length in an accompanying variable, or marking its final position with a dedicated terminator character.
- [[Unicode]] generalizes this idea beyond a fixed 8-bit byte per character, defining variable-length encodings such as [[UTF-8]] that represent a much larger set of character codes (code points) as one or more bytes each.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=129&annotation=479PP64N)
