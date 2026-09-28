---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Improper Linear Model[^1]
> (Dawes and Corrigan) A linear prediction model whose weights are not optimised on data, e.g. equal weights on standardised predictors,
> $$\begin{align}
> \hat y = \sum_{i=1}^{k} w_i z_i, \qquad w_i = 1 \ \text{ (or random with } w_i > 0\text{)},
> \end{align}$$
> where $z_i$ are standardised versions of predictors chosen by experts.

# Properties
- Statistical prediction beats clinical (expert) judgement: experts given the model's prediction still did worse than the prediction alone, and adding expert judgements as model inputs added little. Human judgement alone is not viable, yet complex models are not necessary to beat it.[^2]
- Models with random positive weights matched or beat expert judges; equal weights did even better, and often beat optimally fitted regressions, since optimal weights overfit to a particular context and fail to transfer, whereas equal weights are robust across contexts.[^3]
- Reasons: many high-level relationships are *conditionally monotone*; measurements are noisy, and the noisier a measurement, the more appropriate linear use; and optimal weights require an objective and ground truth we often cannot define or wait for. Even with no data and unclear goals, improper models serve at least as well as intuition.[^4]
- Expertise lies in choosing *what to look at*: the models combine exactly the variables established by generations of best practice, so human wisdom is embodied in the standards determining which information reaches the decision-maker. "The whole trick is to know what variables to look at and then to know how to add."[^5]
- Finding optimal simple rules is itself NP-hard.[^6]
- Illustrates [[Robustness to Distributional Shift]] and the [[Bias-Variance Tradeoff]].

[^1]: [Christian, 2021, p. 100](zotero://open-pdf/library/items/P27SWKW4?page=100&annotation=24FAI2IM)
[^2]: [Christian, 2021, p. 99](zotero://open-pdf/library/items/P27SWKW4?page=99&annotation=63X5RUS2); [Christian, 2021, p. 99](zotero://open-pdf/library/items/P27SWKW4?page=99&annotation=VALNIIUW)
[^3]: [Christian, 2021, p. 100](zotero://open-pdf/library/items/P27SWKW4?page=100&annotation=6TY5BS5K); [Christian, 2021, p. 101](zotero://open-pdf/library/items/P27SWKW4?page=101&annotation=T3PCF6NH)
[^4]: [Christian, 2021, p. 101](zotero://open-pdf/library/items/P27SWKW4?page=101&annotation=KFAR5BFN); [Christian, 2021, p. 101](zotero://open-pdf/library/items/P27SWKW4?page=101&annotation=J3PW4LPX); [Christian, 2021, p. 101](zotero://open-pdf/library/items/P27SWKW4?page=101&annotation=CHWBCJWF); [Christian, 2021, p. 102](zotero://open-pdf/library/items/P27SWKW4?page=102&annotation=ZFVY5QQM); [Christian, 2021, p. 102](zotero://open-pdf/library/items/P27SWKW4?page=102&annotation=RXYN6ARQ)
[^5]: [Christian, 2021, p. 102](zotero://open-pdf/library/items/P27SWKW4?page=102&annotation=E852Y68C); [Christian, 2021, p. 102](zotero://open-pdf/library/items/P27SWKW4?page=102&annotation=VCCQMKWF); [Christian, 2021, p. 103](zotero://open-pdf/library/items/P27SWKW4?page=103&annotation=RTQ5YD2V); [Christian, 2021, p. 103](zotero://open-pdf/library/items/P27SWKW4?page=103&annotation=LXFBALBE)
[^6]: [Christian, 2021, p. 104](zotero://open-pdf/library/items/P27SWKW4?page=104&annotation=5PPFZHUH)
