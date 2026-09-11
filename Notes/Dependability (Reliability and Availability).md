---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Dependability: Reliability and Availability[^1]
> Reliability is a measure of continuous service accomplishment, or equivalently of the time to failure, from a given reference point; a component failure is called a fault. Availability is a measure of service accomplishment with respect to the alternation between periods of accomplishment and periods of interruption.

# Properties
- Reliability is commonly summarized by the mean time to failure (MTTF); improving MTTF is one lever (alongside detecting and tolerating faults) for improving overall [[Dependability via Redundancy|dependability]].
- Availability further accounts for how quickly service is restored after an interruption, so a system can have modest reliability yet high availability if failures are repaired quickly.
- Underlies error-detecting and error-correcting codes such as the [[Hamming Code]], which trade extra bits for the ability to detect or correct faults in stored or transmitted data.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=441&annotation=XD4YLJHD)
