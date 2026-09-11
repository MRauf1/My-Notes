---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Structured Logic: PLA and ROM[^1]
> Regular, table-like hardware structures for implementing arbitrary combinational logic functions, as an alternative to custom-designed gate networks.

# Types
- Programmable logic array (PLA) — takes a set of inputs and their complements through two logic stages: the first forms product terms (minterms), sets of inputs joined by AND; the second forms a sum (OR) of those product terms, so a PLA implements any logic function as a sum of products.
- Read-only memory (ROM) — a memory whose contents are fixed at creation and thereafter only read; used as structured logic by treating a logic function's input terms as the memory's address inputs and its output bits as the corresponding word's stored bits. A programmable ROM (PROM) is a ROM the designer can program once its contents are known, rather than one fixed during manufacture.

# Properties
- Both let a designer implement an arbitrary combinational function (see [[Datapath Element]]) by populating a fixed, regular structure rather than laying out custom gates — a form of [[Field-Programmable Device|field-programmable device]] when the structure is configurable by the end user rather than only at the factory.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=691&annotation=JD345U73)
