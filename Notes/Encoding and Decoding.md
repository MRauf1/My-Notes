---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Encoding and Decoding[^1]
> Encoding is the process of translating a string of characters into its raw-bytes form, according to some [[Character Encoding|encoding]] broad enough to store the string's characters; decoding is the reverse process, translating a string of raw bytes back into characters, according to the same encoding originally used to produce those bytes.

# Properties
- A decoded [[Unicode]] code point may occupy a different number of bytes in memory depending on the programming-language implementation storing it, but its encoded, on-disk or on-the-wire byte format is fixed entirely by the chosen encoding, independent of whatever language created or reads it — which is what makes encoded text portable across different tools and languages[^2].
- Because decoded text is generally easier for a program to work with than its raw encoded bytes, data is normally decoded once it is loaded and only encoded again for storage or transmission[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1439&annotation=ZAY96RFP)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1441&annotation=ZQ2Q57R5)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1442&annotation=N53WFCJU)
