---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Fairness Impossibility Theorem[^1]
> (Kleinberg, Mullainathan, and Raghavan; Chouldechova) When the base rates $p_a \ne p_b$ of the outcome differ between two groups, no imperfect risk score can simultaneously be *calibrated* within each group and have equal false positive rates and equal false negative rates across groups. For a binary classifier in a group with prevalence $p$,
> $$\begin{align}
> \mathrm{FPR} = \frac{p}{1-p} \cdot \frac{1-\mathrm{PPV}}{\mathrm{PPV}} \cdot \left(1 - \mathrm{FNR}\right)
> \end{align}$$
> so equal positive predictive value (a form of calibration) and equal FNR across groups with different $p$ force unequal FPR.

# Properties
- The criteria can hold simultaneously only if base rates are equal (or the predictor is perfect); otherwise "it is simply a fact about risk estimates when the base rates differ between two groups." This reconciles the COMPAS dispute, in which ProPublica (unequal error rates) and Northpointe (calibration) were each right by their own criterion.[^1]
- *Calibration* means that for every risk level, the probability of the outcome is the same regardless of group; equalising false positive and negative rates requires giving it up. Yet calibration alone provides little guarantee that decisions are equitable.[^2]
- The impossibility is mathematical, so it applies to any classification, by algorithm or by human decision-makers; any risk-assessment instrument is guaranteed to exhibit some headline-worthy unfairness.[^3]
- Impossibility of satisfying all criteria does not preclude choosing better trade-offs, which depend on context: in criminal justice both false positives and false negatives carry serious human costs.[^4]
- Related: [[Algorithmic Bias]], [[Redundant Encoding]].

[^1]: [Christian, 2021, p. 74](zotero://open-pdf/library/items/P27SWKW4?page=74&annotation=WULZ8DC2); [Christian, 2021, p. 74](zotero://open-pdf/library/items/P27SWKW4?page=74&annotation=UM3AKZHU); [Christian, 2021, p. 74](zotero://open-pdf/library/items/P27SWKW4?page=74&annotation=XTRMLHA3)
[^2]: [Christian, 2021, p. 76](zotero://open-pdf/library/items/P27SWKW4?page=76&annotation=GRPWZDV4); [Christian, 2021, p. 76](zotero://open-pdf/library/items/P27SWKW4?page=76&annotation=FKWIL93R); [Christian, 2021, p. 77](zotero://open-pdf/library/items/P27SWKW4?page=77&annotation=G7MR8ITE)
[^3]: [Christian, 2021, p. 74](zotero://open-pdf/library/items/P27SWKW4?page=74&annotation=8ET79R25); [Christian, 2021, p. 74](zotero://open-pdf/library/items/P27SWKW4?page=74&annotation=DCV36IN6); [Christian, 2021, p. 75](zotero://open-pdf/library/items/P27SWKW4?page=75&annotation=MWKYEYY4)
[^4]: [Christian, 2021, p. 75](zotero://open-pdf/library/items/P27SWKW4?page=75&annotation=Y98P7CQS); [Christian, 2021, p. 76](zotero://open-pdf/library/items/P27SWKW4?page=76&annotation=VEVLZMZH); [Christian, 2021, p. 77](zotero://open-pdf/library/items/P27SWKW4?page=77&annotation=TDB8MHYQ); [Christian, 2021, p. 77](zotero://open-pdf/library/items/P27SWKW4?page=77&annotation=MB62QTKT)
