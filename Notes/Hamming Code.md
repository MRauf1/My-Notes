---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Hamming Code[^1]
> An error detection and correction scheme built around the Hamming distance between bit patterns — the minimum number of bits that differ between any two correct (codeword) patterns. A larger Hamming distance lets more errors be detected or corrected: distance 2 detects single-bit errors, distance 3 corrects single-bit errors, and distance 4 corrects single-bit errors while detecting double-bit errors.

# Types
- Parity code — the simplest error detection code (a code that can detect an error without locating or correcting it): the number of 1s in a word is counted, and a parity bit is stored so that the total, including the parity bit, is always even (or always odd); a mismatch on read-back signals an error, achieving a Hamming distance of 2.
- Hamming Error Correction Code (ECC) — Hamming's mapping of data into a distance-3 code, using extra parity bits positioned to allow not just detection but identification of which single bit is wrong, so it can be corrected; adding one further whole-word parity bit raises the distance to 4, adding double-bit error detection on top of single-bit error correction.

# Properties
- Named for Richard Hamming, who developed these codes to protect data such as [[Main Memory]] contents from bit-flip faults.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=443&annotation=I8KFAEI3)
