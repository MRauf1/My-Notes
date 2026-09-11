---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Dynamic Power Dissipation (CMOS)[^1]
> In CMOS (complementary metal oxide semiconductor) circuits, the dominant source of energy consumption is dynamic energy: energy consumed when a [[Integrated Circuit Manufacturing|transistor]] switches state. The energy of a single transition is proportional to the transistor's capacitive load and the square of the voltage applied,
> $$
> \text{Energy}_{dynamic} \propto \text{Capacitive Load} \times \text{Voltage}^2,
> $$
> and the power required is the product of that energy and the frequency of transitions,
> $$
> \text{Power}_{dynamic} \propto \tfrac{1}{2} \times \text{Capacitive Load} \times \text{Voltage}^2 \times \text{Frequency Switched}.
> $$

# Properties
- Frequency switched is a function of the clock rate; capacitive load per transistor depends on the fanout (number of transistors connected to an output) and the fabrication technology.
- Lowering voltage reduces power quadratically and drove power reductions across technology generations, but voltage cannot be lowered indefinitely: transistors become too leaky.
- Static energy consumption, from leakage current that flows even when a transistor is off, is typically responsible for about 40% of energy consumption in server chips, and increases with transistor count even when transistors are switched off.
- Power must be distributed around a chip and removed as heat; this is a major expense in Warehouse Scale Computers.
- Fallacy: computers at low utilization use little power — in practice a large fraction of peak power is consumed even at low load.
- Fallacy: designing for performance and designing for energy efficiency are unrelated goals — because energy is power integrated over time, an optimization that reduces execution time often reduces total energy even if it draws slightly more power while active, since the rest of the system also consumes energy for a shorter duration.
- Energy efficiency, measured in joules rather than watts, has replaced die area as the most critical resource in microprocessor design.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=64&annotation=Q542Q67Y)
