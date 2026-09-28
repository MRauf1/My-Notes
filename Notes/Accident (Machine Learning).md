---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Accident (Machine Learning)[^1]
> Unintended and harmful behaviour that may emerge from a machine learning system when its designers specify the wrong [[Objective Function|objective function]], are not careful about the learning process, or commit other machine-learning-related implementation errors.

# Types
Accidents are classified by where in the design process things went wrong:[^2]
- **Wrong formal objective**: maximising the specified objective leads to harm even in the limit of perfect learning and infinite data.
	- [[Negative Side Effects (Machine Learning)|Negative Side Effects]]
	- [[Reward Hacking]]
- **Correct objective, but too expensive to evaluate frequently**: harm arises from bad extrapolation from limited samples of the true objective.
	- [[Scalable Oversight]]
- **Correct objective, but bad behaviour during learning**: harm arises from insufficient or poorly curated training data or an insufficiently expressive model, even though perfect beliefs would give correct behaviour.
	- [[Safe Exploration]]
	- [[Robustness to Distributional Shift]]

# Properties
- A concrete, machine-learning-grounded framing of AI safety, and a practical face of the [[Value Alignment Problem]].
- Risk grows with the system's autonomy: systems that only output recommendations to humans have limited potential for harm, whereas systems exerting direct control over the world can cause harm that humans cannot necessarily correct or oversee.[^3]
- Summarised in [[Concrete Problems in AI Safety (Amodei et al)]].

[^1]: [Amodei et al., 2016, p. 1](zotero://open-pdf/library/items/JKJMXPTZ?page=1&annotation=C53MEIG9); [Amodei et al., 2016, p. 1](zotero://open-pdf/library/items/JKJMXPTZ?page=1&annotation=8GYD9G4T); [Amodei et al., 2016, p. 2](zotero://open-pdf/library/items/JKJMXPTZ?page=2&annotation=TUE3S6AL)
[^2]: [Amodei et al., 2016, p. 2](zotero://open-pdf/library/items/JKJMXPTZ?page=2&annotation=YKMIHDFH); [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=VUX89RGI); [Amodei et al., 2016, p. 3](zotero://open-pdf/library/items/JKJMXPTZ?page=3&annotation=W97US924)
[^3]: [Amodei et al., 2016, p. 4](zotero://open-pdf/library/items/JKJMXPTZ?page=4&annotation=WI8W4CBB)
