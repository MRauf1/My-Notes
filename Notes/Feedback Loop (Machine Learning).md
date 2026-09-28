---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Feedback Loop (Machine Learning)[^1]
> The phenomenon in which a deployed predictive model changes the reality it models, including the data later used to train it, violating the common assumption that a model does not affect what it predicts.

# Properties
- **Ground truth is not always the ground truth**: one must make sure one is predicting what one thinks one is predicting. E.g. predictive policing trained on arrest data predicts crime that becomes known to police, i.e. *future policing*, not future crime.[^2]
- Because predictions direct the police activity that generates future arrest data, a long-term loop arises: "selection bias meets [[Confirmation Bias|confirmation bias]]", and the model reinforces rather than corrects the over-representation of previously flagged locations, sculpting the reality it is meant to predict.[^3]
- **Use only as directed**: even an accurate model may be used for purposes other than intended; we should know exactly what a tool predicts and be cautious outside those parameters.[^4]
- **Prediction-intervention gap**: predictions are not ends in themselves, e.g. differential enforcement may embolden the overlooked group more than it deters the scrutinised one; predicting a missed court date does not imply jailing is the right intervention; a world with 99% less crime beats one where crime is predicted with 99% accuracy.[^5]
- An ML model "is by definition a tool to predict the future, given that it looks like the past", hence fundamentally the wrong tool where one designs interventions to change the world (Hardt).[^6]
- A form of [[Robustness to Distributional Shift|distributional shift]] caused by the model itself, and a source of [[Algorithmic Bias]].

[^1]: [Christian, 2021, p. 54](zotero://open-pdf/library/items/P27SWKW4?page=54&annotation=3U785KRY)
[^2]: [Christian, 2021, p. 79](zotero://open-pdf/library/items/P27SWKW4?page=79&annotation=BLT6EP9C); [Christian, 2021, p. 80](zotero://open-pdf/library/items/P27SWKW4?page=80&annotation=F6GBS4M5); [Christian, 2021, p. 80](zotero://open-pdf/library/items/P27SWKW4?page=80&annotation=HDNZTXZ7)
[^3]: [Christian, 2021, p. 81](zotero://open-pdf/library/items/P27SWKW4?page=81&annotation=8K5XS5XQ); [Christian, 2021, p. 81](zotero://open-pdf/library/items/P27SWKW4?page=81&annotation=V9Q5NA98); [Christian, 2021, p. 81](zotero://open-pdf/library/items/P27SWKW4?page=81&annotation=SMUUWV7V)
[^4]: [Christian, 2021, p. 82](zotero://open-pdf/library/items/P27SWKW4?page=82&annotation=IRXLJ9GE); [Christian, 2021, p. 83](zotero://open-pdf/library/items/P27SWKW4?page=83&annotation=DXF5YNME)
[^5]: [Christian, 2021, p. 83](zotero://open-pdf/library/items/P27SWKW4?page=83&annotation=EXRRHT2J); [Christian, 2021, p. 83](zotero://open-pdf/library/items/P27SWKW4?page=83&annotation=LQUEYNDM); [Christian, 2021, p. 84](zotero://open-pdf/library/items/P27SWKW4?page=84&annotation=VEZUQA23); [Christian, 2021, p. 84](zotero://open-pdf/library/items/P27SWKW4?page=84&annotation=UZ8SLZRG)
[^6]: [Christian, 2021, p. 85](zotero://open-pdf/library/items/P27SWKW4?page=85&annotation=JQFW2XNZ)
