---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Secondary Memory[^1]
> Nonvolatile memory used to store programs and data between runs, forming the layer of the [[Memory Hierarchy]] below [[Main Memory]]. It typically consists of flash memory in personal mobile devices and magnetic disks in servers.

# Types
- Magnetic disk (hard disk) — rotating platters coated with a magnetic recording material; access times of about 5–20 milliseconds.
- Flash memory — a nonvolatile semiconductor memory that is slower and cheaper per bit than DRAM but faster and more expensive per bit than magnetic disk; access times of about 5–50 microseconds.

# Properties
- Nonvolatile: unlike [[Main Memory]], it retains data even without power.
- A layer of the [[Memory Hierarchy]].
- A magnetic disk surface is divided into concentric tracks, each divided in turn into sectors, the smallest unit read or written on the disk; a cylinder is the set of tracks at a given position across every surface. Accessing a sector requires a seek (positioning the read/write head over the correct track) followed by rotational latency (waiting for the sector to rotate under the head, on average half a rotation) before the data itself can be transferred.
- Disks are cheaper per bit than semiconductor memory at high capacity but have much slower (mechanical) access times; unlike flash memory, disks have no write wear-out problem, but flash's greater ruggedness suits the jostling of personal mobile devices better.
- Flash memory is a type of electrically erasable programmable read-only memory (EEPROM); because writes wear out flash cells, controllers spread writes across less-used blocks (wear leveling) to extend the device's lifetime.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=46&annotation=4JG7Y7BM)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=405&annotation=LYIBV8UW)
