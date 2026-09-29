---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Interpretability (Machine Learning)[^1]
> The degree to which humans can understand what a trained model has learned and why it makes its predictions, allowing them to detect and correct problematic learned relationships before deployment.

# Types
- Intrinsically interpretable models - rule-based models (among the most easily interpreted) and generalized additive models (sums of per-feature shape functions, generalising the [[Generalized Linear Model]]), which can match neural-network accuracy while being far more transparent.[^2]
- [[Saliency Map|Saliency maps]]
- [[Feature Visualization]]
- [[Concept Activation Vector|Concept activation vectors]] (TCAV)
- [[Multitask Learning]], which can improve transparency as a side effect.

# Properties
- Motivating case (Caruana): a rule-based pneumonia model learned that asthmatics had lower mortality, a real correlation caused by the more intensive care they received; acting on it would deny them that care. An equally accurate neural network must have learned the same logic invisibly, plus unknown others, so it could not be safely deployed. Later GAMs revealed many similar spurious "protective" factors (chest pain, heart disease, age over 100).[^3]
- Deep learning systems can be enormous and cannot be understood by examination, so it is usually unknown how, or based on what information, they make decisions; this motivates the sub-field of explainable AI.[^6]
- The field often observes that the most powerful models are the least intelligible and vice versa ([[Model Flexibility vs. Interpretability]]).[^4]
- Editing an interpretable model is straightforward; correcting a black box is harder, though not impossible.[^3]
- Explanation has an inherently human dimension requiring HCI and cognitive science, and may resist a single mathematical definition, which makes computer scientists uncomfortable (Been Kim).[^5]

[^1]: [Christian, 2021, p. 90](zotero://open-pdf/library/items/P27SWKW4?page=90&annotation=MLGJIB67)
[^2]: [Christian, 2021, p. 88](zotero://open-pdf/library/items/P27SWKW4?page=88&annotation=K8RTND5B); [Christian, 2021, p. 91](zotero://open-pdf/library/items/P27SWKW4?page=91&annotation=JJRYJVSB)
[^3]: [Christian, 2021, p. 89](zotero://open-pdf/library/items/P27SWKW4?page=89&annotation=YEFFIMEX); [Christian, 2021, p. 89](zotero://open-pdf/library/items/P27SWKW4?page=89&annotation=G9WVPINN); [Christian, 2021, p. 89](zotero://open-pdf/library/items/P27SWKW4?page=89&annotation=AETGAJIG); [Christian, 2021, p. 90](zotero://open-pdf/library/items/P27SWKW4?page=90&annotation=JZ9IDWNJ); [Christian, 2021, p. 90](zotero://open-pdf/library/items/P27SWKW4?page=90&annotation=EHCZHD4P); [Christian, 2021, p. 91](zotero://open-pdf/library/items/P27SWKW4?page=91&annotation=TSIV4IHH); [Christian, 2021, p. 91](zotero://open-pdf/library/items/P27SWKW4?page=91&annotation=4KUQ4RY3); [Christian, 2021, p. 91](zotero://open-pdf/library/items/P27SWKW4?page=91&annotation=DSYIDE8I)
[^4]: [Christian, 2021, p. 90](zotero://open-pdf/library/items/P27SWKW4?page=90&annotation=3W8W5BWM)
[^5]: [Christian, 2021, p. 118](zotero://open-pdf/library/items/P27SWKW4?page=118&annotation=LD8N8LL8); [Christian, 2021, p. 118](zotero://open-pdf/library/items/P27SWKW4?page=118&annotation=QDBCYADE)
[^6]: [Prince, p. 13](zotero://open-pdf/library/items/BWT7FYX5?page=27&annotation=B2NVM6H9)
